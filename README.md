Security Tools Python
�
�
�
Load image
Load image
Load image
Python wrapper untuk reconnaissance dan scanning bug bounty, dengan validasi scope bawaan dan pencatatan temuan otomatis.
🎯 Fitur
Subdomain Enumeration — Wrapper untuk Subfinder dengan validasi scope
API Endpoint Fuzzing — Fuzzing pintar dengan logging otomatis
Vulnerability Scanning — Integrasi Nuclei dengan output JSON
Scope Validation — Mencegah pengujian di luar izin
Automated Logging — Ekspor temuan ke JSON dan Markdown
CLI Interface — Mudah dipakai lewat command line
📦 Instalasi
Prasyarat
Python 3.8+
Go (untuk Subfinder)
Nuclei (untuk scanning)
Langkah 1: Install dependensi Python
Bash
Langkah 2: Install Subfinder
Bash
Verifikasi:
Bash
Langkah 3: Install Nuclei
Bash
Verifikasi:
Bash
Langkah 4: Clone dan pakai
Bash
🚀 Quick Start
Pemakaian dasar (sebagai library)
Python
Pemakaian CLI
Bash
📊 Logging
Temuan otomatis dicatat ke:
findings.json — format JSON untuk analisis terprogram
findings.md — format Markdown untuk laporan yang mudah dibaca
fuzz_findings.json — hasil API fuzzing
nuclei_findings.json — hasil scan Nuclei
Setiap entri log berisi:
Timestamp
URL target
Payload/Test yang dipakai
Cuplikan response (500 karakter pertama)
🛡️ Scope Validation
Tool ini punya validasi scope bawaan untuk mencegah pengujian tanpa izin:
Python
🔧 Konfigurasi
Wordlist kustom untuk fuzzing
Python
Menonaktifkan logging
Python
🐛 Troubleshooting
Error: subfinder: command not found
Bash
Error: nuclei: command not found
Bash
Error: ModuleNotFoundError: No module named 'requests'
Bash
Error: Permission denied saat menulis log
Bash
Error: TimeoutExpired
Naikkan nilai timeout di security_tools.py:
Python
Scope validation memblokir target yang sah
Periksa format scope:
Python
📚 API Reference
run_recon(domain, allowed_scope=None)
Enumerasi subdomain menggunakan Subfinder.
domain (str): Domain target
allowed_scope (list): Daftar domain/network yang diizinkan
Returns: List subdomain
fuzz_api_endpoint(base_url, wordlist=None, allowed_scope=None, log_findings=True)
Fuzzing endpoint API dan menemukan path.
base_url (str): Base URL yang di-fuzz
wordlist (list): Wordlist kustom
allowed_scope (list): Validasi scope
log_findings (bool): Aktifkan logging
Returns: List temuan dengan status code
run_nuclei_scan(target_url, allowed_scope=None, log_findings=True)
Menjalankan Nuclei vulnerability scanner.
target_url (str): URL target
allowed_scope (list): Validasi scope
log_findings (bool): Aktifkan logging
Returns: Dictionary jumlah dan daftar temuan
🔒 Security & Ethics
Selalu dapatkan izin resmi sebelum melakukan pengujian
Hormati batasan scope yang ditentukan
Jangan mengganggu layanan yang sedang berjalan
Ikuti praktik responsible disclosure
Jangan pernah mengakses atau mengubah data pengguna tanpa izin
📄 Lisensi
MIT License — lihat LICENSE untuk detail.
👤 Author
gadelz
GitHub: @gadelz
🙏 Acknowledgments
ProjectDiscovery — Subfinder & Nuclei
📝 Changelog
v1.0.0
Rilis awal
Subdomain enumeration dengan Subfinder
API endpoint fuzzing
Integrasi Nuclei
Scope validation
Automated logging (JSON/Markdown)
CLI interface
Happy Hunting! 🎯
