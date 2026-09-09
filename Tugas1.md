# 📝 Tugas Mandiri: Pemrograman Python (Pertemuan 1 - 10)

Selamat datang di lembar tugas terstruktur untuk menguji pemahaman Anda dari **Pertemuan 1 hingga Pertemuan 10** (mulai dari Variabel, Input/Output, Tipe Data, String Handling, Operasi, Percabangan, Perulangan, Fungsi, Modul, hingga Datetime).

---

## 📌 Petunjuk Pengerjaan & Pengumpulan

::: info 🎯 **Instruksi Pengerjaan**
1. **Buat & Ketik Ulang Kode Program**: Salin dan jalankan listing program Python pada masing-masing nomor di komputer/editor Anda (VS Code, PyCharm, atau editor pilihan).
2. **Screenshot Hasil Running**: Jalankan kode program di terminal, masukkan data uji sesuai skenario, lalu ambil tangkapan layar (*screenshot*) terminal secara jelas.
3. **Buat Analisis / Penjelasan Kode**: Tuliskan penjelasan ringkas mengenai:
   * Variabel, tipe data, dan modul yang digunakan.
   * Alur logika fungsi, percabangan (`if-elif-else`), dan perulangan (`for`/`while`).
   * Cara modul `datetime` memproses tanggal, jam, atau format waktu.
4. **Format Pengumpulan**: Simpan seluruh kode, screenshot output terminal, dan penjelasan ke dalam satu dokumen (**PDF** / **Word**) dengan format penamaan: `Tugas1_NIM_NamaLengkap.pdf`.
:::

---

## 🚗 Soal 1: Sistem Rental Mobil & Penghitung Denda Keterlambatan

* **Topik Materi**: `Variable`, `Input/Output`, `Operasi Aritmatika`, `Percabangan (if-else)`, `Fungsi (def)`, `Modul datetime (strptime, selisih hari)`.
* **Skenario Kasus**:
  Sebuah rental kendaraan membutuhkan sistem otomatis untuk menghitung denda pengembalian mobil. Sistem menerima input nama penyewa, tanggal rencana kembali, dan tanggal aktual saat mobil dikembalikan. Program akan mendeteksi apakah pengembalian tepat waktu atau terlambat. Jika terlambat, program akan mengalikan jumlah hari keterlambatan dengan tarif denda harian (Rp 50.000/hari).

### Listing Program:

```python
import datetime

def hitung_rental(nama_penyewa: str, tgl_kembali_rencana: str, tgl_kembali_real: str, tarif_per_hari: int, denda_per_hari: int):
    format_tgl = "%Y-%m-%d"
    
    # 1. Konversi string input menjadi objek date
    tgl_rencana = datetime.datetime.strptime(tgl_kembali_rencana.strip(), format_tgl).date()
    tgl_kembali = datetime.datetime.strptime(tgl_kembali_real.strip(), format_tgl).date()
    
    print("\n" + "=" * 45)
    print("        STRUK PENGEMBALIAN RENTAL MOBIL      ")
    print("=" * 45)
    print(f"Nama Penyewa         : {nama_penyewa.upper()}")
    print(f"Batas Pengembalian   : {tgl_rencana.strftime('%d %B %Y')}")
    print(f"Tanggal Dikembalikan : {tgl_kembali.strftime('%d %B %Y')}")
    print("-" * 45)
    
    # 2. Percabangan mengecek keterlambatan
    if tgl_kembali > tgl_rencana:
        hari_terlambat = (tgl_kembali - tgl_rencana).days
        total_denda = hari_terlambat * denda_per_hari
        status = f"TERLAMBAT ({hari_terlambat} Hari)"
    else:
        hari_terlambat = 0
        total_denda = 0
        status = "TEPAT WAKTU (Bebas Denda)"
        
    print(f"Status Pengembalian  : {status}")
    print(f"Total Biaya Denda    : Rp {total_denda:,.2f}")
    print("=" * 45 + "\n")

if __name__ == "__main__":
    nama = input("Masukkan Nama Penyewa                      : ")
    tgl_target = input("Masukkan Tanggal Tenggat Kembali (YYYY-MM-DD) : ")
    tgl_aktual = input("Masukkan Tanggal Pengembalian Nyata (YYYY-MM-DD): ")
    
    TARIF_HARIAN = 350_000
    DENDA_HARIAN = 50_000
    
    hitung_rental(nama, tgl_target, tgl_aktual, TARIF_HARIAN, DENDA_HARIAN)
```

::: tip 💡 Tugas Mahasiswa untuk Soal 1:
1. Jalankan kode di terminal dengan 2 skenario uji:
   * **Uji A (Tepat Waktu)**: Batas 2026-09-10, kembali 2026-09-10.
   * **Uji B (Terlambat)**: Batas 2026-09-10, kembali 2026-09-14.
