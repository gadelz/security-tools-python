#!/bin/bash
# Quick Demo Recording Script
# Use this to record your demo video

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║         SECURITY TOOLS PYTHON - DEMO RECORDING             ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "🎬 Demo akan dijalankan dalam 2 detik..."
sleep 2

clear

echo "📹 RECORDING START: $(date)"
echo ""

# Run the fast demo
python3 demo_fast.py

echo ""
echo "📹 RECORDING END: $(date)"
echo ""

# Save recording info
cat > recording_info.txt << 'EOF'
============================================================
DEMO RECORDING INFORMATION
============================================================

Date: $(date)
Duration: ~30 seconds
Features Shown:
  1. Library Structure
  2. Subdomain Enumeration (Mock)
  3. API Endpoint Fuzzing (Mock)
  4. Scope Validation
  5. Auto Logging
  6. CLI Commands
  7. Features Summary

Total Lines of Code: 320
Documentation: README.md, README_ID.md
License: MIT

============================================================
EOF

echo "✅ Demo recording complete!"
echo "📁 Info saved to: recording_info.txt"
echo ""
echo "💡 Tip: Use OBS Studio or ScreenRec to record this output"
echo ""
