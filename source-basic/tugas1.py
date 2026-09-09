"""
Tugas Mandiri Pemrograman Python (Pertemuan 1 - 10)
Berisi 5 Soal Terstruktur Mengintegrasikan:
Variabel, Input/Output, Tipe Data, String, Operasi, Percabangan, Perulangan, Fungsi, Modul, dan Datetime.
"""

import datetime
from datetime import date, time


# ==============================================================================
# SOAL 1: Sistem Rental Mobil & Penghitung Denda Keterlambatan
# ==============================================================================
def soal_1():
    print("\n" + "=" * 50)
    print("SOAL 1: RENTAL MOBIL & PENGHITUNG DENDA")
    print("=" * 50)

    def hitung_rental(nama_penyewa: str, tgl_kembali_rencana: str, tgl_kembali_real: str, tarif_per_hari: int, denda_per_hari: int):
        format_tgl = "%Y-%m-%d"
        tgl_rencana = datetime.datetime.strptime(tgl_kembali_rencana.strip(), format_tgl).date()
        tgl_kembali = datetime.datetime.strptime(tgl_kembali_real.strip(), format_tgl).date()
        
        print("\n" + "=" * 45)
        print("        STRUK PENGEMBALIAN RENTAL MOBIL      ")
        print("=" * 45)
        print(f"Nama Penyewa         : {nama_penyewa.upper()}")
        print(f"Batas Pengembalian   : {tgl_rencana.strftime('%d %B %Y')}")
        print(f"Tanggal Dikembalikan : {tgl_kembali.strftime('%d %B %Y')}")
        print("-" * 45)
        
        if tgl_kembali > tgl_rencana:
            hari_terlambat = (tgl_kembali - tgl_rencana).days
            total_denda = hari_terlambat * denda_per_hari
            status = f"TERLAMBAT ({hari_terlambat} Hari)"
        else:
            total_denda = 0
            status = "TEPAT WAKTU (Bebas Denda)"
            
        print(f"Status Pengembalian  : {status}")
        print(f"Total Biaya Denda    : Rp {total_denda:,.2f}")
        print("=" * 45 + "\n")

    nama = input("Masukkan Nama Penyewa                      : ")
    tgl_target = input("Masukkan Tanggal Tenggat Kembali (YYYY-MM-DD) : ")
    tgl_aktual = input("Masukkan Tanggal Pengembalian Nyata (YYYY-MM-DD): ")
    hitung_rental(nama, tgl_target, tgl_aktual, 350_000, 50_000)


# ==============================================================================
# SOAL 2: Kasir Minimarket & Cetak Struk dengan Stempel Waktu
# ==============================================================================
def soal_2():
    print("\n" + "=" * 50)
    print("SOAL 2: KASIR DENGAN TIMESTAMP REAL-TIME")
    print("=" * 50)

    def cetak_struk(kasir: str, daftar_belanja: list, is_member: bool):
        waktu_transaksi = datetime.datetime.now()
        format_waktu = waktu_transaksi.strftime("%A, %d-%m-%Y %H:%M:%S")
        
        subtotal = 0
        print("\n" + "-" * 42)
        print("           TOKO SERBA ADA MODERN          ")
        print(f"Waktu Transaksi : {format_waktu}")
        print(f"Kasir           : {kasir.title()}")
        print("-" * 42)
        
        for item in daftar_belanja:
            nama_barang = item["nama"]
            harga = item["harga"]
            qty = item["qty"]
            total_item = harga * qty
            subtotal += total_item
            print(f"{nama_barang:<18} x{qty:<2} : Rp {total_item:>9,}")
            
        print("-" * 42)
        print(f"Subtotal             : Rp {subtotal:>9,}")
        
        diskon = 0.1 * subtotal if (is_member and subtotal >= 100_000) else 0.0
        total_bayar = subtotal - diskon
        
        print(f"Diskon Member (10%)  : Rp {int(diskon):>9,}")
        print(f"TOTAL AKHIR          : Rp {int(total_bayar):>9,}")
        print("-" * 42)
        print("      Terima Kasih Telah Berbelanja!      \n")

    keranjang = [
        {"nama": "Kopi Susu Botol", "harga": 15000, "qty": 3},
        {"nama": "Roti Gandum", "harga": 22000, "qty": 2},
        {"nama": "Minyak Goreng 2L", "harga": 34000, "qty": 2},
    ]
    nama_kasir = input("Masukkan Nama Kasir                          : ")
    member_input = input("Apakah pelanggan memiliki Member Card? (y/t) : ").strip().lower()
    cetak_struk(nama_kasir, keranjang, (member_input == 'y'))