2. Lampirkan screenshot output kedua skenario tersebut.
3. Jelaskan fungsi method `.strptime()`, atribut `.days`, dan fungsi method `.strftime()`.
:::

---

## 🛒 Soal 2: Kasir Minimarket & Cetak Struk dengan Stempel Waktu

* **Topik Materi**: `Tipe Data List & Dictionary`, `Perulangan (for loop)`, `String Formatting (f-string)`, `Operasi Aritmatika`, `Modul datetime (datetime.now, strftime)`.
* **Skenario Kasus**:
  Sebuah minimarket modern ingin mencetak struk transaksi pelanggan secara otomatis. Struk harus memuat nama kasir, daftar belanjaan (diproses dari struktur data `list of dictionary`), total belanjaan, diskon member sebesar 10% jika belanja mencapai minimal Rp 100.000, dan stempel waktu (*timestamp*) transaksi yang diambil secara *real-time* saat program dijalankan.

### Listing Program:

```python
from datetime import datetime

def cetak_struk(kasir: str, daftar_belanja: list, is_member: bool):
    # Mengambil timestamp waktu transaksi saat ini
    waktu_transaksi = datetime.now()
    format_waktu = waktu_transaksi.strftime("%A, %d-%m-%Y %H:%M:%S")
    
    subtotal = 0
    print("\n" + "-" * 42)
    print("           TOKO SERBA ADA MODERN          ")
    print(f"Waktu Transaksi : {format_waktu}")
    print(f"Kasir           : {kasir.title()}")
    print("-" * 42)
    
    # Perulangan for untuk memproses setiap item barang
    for item in daftar_belanja:
        nama_barang = item["nama"]
        harga = item["harga"]
        qty = item["qty"]
        total_item = harga * qty
        subtotal += total_item
        print(f"{nama_barang:<18} x{qty:<2} : Rp {total_item:>9,}")
        
    print("-" * 42)
    print(f"Subtotal             : Rp {subtotal:>9,}")
    
    # Ternary operator untuk menentukan diskon member
    diskon = 0.1 * subtotal if (is_member and subtotal >= 100_000) else 0.0
    total_bayar = subtotal - diskon
    
    print(f"Diskon Member (10%)  : Rp {int(diskon):>9,}")
    print(f"TOTAL AKHIR          : Rp {int(total_bayar):>9,}")
    print("-" * 42)
    print("      Terima Kasih Telah Berbelanja!      \n")

if __name__ == "__main__":
    keranjang = [
        {"nama": "Kopi Susu Botol", "harga": 15000, "qty": 3},
        {"nama": "Roti Gandum", "harga": 22000, "qty": 2},
        {"nama": "Minyak Goreng 2L", "harga": 34000, "qty": 2},
    ]
    
    nama_kasir = input("Masukkan Nama Kasir                          : ")
    member_input = input("Apakah pelanggan memiliki Member Card? (y/t) : ").strip().lower()
    status_member = (member_input == 'y')
    
    cetak_struk(nama_kasir, keranjang, status_member)
```

::: tip 💡 Tugas Mahasiswa untuk Soal 2:
1. Jalankan program dan masukkan nama Anda sebagai kasir.
2. Screenshot hasil cetak struk di terminal.
3. Jelaskan makna penulisan format string `{nama_barang:<18}` dan `{total_item:>9,}`, serta bagaimana `datetime.now()` merekam waktu lokal.
:::

---

## ⏰ Soal 3: Presensi Karyawan & Deteksi Menit Keterlambatan

* **Topik Materi**: `Modul datetime (datetime.time, combine)`, `String Handling (.strip())`, `Type Hinting`, `Percabangan (if-elif-else)`, `Fungsi`.
* **Skenario Kasus**:
  Sebuah perusahaan memberlakukan jam masuk kantor tepat pukul `08:00:00 WIB`. Karyawan menginputkan jam kehadiran dalam format `HH:MM`. Sistem harus memvalidasi apakah karyawan datang tepat waktu, lebih awal, atau terlambat, serta menghitung secara presisi berapa menit selisih keterlambatannya menggunakan perhitungan detik `total_seconds()`.

### Listing Program:

