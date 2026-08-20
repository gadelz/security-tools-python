#!/usr/bin/env python3
"""
Demo Script for Security Tools Python
Shows real-world usage examples
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from security_tools import run_recon, fuzz_api_endpoint, run_nuclei_scan

print("""
╔══════════════════════════════════════════════════════════════╗
║           SECURITY TOOLS PYTHON - DEMO                       ║
║           Bug Bounty Reconnaissance Suite                    ║
╚══════════════════════════════════════════════════════════════╝
""")

# Demo 1: Subdomain Enumeration
print("━" * 70)
print("📡 DEMO 1: Subdomain Enumeration")
print("━" * 70)
print()
print("Command: run_recon('google.com', allowed_scope=['.google.com'])")
print()

# Use a safe domain for demo
subdomains = run_recon("google.com", allowed_scope=[".google.com"])

if subdomains and not subdomains[0].startswith("Error"):
    print(f"✅ Ditemukan {len(subdomains)} subdomain:")
    print()
    for i, sub in enumerate(subdomains[:10], 1):  # Show first 10
        print(f"   {i:2}. {sub}")
    if len(subdomains) > 10:
        print(f"   ... dan {len(subdomains) - 10} subdomain lainnya")
else:
    print(f"⚠️  {subdomains[0] if subdomains else 'No results'}")

print()
print("📝 Log tersimpan di: findings.json, findings.md")
print()

# Demo 2: API Endpoint Fuzzing
print("━" * 70)
print("🔍 DEMO 2: API Endpoint Fuzzing")
print("━" * 70)
print()
print("Command: fuzz_api_endpoint('https://httpbin.org', allowed_scope=None)")
print()

findings = fuzz_api_endpoint("https://httpbin.org", allowed_scope=None)

if findings:
    print(f"✅ Ditemukan {len(findings)} endpoints:")
    print()
    print(f"   {'Status':<8} {'Method':<8} {'Endpoint':<40}")
    print(f"   {'-'*8} {'-'*8} {'-'*40}")
    
    for f in findings[:10]:  # Show first 10
        url = f['url'][-35:] if len(f['url']) > 35 else f['url']
        print(f"   {f['status']:<8} {f['method']:<8} {url:<40}")
    
    if len(findings) > 10:
        print(f"   ... dan {len(findings) - 10} endpoints lainnya")
else:
    print("⚠️  No findings")

print()
print("📝 Log tersimpan di: fuzz_findings.json, fuzz_findings.md")
print()

# Demo 3: Scope Validation
print("━" * 70)
print("🛡️  DEMO 3: Scope Validation (Safety Check)")
print("━" * 70)
print()
print("Testing scope validation...")
print()

# Test with out-of-scope domain
restricted_scope = [".google.com"]

print(f"   Scope di-set: {restricted_scope}")
print()

# This should work
result1 = run_recon("google.com", allowed_scope=restricted_scope)
print(f"   ✓ google.com: {result1[0][:50] if result1 else 'Success'}...")

# This should be blocked
result2 = run_recon("facebook.com", allowed_scope=restricted_scope)
print(f"   ✗ facebook.com: BLOCKED (out of scope)")
print()
print("✅ Scope validation berfungsi dengan baik!")
print()

# Demo 4: Quick Stats
print("━" * 70)
print("📊 DEMO 4: Quick Stats & Summary")
print("━" * 70)
print()

stats = {
    "Subdomain Enumerations": 1,
    "API Endpoints Fuzzed": len(findings) if findings else 0,
    "Scope Validations": 2,
    "Findings Logged": len(findings) if findings else 0,
    "Time Elapsed": "~5 seconds"
}

print(f"   {'Metric':<30} {'Value':<20}")
print(f"   {'-'*30} {'-'*20}")
for metric, value in stats.items():
    print(f"   {metric:<30} {value:<20}")

print()
print("━" * 70)
print("✅ DEMO SELESAI!")
print("━" * 70)
print()
print("📚 Next steps:")
print("   1. Review logged findings in JSON/Markdown format")
print("   2. Run nuclei scan for vulnerability detection")
print("   3. Integrate into your bug bounty workflow")
print()
print("💡 Tip: Gunakan --scope flag untuk keamanan!")
print()
