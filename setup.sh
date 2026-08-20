#!/bin/bash
# Setup script for Security Tools Python

echo "🔧 Setting up Security Tools Python..."
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+"
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Check Go
if ! command -v go &> /dev/null; then
    echo "❌ Go not found. Please install Go first."
    echo "   Visit: https://go.dev/doc/install"
    exit 1
fi

# Install Subfinder
echo "🔍 Installing Subfinder..."
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Check subfinder
if command -v subfinder &> /dev/null; then
    echo "✓ Subfinder installed: $(subfinder -version)"
else
    echo "⚠ Subfinder may need PATH update"
    echo "  Run: export PATH=\$PATH:\$(go env GOPATH)/bin"
fi

# Install Nuclei
echo "☢️  Installing Nuclei..."
if ! command -v nuclei &> /dev/null; then
    go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
fi

# Check nuclei
if command -v nuclei &> /dev/null; then
    echo "✓ Nuclei installed: $(nuclei -version)"
else
    echo "⚠ Nuclei may need PATH update"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Usage examples:"
echo "  python3 security_tools.py recon example.com"
echo "  python3 security_tools.py fuzz https://api.example.com"
echo "  python3 security_tools.py nuclei https://example.com"