```python
from datetime import datetime, time

def validasi_presensi(nama_karyawan: str, jam_masuk_str: str):
    # Jam batas masuk kantor: 08:00:00
    batas_masuk = time(8, 0, 0)
    
    # Mengubah string input jam menjadi objek time
    jam_input = datetime.strptime(jam_masuk_str.strip(), "%H:%M").time()
    
    # Menggabungkan dengan tanggal dummy yang sama untuk menghitung selisih waktu
    tgl_dummy = datetime(2026, 1, 1)
    dt_input = datetime.combine(tgl_dummy, jam_input)
    dt_batas = datetime.combine(tgl_dummy, batas_masuk)
    
    print("\n" + "=" * 42)
    print("      LAPORAN PRESENSI HARIAN PEGAWAI     ")
    print("=" * 42)
    print(f"Karyawan   : {nama_karyawan.strip().title()}")
    print(f"Jam Hadir  : {jam_input.strftime('%H:%M')} WIB")
    print(f"Batas Jam  : {batas_masuk.strftime('%H:%M')} WIB")
    print("-" * 42)
    
    if jam_input > batas_masuk:
        menit_telat = int((dt_input - dt_batas).total_seconds() // 60)
        print("Status     : TERLAMBAT ⚠️")
        print(f"Keterangan : Terlambat selama {menit_telat} menit.")
    elif jam_input == batas_masuk:
        print("Status     : TEPAT WAKTU ✅")
        print("Keterangan : Hadir persis pada jam batas masuk.")
    else:
        menit_awal = int((dt_batas - dt_input).total_seconds() // 60)
        print("Status     : SANGAT DISIPLIN 🌟")
        print(f"Keterangan : Hadir lebih awal {menit_awal} menit.")
        
    print("=" * 42 + "\n")

if __name__ == "__main__":
    nama = input("Masukkan Nama Pegawai                             : ")
    jam_hadir = input("Masukkan Jam Hadir (Format HH:MM contoh: 08:25) : ")
    validasi_presensi(nama, jam_hadir)
```

::: tip 💡 Tugas Mahasiswa untuk Soal 3:
1. Jalankan kode dengan input jam terlambat (contoh: `08:35`) dan jam tepat/lebih awal (contoh: `07:45`).
2. Lampirkan screenshot output dari kedua kondisi tersebut.
3. Jelaskan mengapa kita menggunakan `datetime.combine()` saat menghitung selisih antara dua objek `time`.
:::

---

## 🎂 Soal 4: Kalkulator Usia Lengkap & Hitung Mundur Ulang Tahun

* **Topik Materi**: `Modul datetime (date, timedelta)`, `Operasi Aritmatika & Perbandingan`, `Fungsi`, `String Handling`.
* **Skenario Kasus**:
  Aplikasi personal yang meminta tahun, bulan, dan hari lahir pengguna. Program menghitung usia pengguna secara tepat dalam satuan tahun dan jumlah total hari yang telah dilalui sejak lahir, serta menghitung mundur berapa hari lagi menuju hari ulang tahun berikutnya.

### Listing Program:

```python
from datetime import date

def kalkulator_umur(nama: str, tahun_lahir: int, bulan_lahir: int, tgl_lahir: int):
    hari_ini = date.today()
    tgl_kelahiran = date(tahun_lahir, bulan_lahir, tgl_lahir)
    
    # 1. Menghitung total hari hidup dan usia tahun
    total_hari_hidup = (hari_ini - tgl_kelahiran).days
    
    # Koreksi jika di tahun berjalan belum melewati bulan/tanggal ultah
    usia_tahun = hari_ini.year - tgl_kelahiran.year - (
        (hari_ini.month, hari_ini.day) < (tgl_kelahiran.month, tgl_kelahiran.day)
    )
    
    # 2. Menentukan target ulang tahun berikutnya
    tahun_ultah_berikut = hari_ini.year
    target_ultah = date(tahun_ultah_berikut, bulan_lahir, tgl_lahir)
    
    # Jika ulang tahun tahun ini sudah lewat, maka target adalah tahun depan
    if target_ultah < hari_ini:
        target_ultah = date(tahun_ultah_berikut + 1, bulan_lahir, tgl_lahir)
        
    sisa_hari_ultah = (target_ultah - hari_ini).days
    
    print("\n" + "*" * 45)
    print("         INFORMASI USIA & HARI LAHIR         ")
    print("*" * 45)
    print(f"Halo, {nama.title()}!")
    print(f"Tanggal Lahir        : {tgl_kelahiran.strftime('%d %B %Y')}")
    print(f"Tanggal Hari Ini     : {hari_ini.strftime('%d %B %Y')}")
    print("-" * 45)
    print(f"Usia Anda Saat Ini   : {usia_tahun} Tahun")
    print(f"Total Hari Hidup     : {total_hari_hidup:,} Hari")
    
    if sisa_hari_ultah == 0:
        print("🎉 Selamat! Hari ini adalah hari ulang tahun Anda! 🎂")
    else:
        print(f"Ulang Tahun Berikut  : {sisa_hari_ultah} hari lagi")
    print("*" * 45 + "\n")

if __name__ == "__main__":
    nama_user = input("Masukkan Nama Anda              : ")
    thn = int(input("Masukkan Tahun Lahir (YYYY)     : "))
    bln = int(input("Masukkan Bulan Lahir (1-12)     : "))
    tgl = int(input("Masukkan Tanggal Lahir (1-31)   : "))
    
    kalkulator_umur(nama_user, thn, bln, tgl)
```

