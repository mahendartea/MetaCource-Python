# 📊 Python CSV: Mengolah Data Spreadsheet

**CSV** (*Comma Separated Values*) adalah format file sederhana yang digunakan untuk menyimpan data tabular, seperti spreadsheet atau database. Python memiliki modul bawaan `csv` untuk membaca dan menulis file ini dengan mudah.

---

## 🚀 Memulai dengan `csv`

Impor modul `csv` sebelum memulai:

```python
import csv
```

---

## 📖 Membaca File CSV

Misalkan kita memiliki file `siswa.csv` dengan isi sebagai berikut:
```text
nama,kelas,nilai
Andi,10A,90
Budi,10B,85
Cici,10A,95
```

### 1. Menggunakan `csv.reader`
Fungsi ini membaca setiap baris sebagai **list**.

```python
with open('siswa.csv', mode='r') as file:
    reader = csv.reader(file)
    for baris in reader:
        print(f"Nama: {baris[0]}, Kelas: {baris[1]}, Nilai: {baris[2]}")
```

### 2. Menggunakan `csv.DictReader` (Direkomendasikan)
Fungsi ini membaca setiap baris sebagai **dictionary**, di mana header (baris pertama) menjadi kuncinya.

```python
with open('siswa.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for baris in reader:
        print(f"{baris['nama']} berada di kelas {baris['kelas']}")
```

---

## ✍️ Menulis File CSV

### 1. Menggunakan `csv.writer`
Kita bisa menulis data dalam bentuk list.

```python
data = [
    ['nama', 'jurusan', 'tahun'],
    ['Dedi', 'Informatika', '2023'],
    ['Eka', 'Sistem Informasi', '2024']
]

with open('alumni.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

### 2. Menggunakan `csv.DictWriter`
Lebih rapi karena menggunakan dictionary.

```python
with open('produk.csv', mode='w', newline='') as file:
    kolom = ['id', 'nama_barang', 'harga']
    writer = csv.DictWriter(file, fieldnames=kolom)

    writer.writeheader() # Menulis header
    writer.writerow({'id': 1, 'nama_barang': 'Keyboard', 'harga': 150000})
    writer.writerow({'id': 2, 'nama_barang': 'Mouse', 'harga': 80000})
```

---

## 💡 Parameter Penting

- `newline=''`: Sangat disarankan saat membuka file untuk menulis guna menghindari baris kosong tambahan di sistem operasi tertentu (seperti Windows).
- `delimiter`: Jika file Anda menggunakan titik koma (`;`) dan bukan koma, Anda bisa menentukannya:
  ```python
  reader = csv.reader(file, delimiter=';')
  ```

---

## 🛠️ Latihan Kecil
Buatlah kode Python yang membaca file CSV berisi daftar belanjaan (item, jumlah), lalu hitung total seluruh item yang dibeli!

```python
import csv

# Anggap ada file 'belanja.csv'
# item,jumlah
# Beras,5
# Minyak,2

total = 0
with open('belanja.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for baris in reader:
        total += int(baris['jumlah'])

print(f"Total item yang dibeli: {total}")
```

---

### 🚀 Tips Lanjutan
Jika Anda mengolah data yang sangat besar atau butuh analisis statistik, pertimbangkan untuk belajar library **Pandas**. Pandas jauh lebih cepat dan kuat untuk urusan tabel data!
