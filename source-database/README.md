# 📁 Source Database - Contoh Praktik Database SQLite

Folder ini berisi contoh-contoh praktik penggunaan database SQLite dengan Python.

## 📋 Daftar File

### 1. `contoh_dasar.py`
File pembelajaran dengan 8 contoh operasi database dasar:
- Koneksi database
- Membuat tabel
- Insert data (single & multiple)
- Select data dengan kondisi
- Update data
- Delete data
- Fungsi agregasi (COUNT, AVG, MAX, MIN)
- Context manager

**Cara menjalankan:**
```bash
python contoh_dasar.py
```

### 2. `app_siswa.py`
Aplikasi manajemen data siswa lengkap dengan fitur:
- ✅ Tambah siswa baru
- 📋 Lihat semua siswa
- 🔍 Cari siswa berdasarkan nama
- ✏️ Update nilai siswa
- 🗑️ Hapus siswa
- 📊 Statistik (total, rata-rata, nilai tertinggi/terendah)

**Cara menjalankan:**
```bash
python app_siswa.py
```

## 🎯 Tujuan Pembelajaran

Setelah mempelajari contoh-contoh ini, Anda akan mampu:
1. Membuat dan mengelola database SQLite
2. Melakukan operasi CRUD (Create, Read, Update, Delete)
3. Menggunakan parameterized queries untuk keamanan
4. Membuat aplikasi berbasis database sederhana
5. Menerapkan best practices dalam pengelolaan database

## 💡 Tips

- Mulai dari `contoh_dasar.py` untuk memahami konsep fundamental
- Setelah paham, coba jalankan `app_siswa.py` untuk melihat implementasi nyata
- Eksperimen dengan memodifikasi kode untuk pembelajaran lebih dalam
- File database (`.db`) akan dibuat otomatis saat program dijalankan

## ⚠️ Catatan Keamanan

Selalu gunakan **parameterized queries** (dengan `?` placeholder) untuk mencegah SQL Injection:

```python
# ✅ AMAN
cursor.execute("SELECT * FROM siswa WHERE nama = ?", (nama,))

# ❌ BAHAYA - Jangan lakukan ini!
cursor.execute(f"SELECT * FROM siswa WHERE nama = '{nama}'")
```

## 🚀 Langkah Selanjutnya

Setelah menguasai SQLite, Anda bisa lanjut ke:
- **MySQL/PostgreSQL**: Database server untuk aplikasi production
- **SQLAlchemy**: ORM (Object-Relational Mapping) untuk Python
- **Database Design**: Normalisasi, relasi, dan optimasi query
