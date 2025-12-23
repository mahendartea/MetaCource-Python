"""
Aplikasi Manajemen Siswa Sederhana
Menggunakan SQLite Database

Fitur:
1. Tambah siswa baru
2. Lihat semua siswa
3. Cari siswa berdasarkan nama
4. Update nilai siswa
5. Hapus siswa
"""

import sqlite3
import os

class DatabaseSiswa:
    def __init__(self, db_name='sekolah.db'):
        """Inisialisasi koneksi database"""
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect()
        self.buat_tabel()
    
    def connect(self):
        """Membuat koneksi ke database"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"✅ Koneksi ke database '{self.db_name}' berhasil!")
        except sqlite3.Error as e:
            print(f"❌ Error koneksi database: {e}")
    
    def buat_tabel(self):
        """Membuat tabel siswa jika belum ada"""
        try:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS siswa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL,
                kelas TEXT NOT NULL,
                nilai INTEGER NOT NULL,
                tanggal_daftar TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"❌ Error membuat tabel: {e}")
    
    def tambah_siswa(self, nama, kelas, nilai):
        """Menambahkan siswa baru"""
        try:
            self.cursor.execute('''
            INSERT INTO siswa (nama, kelas, nilai) 
            VALUES (?, ?, ?)
            ''', (nama, kelas, nilai))
            self.conn.commit()
            print(f"✅ Siswa '{nama}' berhasil ditambahkan!")
            return True
        except sqlite3.Error as e:
            print(f"❌ Error menambah siswa: {e}")
            return False
    
    def lihat_semua_siswa(self):
        """Menampilkan semua siswa"""
        try:
            self.cursor.execute('SELECT * FROM siswa ORDER BY nilai DESC')
            siswa_list = self.cursor.fetchall()
            
            if not siswa_list:
                print("\n📭 Belum ada data siswa.")
                return
            
            print("\n" + "="*70)
            print(f"{'ID':<5} {'Nama':<20} {'Kelas':<10} {'Nilai':<10} {'Tanggal Daftar':<20}")
            print("="*70)
            
            for siswa in siswa_list:
                print(f"{siswa[0]:<5} {siswa[1]:<20} {siswa[2]:<10} {siswa[3]:<10} {siswa[4]:<20}")
            
            print("="*70)
            print(f"Total: {len(siswa_list)} siswa\n")
            
        except sqlite3.Error as e:
            print(f"❌ Error mengambil data: {e}")
    
    def cari_siswa(self, nama):
        """Mencari siswa berdasarkan nama"""
        try:
            self.cursor.execute('''
            SELECT * FROM siswa 
            WHERE nama LIKE ?
            ''', (f'%{nama}%',))
            
            hasil = self.cursor.fetchall()
            
            if not hasil:
                print(f"\n❌ Siswa dengan nama '{nama}' tidak ditemukan.")
                return
            
            print("\n" + "="*70)
            print(f"{'ID':<5} {'Nama':<20} {'Kelas':<10} {'Nilai':<10}")
            print("="*70)
            
            for siswa in hasil:
                print(f"{siswa[0]:<5} {siswa[1]:<20} {siswa[2]:<10} {siswa[3]:<10}")
            
            print("="*70 + "\n")
            
        except sqlite3.Error as e:
            print(f"❌ Error mencari siswa: {e}")
    
    def update_nilai(self, id_siswa, nilai_baru):
        """Update nilai siswa berdasarkan ID"""
        try:
            # Cek apakah siswa ada
            self.cursor.execute('SELECT nama FROM siswa WHERE id = ?', (id_siswa,))
            siswa = self.cursor.fetchone()
            
            if not siswa:
                print(f"❌ Siswa dengan ID {id_siswa} tidak ditemukan.")
                return False
            
            self.cursor.execute('''
            UPDATE siswa 
            SET nilai = ? 
            WHERE id = ?
            ''', (nilai_baru, id_siswa))
            
            self.conn.commit()
            print(f"✅ Nilai siswa '{siswa[0]}' berhasil diupdate menjadi {nilai_baru}!")
            return True
            
        except sqlite3.Error as e:
            print(f"❌ Error update nilai: {e}")
            return False
    
    def hapus_siswa(self, id_siswa):
        """Menghapus siswa berdasarkan ID"""
        try:
            # Cek apakah siswa ada
            self.cursor.execute('SELECT nama FROM siswa WHERE id = ?', (id_siswa,))
            siswa = self.cursor.fetchone()
            
            if not siswa:
                print(f"❌ Siswa dengan ID {id_siswa} tidak ditemukan.")
                return False
            
            self.cursor.execute('DELETE FROM siswa WHERE id = ?', (id_siswa,))
            self.conn.commit()
            print(f"✅ Siswa '{siswa[0]}' berhasil dihapus!")
            return True
            
        except sqlite3.Error as e:
            print(f"❌ Error menghapus siswa: {e}")
            return False
    
    def statistik(self):
        """Menampilkan statistik data siswa"""
        try:
            self.cursor.execute('''
            SELECT 
                COUNT(*) as total,
                AVG(nilai) as rata_rata,
                MAX(nilai) as nilai_tertinggi,
                MIN(nilai) as nilai_terendah
            FROM siswa
            ''')
            
            stats = self.cursor.fetchone()
            
            if stats[0] == 0:
                print("\n📭 Belum ada data untuk statistik.")
                return
            
            print("\n" + "="*50)
            print("📊 STATISTIK DATA SISWA")
            print("="*50)
            print(f"Total Siswa       : {stats[0]}")
            print(f"Rata-rata Nilai   : {stats[1]:.2f}")
            print(f"Nilai Tertinggi   : {stats[2]}")
            print(f"Nilai Terendah    : {stats[3]}")
            print("="*50 + "\n")
            
        except sqlite3.Error as e:
            print(f"❌ Error mengambil statistik: {e}")
    
    def close(self):
        """Menutup koneksi database"""
        if self.conn:
            self.conn.close()
            print("✅ Koneksi database ditutup.")


def clear_screen():
    """Membersihkan layar terminal"""
    os.system('clear' if os.name == 'posix' else 'cls')


def tampilkan_menu():
    """Menampilkan menu utama"""
    print("\n" + "="*50)
    print("🎓 APLIKASI MANAJEMEN DATA SISWA")
    print("="*50)
    print("1. Tambah Siswa Baru")
    print("2. Lihat Semua Siswa")
    print("3. Cari Siswa")
    print("4. Update Nilai Siswa")
    print("5. Hapus Siswa")
    print("6. Lihat Statistik")
    print("0. Keluar")
    print("="*50)


def main():
    """Fungsi utama aplikasi"""
    db = DatabaseSiswa()
    
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu (0-6): ").strip()
        
        if pilihan == '1':
            print("\n--- TAMBAH SISWA BARU ---")
            nama = input("Nama: ").strip()
            kelas = input("Kelas: ").strip()
            
            try:
                nilai = int(input("Nilai: ").strip())
                if 0 <= nilai <= 100:
                    db.tambah_siswa(nama, kelas, nilai)
                else:
                    print("❌ Nilai harus antara 0-100!")
            except ValueError:
                print("❌ Nilai harus berupa angka!")
        
        elif pilihan == '2':
            db.lihat_semua_siswa()
        
        elif pilihan == '3':
            nama = input("\nMasukkan nama yang dicari: ").strip()
            db.cari_siswa(nama)
        
        elif pilihan == '4':
            try:
                id_siswa = int(input("\nMasukkan ID siswa: ").strip())
                nilai_baru = int(input("Nilai baru (0-100): ").strip())
                
                if 0 <= nilai_baru <= 100:
                    db.update_nilai(id_siswa, nilai_baru)
                else:
                    print("❌ Nilai harus antara 0-100!")
            except ValueError:
                print("❌ Input harus berupa angka!")
        
        elif pilihan == '5':
            try:
                id_siswa = int(input("\nMasukkan ID siswa yang akan dihapus: ").strip())
                konfirmasi = input(f"Yakin ingin menghapus siswa ID {id_siswa}? (y/n): ").strip().lower()
                
                if konfirmasi == 'y':
                    db.hapus_siswa(id_siswa)
            except ValueError:
                print("❌ ID harus berupa angka!")
        
        elif pilihan == '6':
            db.statistik()
        
        elif pilihan == '0':
            print("\n👋 Terima kasih telah menggunakan aplikasi ini!")
            db.close()
            break
        
        else:
            print("❌ Pilihan tidak valid!")
        
        input("\nTekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()
