#!/usr/bin/env python3
"""
TFGrid Studio Registry - Update app versions with latest commits
"""

import yaml
import subprocess
import json
from datetime import datetime
import os
import shutil

def get_latest_commit(repo_url):
    """Get latest commit hash from a repository"""
    print(f"Fetching latest commit for {repo_url}...")
    
    try:
        # Create temporary directory
        temp_dir = "/tmp/repo_update_"
        temp_dir += str(datetime.now().timestamp())
        os.makedirs(temp_dir, exist_ok=True)
        
        # Clone repository
        result = subprocess.run([
            "git", "clone", "--quiet", repo_url, temp_dir
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Failed to clone {repo_url}: {result.stderr}")
            return "unknown"
        
        # Get commit hash
        commit_result = subprocess.run([
            "git", "rev-parse", "--short=7", "HEAD"
        ], cwd=temp_dir, capture_output=True, text=True)
        
        # Clean up
        shutil.rmtree(temp_dir)
        
        if commit_result.returncode == 0:
            return commit_result.stdout.strip()
        else:
            return "unknown"
            
    except Exception as e:
        print(f"Error fetching commit for {repo_url}: {e}")
        return "unknown"

def update_registry_versions(registry_file):
    """Update version fields in registry with latest commits"""
    
    # App repositories to update
    apps = {
        "tfgrid-ai-stack": "https://github.com/tfgrid-studio/tfgrid-ai-stack",
        "tfgrid-ai-agent": "https://github.com/tfgrid-studio/tfgrid-ai-agent", 
        "tfgrid-gitea": "https://github.com/tfgrid-studio/tfgrid-gitea"
    }
    
    # Create backup
    backup_file = f"{registry_file}.backup.{int(datetime.now().timestamp())}"
    shutil.copy2(registry_file, backup_file)
    print(f"📁 Created backup: {os.path.basename(backup_file)}")
    
    # Load registry
    with open(registry_file, 'r') as f:
        data = yaml.safe_load(f)
    
    updates_made = False
    
    # Update each app
    for app in data['apps']['official']:
        app_name = app['name']
        
        if app_name in apps:
            print(f"Processing {app_name}...")
            
            # Get latest commit
            latest_commit = get_latest_commit(apps[app_name])
            
            if latest_commit != "unknown":
                old_version = app.get('version', 'unknown')
                app['version'] = latest_commit
                print(f"✅ {app_name}: {old_version} → {latest_commit}")
                updates_made = True
            else:
                print(f"❌ Failed to fetch {app_name} commit")
    
    if updates_made:
        # Save updated registry
        with open(registry_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
        
        print(f"\n✅ Registry updated successfully!")
        return True
    else:
        print(f"\nℹ️ No updates were made")
        # Remove backup if no changes
        os.remove(backup_file)
        return False

def main():
    # Registry file path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    registry_file = os.path.join(script_dir, "..", "registry", "apps.yaml")
    
    if not os.path.exists(registry_file):
        print(f"❌ Registry file not found: {registry_file}")
        return 1
    
    print("🔄 TFGrid Studio Registry Version Updater")
    print("=" * 40)
    
    # Update versions
    updated = update_registry_versions(registry_file)
    
    if updated:
        print("\n📋 Next steps:")
        print("1. Review changes: git diff registry/apps.yaml")
        print("2. Test with: t update registry")
        print("3. Commit changes: git add && git commit")
    else:
        print("\n✅ All apps are already at latest versions!")
    
    return 0

if __name__ == "__main__":
    exit(main())