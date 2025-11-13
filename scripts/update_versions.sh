#!/usr/bin/env bash
# TFGrid Studio Registry - Auto-update version fields
# This script updates the 'version' field in registry/apps.yaml 
# with the latest commit hash from each app repository

set -e

REGISTRY_FILE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/registry/apps.yaml"
BACKUP_FILE="${REGISTRY_FILE}.backup.$(date +%s)"

# Function to get latest commit hash from a repository
get_latest_commit() {
    local repo_url="$1"
    local temp_dir=$(mktemp -d)
    
    echo "Fetching latest commit for $repo_url..."
    
    # Clone and get commit hash
    if git clone --quiet "$repo_url" "$temp_dir" 2>/dev/null; then
        local commit_hash=$(cd "$temp_dir" && git rev-parse --short=7 HEAD 2>/dev/null)
        cd "$temp_dir" && rm -rf "$temp_dir"
        echo "$commit_hash"
    else
        echo "unknown"
        rm -rf "$temp_dir"
    fi
}

# Function to update version field for an app
update_app_version() {
    local app_name="$1"
    local commit_hash="$2"
    
    echo "Updating $app_name to version: $commit_hash"
    
    # Use a simpler sed approach that doesn't have escaping issues
    sed -i.tmp "s/version: b21ad74/version: $commit_hash/" "$REGISTRY_FILE"
}

echo "🔄 TFGrid Studio Registry Version Updater"
echo "========================================"

# Create backup
echo "📁 Creating backup: $(basename "$BACKUP_FILE")"
cp "$REGISTRY_FILE" "$BACKUP_FILE"

# Update each official app
echo ""
echo "📦 Updating official apps..."

# tfgrid-ai-stack
echo "Processing tfgrid-ai-stack..."
commit=$(get_latest_commit "https://github.com/tfgrid-studio/tfgrid-ai-stack")
if [ "$commit" != "unknown" ]; then
    update_app_version "tfgrid-ai-stack" "$commit"
    echo "✅ tfgrid-ai-stack updated to $commit"
else
    echo "❌ Failed to fetch tfgrid-ai-stack commit"
fi

# tfgrid-ai-agent
echo "Processing tfgrid-ai-agent..."
commit=$(get_latest_commit "https://github.com/tfgrid-studio/tfgrid-ai-agent")
if [ "$commit" != "unknown" ]; then
    update_app_version "tfgrid-ai-agent" "$commit"
    echo "✅ tfgrid-ai-agent updated to $commit"
else
    echo "❌ Failed to fetch tfgrid-ai-agent commit"
fi

# tfgrid-gitea
echo "Processing tfgrid-gitea..."
commit=$(get_latest_commit "https://github.com/tfgrid-studio/tfgrid-gitea")
if [ "$commit" != "unknown" ]; then
    update_app_version "tfgrid-gitea" "$commit"
    echo "✅ tfgrid-gitea updated to $commit"
else
    echo "❌ Failed to fetch tfgrid-gitea commit"
fi

echo ""
echo "🧹 Cleaning up temporary files..."
rm -f "${REGISTRY_FILE}.tmp"

echo ""
echo "✅ Version update complete!"
echo "📁 Backup saved to: $(basename "$BACKUP_FILE")"
echo ""
echo "Next steps:"
echo "1. Review changes: git diff $REGISTRY_FILE"
echo "2. Test with: t update registry"
echo "3. Commit changes: git add && git commit"