# Submitting Your App to TFGrid Registry

This guide explains how to submit your application to the TFGrid App Registry for verification and inclusion.

## Overview

Getting your app verified means:
- ✅ Discoverable via `tfgrid-compose search`
- ✅ Listed in official registry
- ✅ Verified badge
- ✅ Increased visibility and trust

## Prerequisites

Before submitting:

1. **Working App**: Your app deploys successfully with `tfgrid-compose up ./your-app`
2. **Documentation**: Clear README with setup instructions
3. **App Manifest**: Valid `tfgrid-compose.yaml`
4. **Open Source**: Public repository with open source license
5. **No Secrets**: No hardcoded credentials or API keys

## Submission Process

### Step 1: Prepare Your App

Ensure your repository has:

```
your-app/
├── tfgrid-compose.yaml       # Required: App manifest
├── README.md                  # Required: Documentation
├── LICENSE                    # Required: Open source license
├── .gitignore                # Recommended: Ignore secrets
└── (app-specific files)
```

**Minimum `tfgrid-compose.yaml`:**
```yaml
name: your-app
version: 0.1.0
description: Brief description of your app

patterns:
  recommended: single-vm  # or gateway, k3s
  
config:
  # Your app configuration
```

### Step 2: Test Thoroughly

```bash
# Test local deployment
tfgrid-compose up ./your-app

# Verify all functionality
tfgrid-compose status
tfgrid-compose ssh

# Clean up
tfgrid-compose down
```

### Step 3: Fork Registry Repository

```bash
git clone https://github.com/YOUR-USERNAME/tfgrid-registry
cd tfgrid-registry
git checkout -b add-your-app
```

### Step 4: Add Your App Entry

Edit `registry/verified/community.yaml` (create if doesn't exist):

```yaml
apps:
  verified:
    - name: your-app-name
      repo: github.com/your-username/your-app-repo
      author: your-username
      description: Clear one-line description of your app
      pattern: single-vm  # or gateway, k3s
      status: beta  # beta or production
      version: v0.1.0
      verified: false  # Will be set to true after review
      verified_date: null  # Will be set by team
      tags:
        - tag1
        - tag2
        - tag3
      requirements:
        cpu: 2
        memory: 4GB
        disk: 50GB
      links:
        docs: https://github.com/your-username/your-app-repo
        repo: https://github.com/your-username/your-app-repo
        demo: https://example.com  # optional
```

### Step 5: Create Pull Request

```bash
git add registry/verified/community.yaml
git commit -m "feat: add YOUR-APP to verified apps"
git push origin add-your-app
```

Create PR on GitHub with:
- **Title**: `Add [Your App Name] to verified apps`
- **Description**: 
  - What does your app do?
  - Why should users try it?
  - Any special requirements or notes?

## Review Process

Our team will:

1. **Code Review** (1-3 days)
   - Review repository structure
   - Check for security issues
   - Verify no hardcoded secrets
   - Validate app manifest

2. **Testing** (1-2 days)
   - Deploy app on test environment
   - Verify all features work
   - Check resource requirements
   - Test cleanup process

3. **Documentation Review** (1 day)
   - README clarity
   - Setup instructions
   - Prerequisites listed
   - Troubleshooting info

4. **Approval or Feedback**
   - If approved: Merged, `verified: true` set
   - If changes needed: Comments on PR

**Total Timeline**: ~5-7 days

## Verification Criteria

### Must Have ✅

- [ ] Valid `tfgrid-compose.yaml`
- [ ] Clear README with setup instructions
- [ ] Open source license (Apache 2.0 recommended)
- [ ] No hardcoded secrets or credentials
- [ ] Deploys successfully
- [ ] Cleans up properly with `tfgrid-compose down`
- [ ] Works with current tfgrid-compose version

### Should Have 📋

- [ ] Comprehensive documentation
- [ ] Example configurations
- [ ] Troubleshooting guide
- [ ] Security best practices documented
- [ ] Resource requirements documented
- [ ] Regular maintenance commitment

### Nice to Have 🌟

- [ ] Automated tests
- [ ] CI/CD pipeline
- [ ] Multiple pattern support
- [ ] Configuration examples
- [ ] Video tutorial or demo

## After Verification

Once approved:

1. **Merged to Registry**: Your app appears in `registry/verified/community.yaml`
2. **Discoverable**: Users can find it via `tfgrid-compose search`
3. **Verified Badge**: Shows as verified in listings
4. **Responsibility**: Maintain app, respond to issues, keep updated

## Maintaining Your App

### Updates

When you update your app:
1. Update version in your repo's `tfgrid-compose.yaml`
2. Create PR to update version in registry
3. Include changelog in PR description

### Support

- Respond to user issues in your repo
- Keep documentation updated
- Fix bugs promptly
- Announce breaking changes

### Revocation

Verification may be revoked if:
- App becomes unmaintained
- Security vulnerabilities not fixed
- Breaking changes without migration guide
- Violates community guidelines

## Examples

See official apps for reference:
- [tfgrid-ai-agent](https://github.com/tfgrid-studio/tfgrid-ai-agent)
- [tfgrid-gateway](https://github.com/tfgrid-studio/tfgrid-gateway)
- [tfgrid-k3s](https://github.com/tfgrid-studio/tfgrid-k3s)

## Need Help?

- **Questions**: [Open a discussion](https://github.com/tfgrid-studio/tfgrid-registry/discussions)
- **Issues**: [Report problems](https://github.com/tfgrid-studio/tfgrid-registry/issues)
- **Guidelines**: See [app-guidelines.md](app-guidelines.md)

---

**Thank you for contributing to the TFGrid ecosystem!** 🎉
