#!/usr/bin/env python3
"""
Security Tools Python - Bug Bounty Reconnaissance & Scanning Suite

A Python wrapper for common security tools (Subfinder, Nuclei) with:
- Scope validation to prevent unauthorized testing
- Automated logging of findings (JSON/Markdown)
- API endpoint fuzzing
- Subdomain enumeration

Author: Cell'ex
License: MIT
"""

import subprocess
import json
import requests
import time
import ipaddress
import os
from datetime import datetime
from typing import List, Dict, Any, Optional, Union

# --- Utility Functions ---

def _is_allowed_target(target: str, allowed_scope: Optional[List[str]]) -> bool:
    """
    Validate if target (domain, IP, or URL) is within allowed scope.
    
    Args:
        target: Domain, IP, or URL to check
        allowed_scope: List of allowed domains/networks (e.g., [".example.com", "192.168.1.0/24"])
    
    Returns:
        True if target is in scope, False otherwise
    """
    if not allowed_scope:
        return True
    
    hostname = target
    if target.startswith("http://") or target.startswith("https://"):
        try:
            from urllib.parse import urlparse
            parsed = urlparse(target)
            hostname = parsed.hostname or target
        except Exception:
            pass
    
    for scope in allowed_scope:
        scope = scope.strip()
        if not scope:
            continue
        try:
            # Check if it's an IP/CIDR notation
            if '/' in scope and (scope.count('.') == 3 or ':' in scope):
                network = ipaddress.ip_network(scope, strict=False)
                ip = ipaddress.ip_address(hostname)
                if ip in network:
                    return True
                continue
        except ValueError:
            pass
        
        # Domain matching
        if scope.startswith('.'):
            scope = scope[1:]
        if hostname == scope or hostname.endswith('.' + scope):
            return True
    
    return False

def log_finding(
    target_url: str, 
    payload: str, 
    response_snippet: str, 
    log_format: str = "json", 
    filename: str = "findings"
):
    """
    Log a security finding with timestamp, target, payload, and response snippet.
    
    Args:
        target_url: The URL that was tested
        payload: The payload or test used
        response_snippet: First 500 chars of response
        log_format: 'json' or 'md'
        filename: Output filename (without extension)
    """
    timestamp = datetime.now().isoformat()
    data = {
        "timestamp": timestamp,
        "target_url": target_url,
        "payload": payload,
        "response_snippet": response_snippet
    }

    if log_format.lower() == "json":
        log_file = f"{filename}.json"
        existing_data = []
        if os.path.exists(log_file):
            try:
                with open(log_file, "r") as f:
                    existing_data = json.load(f)
            except json.JSONDecodeError:
                pass
        
        existing_data.append(data)
        with open(log_file, "w") as f:
            json.dump(existing_data, f, indent=4)
            
    elif log_format.lower() == "md":
        log_file = f"{filename}.md"
        mode = "a" if os.path.exists(log_file) else "w"
        with open(log_file, mode) as f:
            if mode == "w":
                f.write("# Security Findings Log\n\n")
            f.write(f"### Finding - {timestamp}\n")
            f.write(f"- **Target:** `{target_url}`\n")
            f.write(f"- **Payload:** `{payload}`\n")
            f.write(f"- **Response Snippet:**\n```http\n{response_snippet}\n```\n")
            f.write("---\n\n")

# --- Security Tools ---

def run_recon(domain: str, allowed_scope: Optional[List[str]] = None) -> List[str]:
    """
    Run Subfinder to enumerate subdomains.
    
    Args:
        domain: Target domain (e.g., "example.com")
        allowed_scope: List of allowed domains
    
    Returns:
        List of discovered subdomains
    """
    if not _is_allowed_target(domain, allowed_scope):
        return [f"Error: Domain {domain} not in allowed scope"]
    
    try:
        cmd = ["subfinder", "-d", domain, "-silent"]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode != 0:
            return [f"Subfinder error: {result.stderr.strip()}"]
        
        return sorted(set(line.strip() for line in result.stdout.splitlines() if line.strip()))
    
    except subprocess.TimeoutExpired:
        return ["Error: Subfinder timed out (300s limit)"]
    except FileNotFoundError:
        return ["Error: subfinder not found. Install with: go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"]
    except Exception as e:
        return [f"Error: {str(e)}"]