::: tip 💡 Tugas Mahasiswa untuk Soal 4:
1. Masukkan tanggal lahir Anda sendiri dan jalankan programnya.
2. Screenshot hasil informasi usia yang ditampilkan di terminal.
3. Jelaskan baris logika: `(hari_ini.month, hari_ini.day) < (tgl_kelahiran.month, tgl_kelahiran.day)` yang digunakan untuk mengoreksi perhitungan usia tahun.
:::

---

## 🏨 Soal 5: Reservasi Kamar Hotel & Validasi Tanggal Menginap

* **Topik Materi**: `Perulangan interaktif (while loop & try-except)`, `Dictionary`, `Modul datetime (strptime, selisih hari)`, `Percabangan`, `Fungsi modular`.
* **Skenario Kasus**:
  Sistem pemesanan kamar hotel yang interaktif. Pelanggan memilih tipe kamar dari katalog yang disediakan, kemudian menginput tanggal check-in dan tanggal check-out. Program memiliki mekanisme validasi perulangan (`while True` dan `try-except`) yang memastikan pengguna memasukkan format tanggal yang benar (`YYYY-MM-DD`) dan tanggal check-out harus lebih besar dari check-in. Program kemudian mencetak rincian malam menginap dan total biaya.

### Listing Program:

```python
from datetime import datetime

# Katalog tipe kamar dan harga per malam
DAFTAR_KAMAR = {
    "1": {"tipe": "Standard Room", "harga": 300_000},
    "2": {"tipe": "Deluxe Room", "harga": 500_000},
    "3": {"tipe": "Suite Room", "harga": 950_000}
}

def tampilkan_katalog():
    print("\n" + "=" * 36)
    print("      PILIHAN TIPE KAMAR HOTEL      ")
    print("=" * 36)
    for kode, info in DAFTAR_KAMAR.items():
        print(f"[{kode}] {info['tipe']:<15} : Rp {info['harga']:>8,}/malam")
    print("-" * 36)

def proses_reservasi():
    tampilkan_katalog()
    pilihan = input("Pilih Kode Kamar (1/2/3): ").strip()
    
    if pilihan not in DAFTAR_KAMAR:
        print("❌ Pilihan kamar tidak valid!")
        return
        
    kamar_dipilih = DAFTAR_KAMAR[pilihan]
    format_tgl = "%Y-%m-%d"
    
    # Perulangan while untuk memvalidasi input tanggal
    while True:
        try:
            str_checkin = input("Masukkan Tanggal Check-in  (YYYY-MM-DD): ").strip()
            str_checkout = input("Masukkan Tanggal Check-out (YYYY-MM-DD): ").strip()
            
            tgl_in = datetime.strptime(str_checkin, format_tgl).date()
            tgl_out = datetime.strptime(str_checkout, format_tgl).date()
            
            if tgl_out <= tgl_in:
                print("⚠️ Tanggal check-out harus minimal 1 hari setelah check-in! Silakan input ulang.\n")
                continue
            break
        except ValueError:
            print("⚠️ Format tanggal keliru! Harap gunakan format YYYY-MM-DD (Contoh: 2026-10-25).\n")

    durasi_malam = (tgl_out - tgl_in).days
    total_biaya = durasi_malam * kamar_dipilih["harga"]
    
    print("\n" + "=" * 45)
    print("          BUKTI RESERVASI KAMAR HOTEL        ")
    print("=" * 45)
    print(f"Tipe Kamar       : {kamar_dipilih['tipe']}")
    print(f"Harga per Malam  : Rp {kamar_dipilih['harga']:,}")
    print(f"Tanggal Check-in : {tgl_in.strftime('%A, %d %B %Y')}")
    print(f"Tanggal Check-out: {tgl_out.strftime('%A, %d %B %Y')}")
    print(f"Durasi Menginap  : {durasi_malam} Malam")
    print("-" * 45)
    print(f"TOTAL TAGIHAN    : Rp {total_biaya:,}")
    print("=" * 45 + "\n")

if __name__ == "__main__":
    proses_reservasi()
```

::: tip 💡 Tugas Mahasiswa untuk Soal 5:
1. Jalankan kode program. Uji coba dengan memasukkan format yang salah terlebih dahulu (misal: `25-10-2026`) untuk melihat cara kerja error handling `try-except`, kemudian masukkan tanggal yang benar.
2. Screenshot seluruh interaksi terminal dari kesalahan input hingga struk reservasi berhasil dicetak.
3. Jelaskan alur kerja perulangan `while True`, perintah `continue`, dan perintah `break` dalam memvalidasi tanggal.
:::

---

[⬅️ Kembali ke Menu Utama](README.md)
