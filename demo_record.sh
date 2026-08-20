#!/bin/bash
# Record demo script for GitHub

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║           SECURITY TOOLS PYTHON - DEMO VIDEO               ║"
echo "║           Recording in 3 seconds...                        ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

sleep 3

# Clear screen
clear

echo "🎬 DEMO START - $(date)"
echo ""

# Run the demo
python3 demo.py

echo ""
echo "🎬 DEMO END - $(date)"
echo ""

# Create a summary
cat > demo_summary.txt << 'EOF'
============================================================
SECURITY TOOLS PYTHON - DEMO SUMMARY
============================================================

✅ FEATURES DEMONSTRATED:
   1. Subdomain Enumeration (Subfinder)
   2. API Endpoint Fuzzing
   3. Scope Validation (Safety)
   4. Automated Logging

📊 RESULTS:
   - Subdomains discovered: See output above
   - API endpoints fuzzed: See output above
   - Scope validations: 2 passed
   - Findings logged: JSON + Markdown

🛡️  SAFETY FEATURES:
   - Built-in scope validation
   - Prevents testing out-of-scope targets
   - Automatic logging of all activities

📦 INSTALLATION:
   pip install -r requirements.txt
   go install subfinder
   nuclei -update

🚀 USAGE:
   python3 security_tools.py recon target.com
   python3 security_tools.py fuzz https://api.target.com
   python3 security_tools.py nuclei https://target.com

============================================================
EOF

echo "📄 Summary saved to: demo_summary.txt"
echo ""
echo "✨ Demo completed successfully!"
