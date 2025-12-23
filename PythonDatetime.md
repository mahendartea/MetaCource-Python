# 🗓️ Python Datetime: Menguasai Waktu dan Tanggal

Modul `datetime` di Python menyediakan berbagai kelas untuk memanipulasi tanggal dan waktu. Baik Anda ingin mencatat waktu log, menghitung selisih hari, atau memformat tampilan tanggal, modul ini adalah alat utamanya.

---

## 🚀 Memulai dengan `datetime`

Untuk menggunakan fitur ini, kita perlu mengimpor modulnya terlebih dahulu:

```python
import datetime
```

### 1. Mendapatkan Waktu Sekarang
Cara paling umum untuk memulai adalah dengan melihat waktu saat ini.

```python
sekarang = datetime.datetime.now()
print(f"Waktu sekarang: {sekarang}")
```

---

## 🧱 Objek Dasar dalam `datetime`

Modul ini memiliki beberapa kelas utama yang sering digunakan:

### `datetime.date`
Digunakan untuk menangani tanggal saja (Tahun, Bulan, Hari).
```python
tgl = datetime.date(2025, 12, 25)
print(f"Tanggal: {tgl}")
print(f"Tahun: {tgl.year}, Bulan: {tgl.month}, Hari: {tgl.day}")
```

### `datetime.time`
Digunakan untuk menangani waktu saja (Jam, Menit, Detik, Mikrodetik).
```python
waktu = datetime.time(14, 30, 0)
print(f"Waktu: {waktu}")
```

### `datetime.datetime`
Kombinasi dari tanggal dan waktu.
```python
dt = datetime.datetime(2025, 12, 25, 14, 30, 0)
print(f"Gabungan: {dt}")
```

---

## 🎨 Memformat Tanggal (`strftime`)

Terkadang kita ingin menampilkan tanggal dalam format tertentu (misal: "25 Desember 2025"). Kita menggunakan metode `strftime` (*string format time*).

| Kode | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `%Y` | Tahun (4 digit) | 2025 |
| `%m` | Bulan (angka) | 12 |
| `%B` | Nama Bulan | December |
| `%d` | Hari dalam bulan | 25 |
| `%H` | Jam (00-23) | 14 |
| `%M` | Menit | 30 |

**Contoh Penggunaan:**
```python
sekarang = datetime.datetime.now()
format_kustom = sekarang.strftime("%d %B %Y, %H:%M")
print(f"Format Cantik: {format_kustom}")
```

---

## 🧩 Mengubah String Menjadi Objek (`strptime`)

Jika Anda menerima data tanggal dalam bentuk teks (String), Anda bisa mengubahnya menjadi objek `datetime` agar bisa diolah secara matematis.

```python
teks_tgl = "2025-12-25"
objek_tgl = datetime.datetime.strptime(teks_tgl, "%Y-%m-%d")
print(f"Hasil konversi: {objek_tgl}")
```

---

## ⏳ Operasi Waktu dengan `timedelta`

`timedelta` digunakan untuk merepresentasikan durasi atau selisih waktu. Ini sangat berguna untuk menambah atau mengurangi hari/menit dari suatu tanggal.

### Menambah Hari
```python
hari_ini = datetime.date.today()
besok = hari_ini + datetime.timedelta(days=1)
minggu_depan = hari_ini + datetime.timedelta(weeks=1)

print(f"Hari ini: {hari_ini}")
print(f"Besok: {besok}")
print(f"Minggu depan: {minggu_depan}")
```

### Menghitung Selisih
```python
tgl_lahir = datetime.date(2000, 1, 1)
umur_hari = hari_ini - tgl_lahir
print(f"Anda telah hidup selama {umur_hari.days} hari!")
```

---

## 💡 Tips & Trik

1. **Gunakan `date.today()`** jika Anda hanya butuh tanggal hari ini tanpa informasi jam.
2. **Hati-hati dengan Timezone**: Secara default, `datetime` bersifat "naive" (tidak sadar zona waktu). Untuk aplikasi global, pertimbangkan menggunakan modul `pytz` atau `zoneinfo` (Python 3.9+).
3. **Konversi Timestamp**: Gunakan `datetime.fromtimestamp(timestamp)` untuk mengubah detik UNIX menjadi objek datetime.

---

### 🛠️ Latihan Kecil
Cobalah buat kode untuk menghitung berapa hari lagi menuju Tahun Baru!

```python
import datetime

hari_ini = datetime.datetime.now()
tahun_baru = datetime.datetime(hari_ini.year + 1, 1, 1)
selisih = tahun_baru - hari_ini

print(f"Sisa waktu menuju tahun baru: {selisih.days} hari, {selisih.seconds // 3600} jam.")
```
