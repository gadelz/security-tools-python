# Security Tools Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Bug Bounty](https://img.shields.io/badge/Bug%20Bounty-Ready-orange.svg)](https://example.com)

Python wrapper for bug bounty reconnaissance and scanning tools with built-in scope validation and automated finding logging.

## 🎯 Features

- **Subdomain Enumeration** - Wrapper for Subfinder with scope validation
- **API Endpoint Fuzzing** - Smart fuzzing with automatic logging
- **Vulnerability Scanning** - Nuclei integration with JSON output
- **Scope Validation** - Prevents unauthorized testing
- **Automated Logging** - JSON and Markdown export of findings
- **CLI Interface** - Easy command-line usage

## 📦 Installation

### Prerequisites

- Python 3.8+
- Go (for Subfinder)
- Nuclei (for scanning)

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Install Subfinder

```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

Verify installation:
```bash
subfinder -h
```

### Step 3: Install Nuclei

```bash
nuclei -update
```

Verify installation:
```bash
nuclei -version
```

### Step 4: Clone and Use

```bash
git clone https://github.com/cellex/security-tools-python.git
cd security-tools-python
python3 security_tools.py --help
```

## 🚀 Quick Start

### Basic Usage

```python
from security_tools import run_recon, fuzz_api_endpoint, run_nuclei_scan

# Enumerate subdomains
subdomains = run_recon("example.com", allowed_scope=[".example.com"])
print(f"Found {len(subdomains)} subdomains")

# Fuzz API endpoints
findings = fuzz_api_endpoint("https://api.example.com", allowed_scope=[".example.com"])
for f in findings:
    print(f"[{f['status']}] {f['method']} {f['url']}")

# Run nuclei scan
results = run_nuclei_scan("https://target.com", allowed_scope=[".target.com"])
print(f"Found {results['findings_count']} vulnerabilities")
```

### CLI Usage

```bash
# Reconnaissance
python3 security_tools.py recon example.com --scope ".example.com"

# API Fuzzing
python3 security_tools.py fuzz https://api.example.com --scope ".example.com"

# Vulnerability Scanning
python3 security_tools.py nuclei https://example.com --scope ".example.com"
```

## 📊 Logging

Findings are automatically logged to:

- `findings.json` - JSON format for programmatic analysis
- `findings.md` - Markdown format for human-readable reports
- `fuzz_findings.json` - API fuzzing results
- `nuclei_findings.json` - Nuclei scan results

Each log entry includes:
- Timestamp
- Target URL
- Payload/Test used
- Response snippet (first 500 characters)

## 🛡️ Scope Validation

The tool includes built-in scope validation to prevent unauthorized testing:

```python
# Allowed scope formats
allowed_scope = [
    ".example.com",           # Domain and subdomains
    "example.com",            # Exact domain match
    "192.168.1.0/24",        # CIDR notation
    "api.example.com"        # Specific subdomain
]

# Validation happens automatically
subdomains = run_recon("example.com", allowed_scope=allowed_scope)
```

## 🔧 Configuration

### Custom Wordlist for Fuzzing

```python
custom_wordlist = ["admin", "user", "api", "v1", "v2", "debug", "config"]
findings = fuzz_api_endpoint("https://api.example.com", wordlist=custom_wordlist)
```

### Disable Logging

```python
findings = fuzz_api_endpoint("https://api.example.com", log_findings=False)
```

## 📋 Report Template

For bug bounty submissions, use the Gerobug format:

```
TYPE= Information Disclosure / Security Misconfiguration
ENDPOINT= https://vulnerable-site.com/
SUMMARY= Description of findings

See attached PDF report for full details.
```

## 🐛 Troubleshooting

### Issue: "subfinder: command not found"

**Solution:** Install Subfinder using Go:
```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
export PATH=$PATH:$(go env GOPATH)/bin
```

### Issue: "nuclei: command not found"

**Solution:** Install/update Nuclei:
```bash
nuclei -update
```

### Issue: "ModuleNotFoundError: No module named 'requests'"

**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: "Permission denied" when writing logs

**Solution:** Check file permissions:
```bash
ls -la findings.json
chmod 644 findings.json
```

### Issue: "TimeoutExpired" errors

**Solution:** Increase timeout in the script:
```python
# In security_tools.py, change timeout values
result = subprocess.run(cmd, timeout=600)  # Increase from 300 to 600
```

### Issue: Scope validation blocking legitimate targets

**Solution:** Verify your scope format:
```python
# Correct formats
allowed_scope = [".example.com", "example.com", "192.168.1.0/24"]

# Incorrect - will not match
allowed_scope = ["example.com"]  # Won't match subdomains
```

## 📚 API Reference

### `run_recon(domain, allowed_scope=None)`

Enumerate subdomains using Subfinder.

**Parameters:**
- `domain` (str): Target domain
- `allowed_scope` (list): List of allowed domains/networks

**Returns:** List of subdomains

### `fuzz_api_endpoint(base_url, wordlist=None, allowed_scope=None, log_findings=True)`

Fuzz API endpoints and discover paths.

**Parameters:**
- `base_url` (str): Base URL to fuzz
- `wordlist` (list): Custom wordlist
- `allowed_scope` (list): Scope validation
- `log_findings` (bool): Enable logging

**Returns:** List of findings with status codes

### `run_nuclei_scan(target_url, allowed_scope=None, log_findings=True)`

Run Nuclei vulnerability scanner.

**Parameters:**
- `target_url` (str): Target URL to scan
- `allowed_scope` (list): Scope validation
- `log_findings` (bool): Enable logging

**Returns:** Dictionary with findings count and list

## 🔒 Security & Ethics

- Always obtain proper authorization before testing
- Respect scope boundaries
- Do not disrupt legitimate services
- Follow responsible disclosure practices
- Never access or modify user data without permission

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

## 👤 Author

**Cell'ex**
- GitHub: [@cellex](https://github.com/cellex)
- Portfolio: [Personal Website](https://example.com)

## 🙏 Acknowledgments

- [ProjectDiscovery](https://projectdiscovery.io) - Subfinder & Nuclei
- [Gerobug](https://gerobug.gerosecurity.com) - Bug Bounty Platform
- All bug bounty programs for responsible disclosure

## 📝 Changelog

### v1.0.0 (2026-08-20)
- Initial release
- Subdomain enumeration with Subfinder
- API endpoint fuzzing
- Nuclei integration
- Scope validation
- Automated logging (JSON/Markdown)
- CLI interface

---

**Happy Hunting! 🎯**
