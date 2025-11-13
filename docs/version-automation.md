# TFGrid Studio Registry - Automated Version Management

## Overview

This repository uses **fully automated version management** for the TFGrid Studio app registry. When you push changes to this repository, it automatically updates version fields and validates the registry.

## How It Works

### 🚀 Automatic Version Updates

**Trigger**: Push to `main` branch with changes to:
- `registry/apps.yaml`
- `scripts/update_versions.sh`

**Process**:
1. GitHub Action runs `scripts/update_versions.sh`
2. Script fetches latest commits from all app repositories:
   - `tfgrid-ai-stack`
   - `tfgrid-ai-agent` 
   - `tfgrid-gitea`
3. Updates `version` field in `registry/apps.yaml` with latest commit hash
4. Commits changes back to repository (if any updates occurred)
5. Validates all apps have required `version` field

### 🔍 Validation Process

The workflow validates that each app has:
- ✅ `version` field (for compatibility with existing validation)
- ✅ `repo` field (repository URL)
- ✅ `versioning.primary` field (Git commit-based tracking)

### 📁 Updated Registry Format

```yaml
apps:
  official:
    - name: tfgrid-ai-stack
      version: b21ad74           # Auto-updated commit hash
      versioning:
        primary: git_commit      # Git commit hash is primary version
        fallback: semantic
```

## Usage

### For TFGrid Studio Maintainers

**Just push your changes!** The automation handles everything:

```bash
# Make your changes to registry/apps.yaml or scripts/
git add .
git commit -m "Update app registry configuration"
git push origin main

# GitHub Action will automatically:
# 1. Update version fields with latest commits
# 2. Validate all entries
# 3. Commit changes if versions were updated
```

### Manual Testing (Optional)

If you want to test locally:

```bash
# Run the update script manually
./scripts/update_versions.sh

# Check what changed
git diff registry/apps.yaml

# Revert if needed
git checkout registry/apps.yaml
```

## Benefits

✅ **Zero Manual Work**: Version updates happen automatically  
✅ **Always Current**: Uses latest commits from all app repositories  
✅ **Validation**: Ensures registry entries are always valid  
✅ **Traceability**: Full git history of all changes  
✅ **Reliable**: GitHub Actions provides robust automation  

## Troubleshooting

### Workflow Fails
- Check repository permissions (GITHUB_TOKEN)
- Ensure `scripts/update_versions.sh` is executable
- Verify app repositories are accessible

### Version Not Updated
- Check if app repository has new commits
- Verify `update_versions.sh` script is running successfully
- Review workflow logs for specific errors

### Validation Errors
- Ensure `version` field exists for each app
- Verify `versioning.primary: git_commit` is set
- Check all required fields are present

## Integration with tfgrid-compose

This automation ensures that when users run:
```bash
t update registry
t up tfgrid-ai-stack
```

They always get the latest version of each app with proper validation.