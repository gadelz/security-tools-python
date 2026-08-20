# Security Tools Python - Panduan Pengguna Indonesia

## 📋 Ringkasan

Tool ini adalah wrapper Python untuk bug bounty reconnaissance yang mencakup:
- Enumerasi subdomain (Subfinder)
- Fuzzing API endpoint
- Scanning kerentanan (Nuclei)
- Validasi scope otomatis
- Logging temuan (JSON/Markdown)

## 🚀 Instalasi Cepat

### 1. Clone Repository
```bash
git clone https://github.com/cellex/security-tools-python.git
cd security-tools-python
```

### 2. Jalankan Setup
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Verifikasi Instalasi
```bash
# Test import Python
python3 -c "from security_tools import run_recon; print('✓ Import berhasil')"

# Test CLI
python3 security_tools.py recon example.com
```

## 📖 Cara Penggunaan

### Enumerasi Subdomain
```bash
python3 security_tools.py recon contoh.com --scope ".contoh.com"
```

### Fuzzing API Endpoint
```bash
python3 security_tools.py fuzz https://api.contoh.com --scope ".contoh.com"
```

### Vulnerability Scanning
```bash
python3 security_tools.py nuclei https://contoh.com --scope ".contoh.com"
```

### Penggunaan sebagai Library
```python
from security_tools import run_recon, fuzz_api_endpoint, run_nuclei_scan

# Enumerasi subdomain
subdomains = run_recon("contoh.com", allowed_scope=[".contoh.com"])
print(f"Ditemukan {len(subdomains)} subdomain")

# Fuzzing API
findings = fuzz_api_endpoint("https://api.contoh.com")
for f in findings:
    print(f"[{f['status']}] {f['method']} {f['url']}")
```

## 📊 Format Log

Temuan otomatis disimpan di:
- `findings.json` - Format JSON
- `findings.md` - Format Markdown

Contoh entri log:
```json
{
  "timestamp": "2026-08-20T10:30:00",
  "target_url": "https://example.com/admin",
  "payload": "Method: GET",
  "response_snippet": "<html>...</html>"
}
```

## 🐛 Troubleshooting

### Error: "subfinder: command not found"
```bash
export PATH=$PATH:$(go env GOPATH)/bin
```

### Error: "nuclei: command not found"
```bash
nuclei -update
```

### Error: "Permission denied" saat write log
```bash
chmod 644 findings.json
```

## ⚠️ Catatan Penting

1. **Hanya test domain yang diizinkan**
2. **Jangan disrupt layanan orang lain**
3. **Gunakan scope validation** untuk mencegah kesalahan
4. **Report via channel resmi** (email/web portal)

## 📄 Lisensi

MIT License - Bebas digunakan untuk tujuan edukasi dan bug bounty.
