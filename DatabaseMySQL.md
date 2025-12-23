# 🐬 Python & MySQL Database

MySQL adalah salah satu sistem manajemen database relasional (RDBMS) paling populer di dunia. Berbeda dengan SQLite yang file-based, MySQL adalah database server yang lebih powerful dan cocok untuk aplikasi production dengan banyak pengguna.

---

## 🚀 Mengapa MySQL?

MySQL memiliki beberapa keunggulan:

- **Scalable**: Mampu menangani jutaan data dengan performa tinggi
- **Multi-user**: Mendukung banyak pengguna secara bersamaan
- **Client-Server**: Arsitektur yang memisahkan database server dan aplikasi client
- **Open Source**: Gratis dan didukung komunitas besar
- **Cross-platform**: Berjalan di Windows, Linux, macOS

---

## ⚙️ Instalasi MySQL

### 1. Install MySQL Server

**Windows:**
Download installer dari [MySQL Official Website](https://dev.mysql.com/downloads/installer/) dan ikuti wizard instalasi.

**macOS:**
```bash
brew install mysql
brew services start mysql
```

**Linux (Ubuntu):**
```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
```

### 2. Install MySQL Connector untuk Python

Setelah MySQL Server terinstall, kita perlu library Python untuk berkomunikasi dengan MySQL:

```bash
pip install mysql-connector-python
```

---

## 🔌 Koneksi ke MySQL Server

### Membuat Koneksi Dasar

```python
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password_anda'
    )
    
    if connection.is_connected():
        print("✅ Berhasil terhubung ke MySQL Server")
        
except Error as e:
    print(f"❌ Error: {e}")
    
finally:
    if connection.is_connected():
        connection.close()
        print("Koneksi ditutup")
```

::: warning ⚠️ **Keamanan**
Jangan pernah hard-code password di kode! Gunakan environment variables atau file konfigurasi terpisah.
:::

### Koneksi dengan Input User

```python
from getpass import getpass
import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user=input("Username MySQL: "),
        password=getpass("Password: ")
    )
    print("✅ Koneksi berhasil!")
    
except mysql.connector.Error as e:
    print(f"❌ Gagal koneksi: {e}")
```

---

## 🗄️ Membuat dan Menggunakan Database

### Membuat Database Baru

```python
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password'
)

cursor = connection.cursor()

# Membuat database
cursor.execute("CREATE DATABASE IF NOT EXISTS toko_buku")
print("✅ Database 'toko_buku' berhasil dibuat!")

cursor.close()
connection.close()
```

### Koneksi ke Database Spesifik

```python
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='toko_buku'  # Langsung ke database
)
```

---

## 📊 Membuat Tabel (CREATE TABLE)

```python
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='toko_buku'
)

cursor = connection.cursor()

# Query CREATE TABLE
create_table_query = """
CREATE TABLE IF NOT EXISTS buku (
    id INT AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(200) NOT NULL,
    penulis VARCHAR(100),
    tahun_terbit YEAR,
    harga DECIMAL(10, 2),
    stok INT DEFAULT 0
)
"""

cursor.execute(create_table_query)
connection.commit()

print("✅ Tabel 'buku' berhasil dibuat!")

cursor.close()
connection.close()
```

### Tipe Data MySQL yang Umum

| Tipe Data | Deskripsi | Contoh |
|-----------|-----------|--------|
| `INT` | Bilangan bulat | 100, -50 |
| `VARCHAR(n)` | String dengan panjang maksimal n | "Budi" |
| `TEXT` | String panjang | Deskripsi artikel |
| `DECIMAL(m,d)` | Angka desimal | 99.99 |
| `DATE` | Tanggal (YYYY-MM-DD) | 2025-01-15 |
| `DATETIME` | Tanggal + waktu | 2025-01-15 14:30:00 |
| `YEAR` | Tahun | 2025 |

---

## ➕ Menambah Data (INSERT)

### Insert Single Record

```python
cursor = connection.cursor()

insert_query = """
INSERT INTO buku (judul, penulis, tahun_terbit, harga, stok)
VALUES (%s, %s, %s, %s, %s)
"""

data = ("Laskar Pelangi", "Andrea Hirata", 2005, 85000, 15)

cursor.execute(insert_query, data)
connection.commit()

print(f"✅ {cursor.rowcount} buku berhasil ditambahkan!")
```

### Insert Multiple Records

```python
cursor = connection.cursor()

insert_query = """
INSERT INTO buku (judul, penulis, tahun_terbit, harga, stok)
VALUES (%s, %s, %s, %s, %s)
"""

data_buku = [
    ("Bumi Manusia", "Pramoedya Ananta Toer", 1980, 95000, 10),
    ("Negeri 5 Menara", "Ahmad Fuadi", 2009, 78000, 20),
    ("Ronggeng Dukuh Paruk", "Ahmad Tohari", 1982, 65000, 8),
    ("Cantik Itu Luka", "Eka Kurniawan", 2002, 89000, 12)
]

cursor.executemany(insert_query, data_buku)
connection.commit()

print(f"✅ {cursor.rowcount} buku berhasil ditambahkan!")
```

---

## 🔍 Membaca Data (SELECT)

### Select Semua Data

```python
cursor = connection.cursor()

cursor.execute("SELECT * FROM buku")
hasil = cursor.fetchall()

for buku in hasil:
    print(f"ID: {buku[0]}, Judul: {buku[1]}, Penulis: {buku[2]}, Harga: Rp{buku[4]:,.0f}")
```

### Select dengan Kondisi (WHERE)

```python
cursor.execute("SELECT * FROM buku WHERE harga < %s", (80000,))
buku_murah = cursor.fetchall()

print("📚 Buku dengan harga < Rp80.000:")
for buku in buku_murah:
    print(f"- {buku[1]} oleh {buku[2]} (Rp{buku[4]:,.0f})")
```

### Select Kolom Tertentu

```python
cursor.execute("SELECT judul, penulis FROM buku WHERE tahun_terbit > 2000")

for row in cursor.fetchall():
    print(f"📖 {row[0]} - {row[1]}")
```

### Menggunakan LIMIT

```python
# Ambil 5 buku pertama
cursor.execute("SELECT * FROM buku LIMIT 5")
top_5 = cursor.fetchall()
```

---

## ✏️ Mengupdate Data (UPDATE)

```python
cursor = connection.cursor()

update_query = """
UPDATE buku 
SET harga = %s, stok = %s 
WHERE judul = %s
"""

cursor.execute(update_query, (90000, 25, "Laskar Pelangi"))
connection.commit()

print(f"✅ {cursor.rowcount} data berhasil diupdate!")
```

---

## 🗑️ Menghapus Data (DELETE)

```python
cursor = connection.cursor()

delete_query = "DELETE FROM buku WHERE stok = 0"

cursor.execute(delete_query)
connection.commit()

print(f"✅ {cursor.rowcount} buku dengan stok 0 berhasil dihapus!")
```

---

## 🔗 Relasi Antar Tabel (JOIN)

### Membuat Tabel dengan Foreign Key

```python
# Tabel kategori
create_kategori = """
CREATE TABLE IF NOT EXISTS kategori (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_kategori VARCHAR(50)
)
"""

# Tabel buku dengan foreign key
create_buku_v2 = """
CREATE TABLE IF NOT EXISTS buku_v2 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(200),
    kategori_id INT,
    FOREIGN KEY (kategori_id) REFERENCES kategori(id)
)
"""

cursor.execute(create_kategori)
cursor.execute(create_buku_v2)
connection.commit()
```

### Query dengan JOIN

```python
join_query = """
SELECT buku_v2.judul, kategori.nama_kategori
FROM buku_v2
INNER JOIN kategori ON buku_v2.kategori_id = kategori.id
"""

cursor.execute(join_query)
for row in cursor.fetchall():
    print(f"{row[0]} - Kategori: {row[1]}")
```

---

## 💡 Best Practices

### 1. Gunakan Context Manager

```python
import mysql.connector

with mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='toko_buku'
) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM buku")
        hasil = cursor.fetchall()
        # Koneksi otomatis ditutup
```

### 2. Hindari SQL Injection

**❌ JANGAN:**
```python
nama = input("Nama buku: ")
query = f"SELECT * FROM buku WHERE judul = '{nama}'"  # BAHAYA!
```

**✅ LAKUKAN:**
```python
nama = input("Nama buku: ")
query = "SELECT * FROM buku WHERE judul = %s"
cursor.execute(query, (nama,))  # AMAN
```

### 3. Selalu Commit Perubahan

```python
cursor.execute("INSERT INTO buku ...")
connection.commit()  # Jangan lupa!
```

---

## 🛠️ Latihan: Aplikasi CRUD Sederhana

Buatlah aplikasi manajemen perpustakaan dengan fitur:
1. Tambah buku baru
2. Lihat semua buku
3. Cari buku berdasarkan judul
4. Update stok buku
5. Hapus buku

**Hint:** Gunakan loop `while` untuk menu interaktif, dan fungsi-fungsi terpisah untuk setiap operasi CRUD.

---

## 🚀 Langkah Selanjutnya

Setelah menguasai MySQL dengan Python, Anda bisa belajar:
- **ORM (SQLAlchemy)**: Cara bekerja dengan database tanpa menulis SQL manual
- **Database Design**: Normalisasi, indexing, dan optimasi query
- **Connection Pooling**: Manajemen koneksi untuk aplikasi besar

---

[⬅️ Kembali ke Menu Utama](README.md)
