# 📦 Python PIP: Manajemen Paket Python

**PIP** adalah manajer paket untuk Python. Dengan PIP, Anda dapat menginstal modul atau library tambahan yang tidak disertakan dalam instalasi standar Python.

---

## 🚀 Apa itu Paket (Package)?
Paket berisi semua file yang diperlukan untuk sebuah modul. Modul adalah library kode Python yang bisa Anda sertakan dalam proyek Anda.

---

## 🛠️ Perintah Dasar PIP

PIP biasanya dijalankan melalui terminal atau command prompt.

### 1. Mengecek Versi PIP
Pastikan PIP sudah terinstal di sistem Anda:
```bash
pip --version
```

### 2. Menginstal Paket
Untuk menginstal paket baru, gunakan perintah `install`:
```bash
pip install nama_paket
```
*Contoh menginstal library `requests`:*
```bash
pip install requests
```

### 3. Menggunakan Paket yang Terinstal
Setelah diinstal, Anda bisa langsung mengimpornya dalam kode Python:
```python
import requests

respons = requests.get('https://www.google.com')
print(respons.status_code)
```

### 4. Melihat Daftar Paket
Untuk melihat paket apa saja yang sudah terinstal di komputer Anda:
```bash
pip list
```

### 5. Menghapus Paket (Uninstall)
Jika paket sudah tidak digunakan:
```bash
pip uninstall nama_paket
```

---

## 🧬 Manajemen Dependencies dengan `requirements.txt`

Dalam proyek besar, biasanya kita menggunakan file `requirements.txt` untuk mencatat semua library yang dibutuhkan.

### Menyimpan daftar paket:
```bash
pip freeze > requirements.txt
```

### Menginstal semua paket dari file tersebut:
```bash
pip install -r requirements.txt
```

---

## 💡 Tips Penting

1. **Gunakan Virtual Environment**: Sangat disarankan untuk menggunakan **venv** agar paket antar proyek tidak saling bertabrakan.
   ```bash
   python -m venv env
   source env/bin/activate  # Untuk Mac/Linux
   # atau
   .\env\Scripts\activate   # Untuk Windows
   ```
2. **Upgrade PIP**: Pastikan PIP Anda selalu versi terbaru.
   ```bash
   python -m pip install --upgrade pip
   ```
3. **PyPI**: Semua paket yang diinstal melalui PIP berasal dari [pypi.org](https://pypi.org). Anda bisa mencari ribuan library di sana.

---

## 🔥 Alternatif Modern (Kekinian)

Dalam industri pengembangan Python saat ini, banyak developer dan tim proyek beralih dari kombinasi tradisional `pip + venv` ke alat pengelola paket modern yang jauh lebih cepat dan terintegrasi:

### 1. **uv** (oleh Astral)
`uv` adalah manajer paket Python yang ditulis dalam bahasa Rust. Alat ini memiliki kecepatan instalasi paket hingga **10-100 kali lebih cepat** dibandingkan `pip` tradisional, karena mengimplementasikan sistem caching yang sangat pintar.
* Cara menginstal: `curl -LsSf https://astral.sh/uv/install.sh | sh` (di macOS/Linux)
* Membuat virtual env: `uv venv`
* Menginstal paket: `uv pip install requests`

### 2. **Poetry**
`Poetry` adalah alat manajemen dependensi dan pengemasan proyek yang serbaguna. Ia menggunakan satu file konfigurasi standar `pyproject.toml` untuk mengatur semua dependensi, versi Python, metadata proyek, dan melakukan *lock* dependensi secara otomatis (menjamin kecocokan versi library di komputer developer lain).
* Membuat proyek baru: `poetry new nama-proyek`
* Menambahkan paket: `poetry add requests`

---

### 🛠️ Latihan Kecil
Coba instal library `camelcase` dan gunakan untuk mengubah kalimat menjadi format camel case!

```python
# Di terminal: pip install camelcase

# Di file python:
import camelcase

c = camelcase.CamelCase()
teks = "halo dunia python"
print(c.hump(teks)) # Output: Halo Dunia Python
```
