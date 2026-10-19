<div align="center">

# 🛡️ Cyber Sentry Arch

**Local vulnerability correlation for Arch Linux**

</div>

---

## The Problem

Reading a CVE headline and wondering:  
*“Does this actually affect my machine?”*

Most tools either:
- Show global noise, or
- Require complex infrastructure

## The Solution

**Cyber Sentry Arch** correlates live security intelligence against the packages **actually installed** on your system (`pacman -Q`).

### Data Sources

- Arch Linux Security Tracker
- CISA Known Exploited Vulnerabilities (KEV)
- (Extensible to NVD / EPSS)

## Current Status

This repository currently contains a solid foundation and architecture.  
The core scanning engine is being expanded.

## Quick Start

```bash
pip install requests
python cyber_sentry.py
```

## Roadmap

- [x] Package inventory
- [ ] Arch Security Tracker integration
- [ ] CISA KEV correlation
- [ ] Severity scoring
- [ ] Terminal + optional waybar module

## License

MIT
