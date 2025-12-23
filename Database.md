# 🗄️ Python Database: Pengenalan Database dengan SQLite

Database adalah sistem terorganisir untuk menyimpan, mengelola, dan mengambil data. Python memiliki dukungan bawaan untuk **SQLite**, database ringan yang sempurna untuk belajar dan aplikasi kecil hingga menengah.

---

## 🚀 Mengapa SQLite?

- **Tanpa Instalasi**: SQLite sudah termasuk dalam Python, tidak perlu install server terpisah.
- **File-Based**: Database disimpan dalam satu file `.db` yang mudah dipindahkan.
- **SQL Standard**: Menggunakan bahasa SQL yang sama dengan database besar seperti MySQL dan PostgreSQL.

---

## 🛠️ Memulai dengan SQLite

### 1. Import Modul
```python
import sqlite3
```

### 2. Membuat Koneksi dan Database
```python
# Membuat koneksi (jika file tidak ada, akan dibuat otomatis)
conn = sqlite3.connect('sekolah.db')

# Membuat cursor untuk eksekusi perintah SQL
cursor = conn.cursor()

print("Database berhasil dibuat!")
```

---

## 📊 Operasi CRUD (Create, Read, Update, Delete)

### 1. CREATE - Membuat Tabel
```python
cursor.execute('''
CREATE TABLE IF NOT EXISTS siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    kelas TEXT,
    nilai INTEGER
)
''')

conn.commit()
print("Tabel siswa berhasil dibuat!")
```

### 2. INSERT - Menambah Data
```python
# Menambah satu data
cursor.execute('''
INSERT INTO siswa (nama, kelas, nilai) 
VALUES (?, ?, ?)
''', ('Andi', '10A', 90))

# Menambah banyak data sekaligus
data_siswa = [
    ('Budi', '10B', 85),
    ('Cici', '10A', 95),
    ('Dedi', '10C', 78)
]

cursor.executemany('''
INSERT INTO siswa (nama, kelas, nilai) 
VALUES (?, ?, ?)
''', data_siswa)

conn.commit()
print(f"{cursor.rowcount} data berhasil ditambahkan!")
```

### 3. SELECT - Membaca Data
```python
# Mengambil semua data
cursor.execute('SELECT * FROM siswa')
semua_siswa = cursor.fetchall()

for siswa in semua_siswa:
    print(f"ID: {siswa[0]}, Nama: {siswa[1]}, Kelas: {siswa[2]}, Nilai: {siswa[3]}")

# Mengambil dengan kondisi
cursor.execute('SELECT * FROM siswa WHERE nilai >= ?', (85,))
siswa_terbaik = cursor.fetchall()
print(f"\nSiswa dengan nilai >= 85: {siswa_terbaik}")
```

### 4. UPDATE - Mengubah Data
```python
cursor.execute('''
UPDATE siswa 
SET nilai = ? 
WHERE nama = ?
''', (92, 'Andi'))

conn.commit()
print(f"{cursor.rowcount} data berhasil diupdate!")
```

### 5. DELETE - Menghapus Data
```python
cursor.execute('DELETE FROM siswa WHERE nilai < ?', (80,))
conn.commit()
print(f"{cursor.rowcount} data berhasil dihapus!")
```

---

## 🔒 Best Practices

### 1. Selalu Gunakan Parameterized Queries
**JANGAN** seperti ini (rentan SQL Injection):
```python
nama = "Andi"
cursor.execute(f"SELECT * FROM siswa WHERE nama = '{nama}'")  # ❌ BAHAYA!
```

**LAKUKAN** seperti ini:
```python
cursor.execute("SELECT * FROM siswa WHERE nama = ?", (nama,))  # ✅ AMAN
```

### 2. Gunakan Context Manager
```python
# Otomatis menutup koneksi
with sqlite3.connect('sekolah.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM siswa')
    hasil = cursor.fetchall()
    # conn.commit() otomatis dipanggil
# Koneksi otomatis ditutup di sini
```

### 3. Jangan Lupa `commit()` dan `close()`
```python
conn.commit()  # Simpan perubahan
conn.close()   # Tutup koneksi
```

---

## 💡 Fungsi Cursor yang Berguna

| Fungsi | Deskripsi |
| :--- | :--- |
| `fetchone()` | Mengambil satu baris hasil query |
| `fetchall()` | Mengambil semua baris hasil query |
| `fetchmany(n)` | Mengambil n baris hasil query |
| `rowcount` | Jumlah baris yang terpengaruh operasi terakhir |

---

## 🛠️ Latihan: Aplikasi Sederhana

Lihat folder `source-database/` untuk contoh aplikasi lengkap manajemen siswa dengan menu interaktif!

---

## 🚀 Langkah Selanjutnya

Setelah menguasai SQLite, Anda bisa belajar:
- **MySQL/PostgreSQL**: Database server untuk aplikasi production
- **ORM (SQLAlchemy)**: Cara bekerja dengan database tanpa menulis SQL langsung
- **Database Design**: Normalisasi, relasi antar tabel, indexing
