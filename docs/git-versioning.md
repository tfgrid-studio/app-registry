# Git Commit-Based Versioning for TFGrid Registry

This document describes the enhanced versioning system using Git commit hashes as the primary version identifier for TFGrid Compose applications.

## Overview

Instead of manually managing semantic versions (v1.0.0, v1.1.2, etc.), TFGrid Compose now uses Git commit hashes as the primary version identifier. This provides:

- ✅ **Precise versioning**: Every deployment has a unique, immutable version
- ✅ **Automatic version management**: No manual version bumping required
- ✅ **Instant traceability**: Know exactly which code is running
- ✅ **Better debugging**: Can track exactly what changed between deployments
- ✅ **Consistency**: All TFGrid components use the same versioning approach

## Before vs After

### Traditional Semantic Versioning
```yaml
# Before: Manual version management
apps:
  official:
    - name: tfgrid-ai-stack
      version: "0.12.0-dev"  # Manual bumping required
      repo: github.com/tfgrid-studio/tfgrid-ai-stack
```

**Issues:**
- Requires manual version updates
- Doesn't reflect exact code state
- Version drift between code and registry
- No automatic update detection

### Git Commit-Based Versioning
```yaml
# After: Git commit as primary version
apps:
  official:
    - name: tfgrid-ai-stack
      repo: github.com/tfgrid-studio/tfgrid-ai-stack
      
      versioning:
        primary: git_commit      # Git commit hash is primary version
        fallback: semantic       # Semantic version as fallback
        auto_update: true        # Auto-update when new commits available
        
      git:
        default_branch: main
        tracking: true          # Track commit changes automatically
        auto_cache_refresh: true # Refresh cache when commits change
```

**Benefits:**
- Automatic version management
- Exact code traceability
- Smart cache management
- Consistent versioning across ecosystem

## Registry Structure

### Enhanced App Entry Format

Each app in the registry now includes:

```yaml
- name: tfgrid-ai-stack
  repo: github.com/tfgrid-studio/tfgrid-ai-stack
  description: "AI development environment"
  pattern: single-vm
  status: production
  maintainer: tfgrid-studio
  tags: [ai, development, coding]
  
  # NEW: Enhanced versioning configuration
  versioning:
    primary: git_commit      # Primary version source
    fallback: semantic       # Fallback version source
    auto_update: true        # Enable automatic updates
    
  # NEW: Git tracking metadata
  git:
    default_branch: main     # Branch to track
    tracking: true          # Enable commit tracking
    auto_cache_refresh: true # Auto-refresh cache on updates
```

### Metadata Section

The registry metadata indicates the versioning strategy:

```yaml
metadata:
  version: "2.0.0"  # Registry schema version
  last_updated: "2025-11-13"
  description: "Official registry with Git commit versioning"
  versioning_strategy: "git_commit"  # Indicates Git commit primary
```

## Version Display Examples

### Application Loading
```bash
# Shows Git commit as primary version
✅ Application loaded: tfgrid-ai-stack 24c9148
ℹ Manifest version: v0.12.0-dev
ℹ Last updated: 2025-11-11 22:47:49
ℹ Branch: main
ℹ Repository: https://github.com/tfgrid-studio/tfgrid-ai-stack.git
```

### Tool Version Display
```bash
# Shows Git commit as primary version for tfgrid-compose
TFGrid Compose cef6d4d
Semantic version: v0.14.0
```

### Cache Status
```bash
# Enhanced cache listing with commit information
✅ tfgrid-ai-stack (24c9148)
    Last updated: 2025-11-11 22:47:49
🔄 tfgrid-ai-agent (0e91178)
    Last updated: 2025-11-02 08:23:48
```

## Implementation Benefits

### 1. Automatic Version Management
- No need to manually update version numbers
- Git commit hash automatically reflects code state
- Version consistency between code and registry

### 2. Enhanced Debugging
```bash
# Exact version identification
Deployment: tfgrid-ai-stack 24c9148
Previous:   tfgrid-ai-stack 18f7a2c
Changes:    3 commits between versions
```

### 3. Smart Cache Management
- Cache invalidation based on Git commit changes
- Automatic detection of stale cached apps
- Clear version comparison in cache status

### 4. Improved User Experience
- More informative version display
- Better transparency about what's being deployed
- Clear indication of update availability

## Migration from Semantic Versions

### For App Developers
1. **Update app manifest**: Remove manual version bumping
2. **Configure Git tracking**: Add versioning section to registry entry
3. **Test deployment**: Verify Git commit appears as version
4. **Update documentation**: Reflect new versioning approach

### For tfgrid-compose
1. **Enhanced version detection**: Git commit extraction from cached apps
2. **Improved cache management**: Commit-based cache invalidation
3. **Better error reporting**: Include commit hashes in error messages
4. **Consistent display**: Git commit as primary version everywhere

## Future Enhancements

### Planned Features
- **Change tracking**: Show what changed between Git commits
- **Release detection**: Automatically detect version releases
- **Branch tracking**: Support for tracking specific branches
- **Rollback capability**: Easy rollback to previous commits

### Integration Points
- **CI/CD integration**: Automatic registry updates on commits
- **Community apps**: Same versioning for community submissions
- **Version comparison**: Smart comparison between versions
- **Update notifications**: Alert when new commits available

## Best Practices

### For App Maintainers
1. Use meaningful commit messages
2. Tag important releases in Git
3. Keep default branch up to date
4. Test deployments regularly

### For Registry Users
1. Check commit hashes for security
2. Review commit messages before deployment
3. Use specific commits for production when needed
4. Monitor update notifications

## Technical Implementation

### Git Commit Extraction
```bash
# Automatic Git commit detection
cd /path/to/cached/app
COMMIT_HASH=$(git rev-parse --short=7 HEAD)
BRANCH=$(git rev-parse --abbrev-ref HEAD)
COMMIT_DATE=$(git log -1 --format=%ct)
```

### Version Comparison
```bash
# Smart version comparison
if [ "$CACHED_COMMIT" != "$CURRENT_COMMIT" ]; then
    echo "Update available: $CACHED_COMMIT → $CURRENT_COMMIT"
fi
```

### Cache Invalidation
```bash
# Commit-based cache invalidation
cache_needs_update() {
    local cached_commit=$(get_cached_commit "$APP_NAME")
    local current_commit=$(get_current_commit "$APP_NAME")
    [ "$cached_commit" != "$current_commit" ]
}
```

This enhanced versioning system provides a more robust, transparent, and user-friendly approach to version management across the entire TFGrid ecosystem.