def fuzz_api_endpoint(
    base_url: str, 
    wordlist: List[str] = None, 
    allowed_scope: Optional[List[str]] = None, 
    log_findings: bool = True
) -> List[Dict[str, Any]]:
    """
    Simple logic-fuzzing with optional logging of suspicious responses.
    
    Args:
        base_url: Base URL to fuzz (e.g., "https://api.example.com")
        wordlist: Custom wordlist for path discovery
        allowed_scope: List of allowed domains
        log_findings: Whether to log findings to files
    
    Returns:
        List of findings with URL, method, status, etc.
    """
    if not _is_allowed_target(base_url, allowed_scope):
        return [{"error": f"Base URL {base_url} not in allowed scope"}]
    
    if wordlist is None:
        wordlist = [
            "admin", "user", "test", "api", "v1", "v2", "debug", 
            "backup", "config", "login", "dashboard", "graphql",
            "swagger", "docs", "health", "status", "info"
        ]
    
    findings = []
    methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
    
    for method in methods:
        for word in wordlist:
            url = f"{base_url.rstrip('/')}/{word}"
            try:
                resp = requests.request(method, url, timeout=10)
                
                # Flag status codes that usually indicate exposed internal endpoints
                if resp.status_code in [200, 403, 500]:
                    snippet = resp.text[:500]
                    finding = {
                        "type": "path",
                        "method": method,
                        "url": url,
                        "status": resp.status_code,
                        "length": len(resp.text)
                    }
                    findings.append(finding)
                    
                    if log_findings:
                        log_finding(url, f"Method: {method}", snippet, log_format="md")
                        log_finding(url, f"Method: {method}", snippet, log_format="json", filename="fuzz_findings")

            except requests.RequestException:
                continue
            time.sleep(0.1)
    
    return findings

def run_nuclei_scan(
    target_url: str, 
    allowed_scope: Optional[List[str]] = None, 
    log_findings: bool = True
) -> Dict[str, Any]:
    """
    Run Nuclei vulnerability scanner and log results.
    
    Args:
        target_url: Target URL to scan
        allowed_scope: List of allowed domains
        log_findings: Whether to log findings to files
    
    Returns:
        Dictionary with findings count and list
    """
    if not _is_allowed_target(target_url, allowed_scope):
        return {"error": f"Target URL {target_url} not in allowed scope"}
    
    try:
        cmd = ["nuclei", "-u", target_url, "-json", "-silent", "-no-color"]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        
        findings = []
        for line in result.stdout.strip().splitlines():
            if line:
                try:
                    item = json.loads(line)
                    findings.append(item)
                    
                    if log_findings:
                        snippet = item.get("matched-at", "") + "\n" + str(item.get("info", {}).get("description", ""))
                        log_finding(
                            target_url, 
                            item.get("template-id", ""), 
                            snippet, 
                            log_format="md", 
                            filename="nuclei_findings"
                        )
                except json.JSONDecodeError:
                    continue
        
        return {
            "target": target_url,
            "findings_count": len(findings),
            "findings": findings
        }
    
    except subprocess.TimeoutExpired:
        return {"error": "Nuclei scan timed out (600s limit)"}
    except FileNotFoundError:
        return {"error": "nuclei not found. Install with: nuclei -update"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}

# --- Quick Usage Examples ---

if __name__ == "__main__":
    import sys
    
    print("=" * 60)
    print("Security Tools Python - Bug Bounty Reconnaissance Suite")
    print("=" * 60)
    print()
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 security_tools.py recon <domain> [scope...]")
        print("  python3 security_tools.py fuzz <base_url> [scope...]")
        print("  python3 security_tools.py nuclei <url> [scope...]")
        print()
        print("Example:")
        print('  python3 security_tools.py recon example.com --scope ".example.com"')
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "recon":
        domain = sys.argv[2]
        scope = sys.argv[3:] if len(sys.argv) > 3 else None
        print(f"[+] Running recon on {domain}")
        results = run_recon(domain, scope)
        for subdomain in results:
            print(subdomain)
    
    elif command == "fuzz":
        base_url = sys.argv[2]
        scope = sys.argv[3:] if len(sys.argv) > 3 else None
        print(f"[+] Fuzzing {base_url}")
        results = fuzz_api_endpoint(base_url, scope)
        print(f"[*] Found {len(results)} endpoints")
        for r in results:
            print(f"  [{r['status']}] {r['method']} {r['url']}")
    
    elif command == "nuclei":
        target = sys.argv[2]
        scope = sys.argv[3:] if len(sys.argv) > 3 else None
        print(f"[+] Running nuclei scan on {target}")
        results = run_nuclei_scan(target, scope)
        if "error" in results:
            print(f"[-] Error: {results['error']}")
        else:
            print(f"[*] Found {results['findings_count']} vulnerabilities")
    
    else:
        print(f"[-] Unknown command: {command}")
        sys.exit(1)
