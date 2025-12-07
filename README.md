# TFGrid Registry

Official registry of applications for TFGrid Compose - automatically validated and processed via CI/CD.

## Overview

This registry catalogs official and community applications that can be deployed using `tfgrid-compose`. Applications listed here are discoverable via `tfgrid-compose search` and can be deployed with a simple command:

```bash
tfgrid-compose up tfgrid-ai-agent
```

## Registry Structure

```
tfgrid-registry/
├── registry/
│   ├── apps.yaml              # Main official apps registry
│   └── verified/              # Verified community apps
│       └── community.yaml
├── schemas/
│   ├── app-manifest.json      # tfgrid-compose.yaml schema
│   └── registry.json          # Registry validation schema
├── docs/
│   ├── submit-app.md          # How to submit your app
│   ├── verification.md        # Verification process
│   └── app-guidelines.md      # App development guidelines
└── README.md                   # This file
```

## Quick Start

### Using Official Apps

```bash
# List all available apps
tfgrid-compose search

# Get app details
tfgrid-compose info tfgrid-ai-agent

# Deploy official app
tfgrid-compose up tfgrid-ai-agent
```

### Using Unverified Community Apps

```bash
# Deploy from any GitHub repo
tfgrid-compose up username/repo-name

# Deploy from any git URL
tfgrid-compose up https://gitlab.com/org/app
```

## App Categories

### Official Apps (tfgrid-studio)

Maintained by the TFGrid Studio team:
- **tfgrid-ai-agent** - AI coding agent with Qwen integration
- **tfgrid-gitea** - Self-hosted Git service with web interface

> **Note**: Patterns (single-vm, gateway, k3s) are built into tfgrid-compose, not listed here. This registry contains deployable APPLICATIONS that use those patterns.

### Community Apps

Community-contributed apps that have been reviewed and approved:
- Submit a PR to get your app listed!
- [See submission guidelines →](docs/submit-app.md)

## Submitting Your App

1. **Develop your app** following our [guidelines](docs/app-guidelines.md)
2. **Test thoroughly** with `tfgrid-compose up ./your-app`
3. **Submit PR** adding your app to `apps.community` in `registry/apps.yaml`
4. **Automated validation** - GitHub Actions validates your app
5. **Review process** - Team reviews code, security, documentation
6. **Approved!** - App appears in `tfgrid-compose search`

[Read full submission guide →](docs/submit-app.md)

## App Requirements

All apps must include:

- ✅ `tfgrid-compose.yaml` - App manifest
- ✅ `README.md` - Clear documentation
- ✅ Compatible pattern (single-vm, gateway, or k3s)
- ✅ No hardcoded secrets
- ✅ Open source license

[See detailed guidelines →](docs/app-guidelines.md)

## Registry Format

```yaml
apps:
  official:
    - name: tfgrid-ai-agent
      repo: github.com/tfgrid-studio/tfgrid-ai-agent
      description: AI coding agent with Qwen integration
      pattern: single-vm
      status: production
      maintainer: tfgrid-studio
      tags: [ai, coding, development]
      
  community:
    - name: my-app
      repo: github.com/username/my-app
      author: username
      maintainer: username
      submitted_date: 2025-10-14
      status: production
```

**Note:** App counts (total, official, community) are computed automatically by CI/CD - no manual maintenance needed!

## Automated Validation

**GitHub Actions** automatically:
- ✅ Validates YAML syntax
- ✅ Checks schema structure
- ✅ Validates all app entries
- ✅ Computes statistics dynamically
- ✅ Generates processed registry
- ✅ **Auto-updates app versions** with latest Git commits
- ✅ **Maintains version compatibility** with existing validation

[View workflows →](.github/workflows/)
- [Update Versions](.github/workflows/update-versions.yml) - Auto-updates version fields
- [Validate Registry](.github/workflows/validate-registry.yml) - Validates registry format

## Automated Version Management

**Version fields are automatically updated** when you push to this repository:

1. **Trigger**: Push changes to `main` branch
2. **Process**: Fetches latest commits from all app repositories:
   - `tfgrid-ai-stack`
   - `tfgrid-ai-agent`
   - `tfgrid-gitea`
3. **Update**: Sets `version` field to latest commit hash
4. **Validate**: Ensures all required fields exist
5. **Commit**: Saves changes back to repository (if versions changed)

**Format**:
```yaml
- name: tfgrid-ai-stack
  version: b21ad74           # Auto-updated commit hash
  versioning:
    primary: git_commit      # Git commit hash is primary version
```

This ensures `tfgrid-compose` always gets the latest versions while maintaining validation compatibility.

## Security

- **Official apps**: Audited and maintained by TFGrid Studio team
- **Community apps**: Code reviewed, tested, and security checked
- **External apps**: Use at your own risk - review code first

⚠️ Always review application code before deploying, especially for unverified apps.

## Contributing

We welcome contributions!

- 🐛 [Report issues](https://github.com/tfgrid-studio/tfgrid-registry/issues)
- 📝 [Submit apps](docs/submit-app.md)
- 💬 [Join discussions](https://github.com/tfgrid-studio/tfgrid-registry/discussions)

## Support

- **Documentation**: [docs.tfgrid.studio](https://docs.tfgrid.studio)
- **Issues**: [GitHub Issues](https://github.com/tfgrid-studio/tfgrid-registry/issues)
- **Community**: [Discussions](https://github.com/tfgrid-studio/tfgrid-registry/discussions)


Apache 2.0 License - See [LICENSE](LICENSE) for details.

Copyright 2025 ThreeFold

---

**Version**: 0.1.0  
**Last Updated**: 2025-10-15  
**Total Apps**: Computed dynamically via CI/CD  
**Maintained by**: [TFGrid Studio](https://github.com/tfgrid-studio)
