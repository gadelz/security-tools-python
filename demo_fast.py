#!/usr/bin/env python3
"""
Fast Demo Script - Shows functionality without long waits
Uses mock data for demonstration
"""

import sys
import os
import json
from datetime import datetime

print("""
╔══════════════════════════════════════════════════════════════╗
║     SECURITY TOOLS PYTHON - QUICK DEMO (MOCK MODE)         ║
║                                                              ║
║  ⚡ Fast demonstration with sample data                      ║
╚══════════════════════════════════════════════════════════════╝
""")

# Demo 1: Show code structure
print("━" * 70)
print("📦 1. LIBRARY STRUCTURE")
print("━" * 70)
print()
print("""
   from security_tools import (
       run_recon,          # Subdomain enumeration
       fuzz_api_endpoint,  # API fuzzing
       run_nuclei_scan,    # Vulnerability scanning
       log_finding         # Finding logger
   )
""")

# Demo 2: Mock subdomain results
print("━" * 70)
print("📡 2. SUBDOMAIN ENUMERATION (Mock Results)")
print("━" * 70)
print()
print("   Target: example.com (demo)")
print()

mock_subdomains = [
    "www.example.com",
    "api.example.com",
    "mail.example.com",
    "vpn.example.com",
    "dev.example.com",
    "admin.example.com",
    "staging.example.com",
    "test.example.com",
    "cdn.example.com",
    "blog.example.com"
]

print(f"   ✅ Ditemukan {len(mock_subdomains)} subdomain:")
print()
for i, sub in enumerate(mock_subdomains, 1):
    print(f"      {i:2}. {sub}")

print()

# Demo 3: Mock fuzzing results
print("━" * 70)
print("🔍 3. API FUZZING (Mock Results)")
print("━" * 70)
print()
print("   Target: https://api.example.com")
print()

mock_findings = [
    {"status": 200, "method": "GET", "url": "/api/v1/users"},
    {"status": 403, "method": "GET", "url": "/admin"},
    {"status": 200, "method": "GET", "url": "/api/v2/data"},
    {"status": 500, "method": "POST", "url": "/api/debug"},
    {"status": 200, "method": "GET", "url": "/swagger.json"},
    {"status": 403, "method": "GET", "url": "/backup"},
]

print(f"   ✅ Ditemukan {len(mock_findings)} endpoints:")
print()
print(f"      {'Status':<8} {'Method':<8} {'Path':<30}")
print(f"      {'-'*8} {'-'*8} {'-'*30}")
for f in mock_findings:
    print(f"      {f['status']:<8} {f['method']:<8} {f['url']:<30}")

print()

# Demo 4: Scope validation
print("━" * 70)
print("🛡️  4. SCOPE VALIDATION")
print("━" * 70)
print()
print("   Allowed scope: ['.example.com']")
print()
print("   ✓ example.com    → ALLOWED")
print("   ✓ api.example.com → ALLOWED")
print("   ✗ facebook.com   → BLOCKED (out of scope)")
print("   ✗ google.com     → BLOCKED (out of scope)")
print()
print("   ✅ Scope validation mencegah pengujian tanpa otorisasi!")
print()

# Demo 5: Logging output
print("━" * 70)
print("📝 5. AUTO LOGGING (JSON Format)")
print("━" * 70)
print()

sample_log = {
    "timestamp": datetime.now().isoformat(),
    "target_url": "https://api.example.com/admin",
    "payload": "Method: GET",
    "response_snippet": "<html><body>403 Forbidden</body></html>"
}

print("   Sample log entry:")
print()
print("   " + json.dumps(sample_log, indent=2).replace("\n", "\n   "))
print()
print("   📂 Files created:")
print("      • findings.json")
print("      • findings.md")
print("      • fuzz_findings.json")
print()

# Demo 6: CLI usage
print("━" * 70)
print("⚡ 6. CLI COMMANDS")
print("━" * 70)
print()
print("   # Enumerasi subdomain")
print('   $ python3 security_tools.py recon example.com')
print()
print("   # Fuzzing API endpoint")
print('   $ python3 security_tools.py fuzz https://api.example.com')
print()
print("   # Vulnerability scanning")
print('   $ python3 security_tools.py nuclei https://example.com')
print()
print("   # Dengan scope validation")
print('   $ python3 security_tools.py recon example.com --scope ".example.com"')
print()

# Demo 7: Features summary
print("━" * 70)
print("✨ 7. FEATURES SUMMARY")
print("━" * 70)
print()

features = [
    ("Subdomain Enumeration", "✅", "Subfinder integration"),
    ("API Endpoint Fuzzing", "✅", "Smart wordlist + methods"),
    ("Vulnerability Scanning", "✅", "Nuclei templates"),
    ("Scope Validation", "✅", "Prevent unauthorized testing"),
    ("Auto Logging", "✅", "JSON + Markdown export"),
    ("CLI Interface", "✅", "Easy command-line usage"),
    ("Error Handling", "✅", "Graceful failure handling"),
    ("Timeout Control", "✅", "Configurable timeouts"),
]

print(f"   {'Feature':<25} {'Status':<10} {'Description'}")
print(f"   {'-'*25} {'-'*10} {'-'*30}")
for feature, status, desc in features:
    print(f"   {feature:<25} {status:<10} {desc}")

print()
print("━" * 70)
print("✅ DEMO SELESAI!")
print("━" * 70)
print()
print("📚 Next steps:")
print("   1. git clone https://github.com/CELL-EX/security-tools-python.git")
print("   2. pip install -r requirements.txt")
print("   3. go install subfinder && nuclei -update")
print("   4. python3 security_tools.py --help")
print()
print("💡 Happy Bug Hunting! 🎯")
print()
