# GitHub Actions Workflows

## validate-registry.yml

Automatically validates and processes the app registry on every push and pull request.

### What It Does

1. **YAML Validation**
   - Checks syntax is valid
   - Ensures registry can be parsed

2. **Schema Validation**
   - Verifies required sections exist (`apps.official`, `apps.community`, `metadata`)
   - Checks structure is correct

3. **App Entry Validation**
   - Validates all app entries have required fields:
     - `name`, `repo`, `description`, `pattern`, `status`, `version`, `maintainer`
   - Ensures data integrity

4. **Statistics Computation**
   - Automatically counts apps dynamically:
     - `total_apps` = official + community
     - `official_apps` = count of official apps
     - `community_apps` = count of community apps
   - Displays stats in CI logs

5. **Processed Registry Generation** (main branch only)
   - Creates `apps.processed.yaml` with computed statistics
   - Adds computed metadata section
   - Uploads as artifact

### Benefits

- ✅ **No manual maintenance** - Stats computed automatically
- ✅ **Always accurate** - Counts can't get out of sync
- ✅ **PR validation** - Catches errors before merge
- ✅ **Professional** - Industry-standard CI/CD approach
- ✅ **Scalable** - Works for any number of apps

### Workflow Triggers

```yaml
on:
  push:
    branches: [main]
    paths: ['registry/**']
  pull_request:
    branches: [main]
    paths: ['registry/**']
```

Only runs when registry files are modified.

### Artifacts

On main branch pushes, generates:
- **processed-registry** - Contains `apps.processed.yaml` with computed metadata
- Retained for 30 days

### Usage Example

**When adding a new app:**

1. Edit `registry/apps.yaml`
2. Add your app to `apps.official` or `apps.community`
3. Commit and push (or open PR)
4. GitHub Actions automatically:
   - Validates your changes
   - Computes new statistics
   - Generates processed registry
   - Shows results in PR checks

**No need to update counts manually!**

### Viewing Statistics

Check the workflow logs to see:
```
═══════════════════════════════════
📦 Registry Statistics
═══════════════════════════════════
Total Apps:      2
Official Apps:   2
Community Apps:  0
═══════════════════════════════════

📋 Official Apps:
  • tfgrid-ai-agent (v0.9.0) - production
  • tfgrid-gitea (v1.0.0) - production
```

### Future Enhancements

Potential additions:
- JSON schema validation
- Link checking (verify GitHub repos exist)
- Automatic changelog generation
- Deployment to CDN
- Version conflict detection
- Notification on app updates