# ==============================================================================
# SOAL 3: Presensi Karyawan & Deteksi Menit Keterlambatan
# ==============================================================================
def soal_3():
    print("\n" + "=" * 50)
    print("SOAL 3: PRESENSI & DETEKSI KETERLAMBATAN")
    print("=" * 50)

    def validasi_presensi(nama_karyawan: str, jam_masuk_str: str):
        batas_masuk = time(8, 0, 0)
        jam_input = datetime.datetime.strptime(jam_masuk_str.strip(), "%H:%M").time()
        
        tgl_dummy = datetime.datetime(2026, 1, 1)
        dt_input = datetime.datetime.combine(tgl_dummy, jam_input)
        dt_batas = datetime.datetime.combine(tgl_dummy, batas_masuk)
        
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

    nama = input("Masukkan Nama Pegawai                             : ")
    jam_hadir = input("Masukkan Jam Hadir (Format HH:MM contoh: 08:25) : ")
    validasi_presensi(nama, jam_hadir)


# ==============================================================================
# SOAL 4: Kalkulator Usia Lengkap & Hitung Mundur Ulang Tahun
# ==============================================================================
def soal_4():
    print("\n" + "=" * 50)
    print("SOAL 4: KALKULATOR USIA & HITUNG MUNDUR ULTAH")
    print("=" * 50)

    def kalkulator_umur(nama: str, tahun_lahir: int, bulan_lahir: int, tgl_lahir: int):
        hari_ini = date.today()
        tgl_kelahiran = date(tahun_lahir, bulan_lahir, tgl_lahir)
        
        total_hari_hidup = (hari_ini - tgl_kelahiran).days
        usia_tahun = hari_ini.year - tgl_kelahiran.year - (
            (hari_ini.month, hari_ini.day) < (tgl_kelahiran.month, tgl_kelahiran.day)
        )
        
        tahun_ultah_berikut = hari_ini.year
        target_ultah = date(tahun_ultah_berikut, bulan_lahir, tgl_lahir)
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

    nama_user = input("Masukkan Nama Anda              : ")
    thn = int(input("Masukkan Tahun Lahir (YYYY)     : "))
    bln = int(input("Masukkan Bulan Lahir (1-12)     : "))
    tgl = int(input("Masukkan Tanggal Lahir (1-31)   : "))
    kalkulator_umur(nama_user, thn, bln, tgl)


# ==============================================================================
# SOAL 5: Reservasi Kamar Hotel & Validasi Tanggal Menginap
# ==============================================================================
def soal_5():
    print("\n" + "=" * 50)
    print("SOAL 5: RESERVASI KAMAR HOTEL INTERAKTIF")
    print("=" * 50)

    DAFTAR_KAMAR = {
        "1": {"tipe": "Standard Room", "harga": 300_000},
        "2": {"tipe": "Deluxe Room", "harga": 500_000},
        "3": {"tipe": "Suite Room", "harga": 950_000}
    }

    print("\n" + "=" * 36)
    print("      PILIHAN TIPE KAMAR HOTEL      ")
    print("=" * 36)
    for kode, info in DAFTAR_KAMAR.items():
        print(f"[{kode}] {info['tipe']:<15} : Rp {info['harga']:>8,}/malam")
    print("-" * 36)

    pilihan = input("Pilih Kode Kamar (1/2/3): ").strip()
    if pilihan not in DAFTAR_KAMAR:
        print("❌ Pilihan kamar tidak valid!")
        return
        
    kamar_dipilih = DAFTAR_KAMAR[pilihan]
    format_tgl = "%Y-%m-%d"
    
    while True:
        try:
            str_checkin = input("Masukkan Tanggal Check-in  (YYYY-MM-DD): ").strip()
            str_checkout = input("Masukkan Tanggal Check-out (YYYY-MM-DD): ").strip()
            
            tgl_in = datetime.datetime.strptime(str_checkin, format_tgl).date()
            tgl_out = datetime.datetime.strptime(str_checkout, format_tgl).date()
            
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


# ==============================================================================
# MENU UTAMA
# ==============================================================================
if __name__ == "__main__":
    while True:
        print("\n" + "=" * 50)
        print("   MENU TUGAS MANDIRI PEMROGRAMAN PYTHON (1-10)   ")
        print("=" * 50)
        print("[1] Soal 1: Rental Mobil & Penghitung Denda")
        print("[2] Soal 2: Kasir Minimarket dengan Timestamp")
        print("[3] Soal 3: Presensi Karyawan & Deteksi Keterlambatan")
        print("[4] Soal 4: Kalkulator Usia & Hitung Mundur Ultah")
        print("[5] Soal 5: Reservasi Kamar Hotel Interaktif")
        print("[0] Keluar")
        print("=" * 50)
        
        pilih = input("Pilih nomor soal yang ingin diuji (0-5): ").strip()
        if pilih == "1":
            soal_1()
        elif pilih == "2":
            soal_2()
        elif pilih == "3":
            soal_3()
        elif pilih == "4":
            soal_4()
        elif pilih == "5":
            soal_5()
        elif pilih == "0":
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi!")
