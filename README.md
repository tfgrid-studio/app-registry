# TFGrid App Registry

Official registry of verified applications for TFGrid Compose.

## Overview

This registry catalogs official and verified community applications that can be deployed using `tfgrid-compose`. Applications listed here are discoverable via `tfgrid-compose search` and can be deployed with a simple command:

```bash
tfgrid-compose up tfgrid-ai-agent
```

## Registry Structure

```
app-registry/
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

> **Note**: Patterns (single-vm, gateway, k3s) are built into tfgrid-compose, not listed here. This registry contains deployable APPLICATIONS that use those patterns.

### Verified Community Apps

Community-contributed apps that have passed verification:
- Submit a PR to get your app verified!
- [See submission guidelines →](docs/submit-app.md)

## Submitting Your App

1. **Develop your app** following our [guidelines](docs/app-guidelines.md)
2. **Test thoroughly** with `tfgrid-compose up ./your-app`
3. **Submit PR** adding your app to `registry/verified/community.yaml`
4. **Review process** - Team reviews code, security, documentation
5. **Verified!** - App appears in `tfgrid-compose search`

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
      verified: true
      tags: [ai, coding, development]
      
  verified:
    - name: my-app
      repo: github.com/username/my-app
      author: username
      verified: true
      verified_date: 2025-10-14
      status: production
```

## Security

- **Official apps**: Audited by TFGrid Studio team
- **Verified apps**: Code reviewed, tested, security checked
- **Unverified apps**: Use at your own risk - review code first

⚠️ Always review application code before deploying, especially for unverified apps.

## Contributing

We welcome contributions!

- 🐛 [Report issues](https://github.com/tfgrid-studio/app-registry/issues)
- 📝 [Submit apps](docs/submit-app.md)
- 💬 [Join discussions](https://github.com/tfgrid-studio/app-registry/discussions)

## Support

- **Documentation**: [docs.tfgrid.studio](https://docs.tfgrid.studio)
- **Issues**: [GitHub Issues](https://github.com/tfgrid-studio/app-registry/issues)
- **Community**: [Discussions](https://github.com/tfgrid-studio/app-registry/discussions)

## License

Apache 2.0 License - See [LICENSE](LICENSE) for details.

Copyright 2025 ThreeFold

---

**Version**: 0.1.0  
**Last Updated**: 2025-10-14  
**Maintained by**: [TFGrid Studio](https://github.com/tfgrid-studio)
