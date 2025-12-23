"""
Contoh Dasar Operasi Database SQLite
File ini berisi contoh-contoh sederhana untuk belajar database
"""

import sqlite3

def contoh_1_koneksi_database():
    """Contoh membuat koneksi dan database"""
    print("\n=== CONTOH 1: Koneksi Database ===")
    
    # Membuat koneksi (file akan dibuat jika belum ada)
    conn = sqlite3.connect('belajar.db')
    cursor = conn.cursor()
    
    print("✅ Database 'belajar.db' berhasil dibuat/dibuka!")
    
    # Tutup koneksi
    conn.close()


def contoh_2_buat_tabel():
    """Contoh membuat tabel"""
    print("\n=== CONTOH 2: Membuat Tabel ===")
    
    conn = sqlite3.connect('belajar.db')
    cursor = conn.cursor()
    
    # Membuat tabel mahasiswa
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mahasiswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nim TEXT UNIQUE NOT NULL,
        nama TEXT NOT NULL,
        jurusan TEXT,
        ipk REAL
    )
    ''')
    
    conn.commit()
    print("✅ Tabel 'mahasiswa' berhasil dibuat!")
    
    conn.close()


def contoh_3_insert_data():
    """Contoh menambahkan data"""
    print("\n=== CONTOH 3: Menambahkan Data ===")
    
    conn = sqlite3.connect('belajar.db')
    cursor = conn.cursor()
    
    # Insert satu data
    cursor.execute('''
    INSERT INTO mahasiswa (nim, nama, jurusan, ipk) 
    VALUES (?, ?, ?, ?)
    ''', ('2301001', 'Andi Pratama', 'Informatika', 3.75))
    
    # Insert banyak data sekaligus
    data_mahasiswa = [
        ('2301002', 'Budi Santoso', 'Sistem Informasi', 3.50),
        ('2301003', 'Citra Dewi', 'Informatika', 3.85),
        ('2301004', 'Dedi Kurniawan', 'Teknik Komputer', 3.60)
    ]
    
    cursor.executemany('''
    INSERT INTO mahasiswa (nim, nama, jurusan, ipk) 
    VALUES (?, ?, ?, ?)
    ''', data_mahasiswa)
    
    conn.commit()
    print(f"✅ {cursor.rowcount + 1} data mahasiswa berhasil ditambahkan!")
    
    conn.close()


def contoh_4_select_data():
    """Contoh mengambil data"""
    print("\n=== CONTOH 4: Mengambil Data ===")
    
    conn = sqlite3.connect('belajar.db')
    cursor = conn.cursor()
    
    # Mengambil semua data
    print("\n📋 Semua Mahasiswa:")
    cursor.execute('SELECT * FROM mahasiswa')
    semua = cursor.fetchall()
    
    for mhs in semua:
        print(f"NIM: {mhs[1]}, Nama: {mhs[2]}, Jurusan: {mhs[3]}, IPK: {mhs[4]}")
    
    # Mengambil dengan kondisi
    print("\n🏆 Mahasiswa dengan IPK >= 3.7:")
    cursor.execute('SELECT nama, ipk FROM mahasiswa WHERE ipk >= ?', (3.7,))
    mahasiswa_terbaik = cursor.fetchall()
    
    for mhs in mahasiswa_terbaik:
        print(f"- {mhs[0]} (IPK: {mhs[1]})")
    
    conn.close()


def contoh_5_update_data():
    """Contoh mengupdate data"""
    print("\n=== CONTOH 5: Update Data ===")
    
    conn = sqlite3.connect('belajar.db')
    cursor = conn.cursor()
    
    # Update IPK mahasiswa
    cursor.execute('''
    UPDATE mahasiswa 
    SET ipk = ? 
    WHERE nim = ?
    ''', (3.90, '2301001'))
    
    conn.commit()
    print(f"✅ {cursor.rowcount} data berhasil diupdate!")
    
    # Lihat hasil update
    cursor.execute('SELECT nama, ipk FROM mahasiswa WHERE nim = ?', ('2301001',))
    hasil = cursor.fetchone()
    print(f"IPK baru {hasil[0]}: {hasil[1]}")
    
    conn.close()


def contoh_6_delete_data():
    """Contoh menghapus data"""
    print("\n=== CONTOH 6: Menghapus Data ===")
    
    conn = sqlite3.connect('belajar.db')
    cursor = conn.cursor()
    
    # Hapus mahasiswa dengan IPK < 3.5
    cursor.execute('DELETE FROM mahasiswa WHERE ipk < ?', (3.5,))
    
    conn.commit()
    print(f"✅ {cursor.rowcount} data berhasil dihapus!")
    
    conn.close()


def contoh_7_agregasi():
    """Contoh fungsi agregasi (COUNT, AVG, MAX, MIN)"""
    print("\n=== CONTOH 7: Fungsi Agregasi ===")
    
    conn = sqlite3.connect('belajar.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT 
        COUNT(*) as total,
        AVG(ipk) as rata_rata,
        MAX(ipk) as tertinggi,
        MIN(ipk) as terendah
    FROM mahasiswa
    ''')
    
    stats = cursor.fetchone()
    
    print(f"Total Mahasiswa: {stats[0]}")
    print(f"IPK Rata-rata: {stats[1]:.2f}")
    print(f"IPK Tertinggi: {stats[2]}")
    print(f"IPK Terendah: {stats[3]}")
    
    conn.close()


def contoh_8_context_manager():
    """Contoh menggunakan context manager (with)"""
    print("\n=== CONTOH 8: Context Manager ===")
    
    # Dengan context manager, tidak perlu manual close()
    with sqlite3.connect('belajar.db') as conn:
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM mahasiswa')
        total = cursor.fetchone()[0]
        
        print(f"✅ Total mahasiswa: {total}")
        # conn.commit() otomatis dipanggil
    # conn.close() otomatis dipanggil


def reset_database():
    """Menghapus tabel untuk reset"""
    conn = sqlite3.connect('belajar.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS mahasiswa')
    conn.commit()
    conn.close()
    print("🔄 Database direset!")


def main():
    """Menjalankan semua contoh"""
    print("="*60)
    print("📚 TUTORIAL DATABASE SQLite - CONTOH DASAR")
    print("="*60)
    
    # Reset database untuk memulai dari awal
    reset_database()
    
    # Jalankan semua contoh
    contoh_1_koneksi_database()
    contoh_2_buat_tabel()
    contoh_3_insert_data()
    contoh_4_select_data()
    contoh_5_update_data()
    contoh_4_select_data()  # Lihat data setelah update
    contoh_7_agregasi()
    contoh_8_context_manager()
    
    print("\n" + "="*60)
    print("✅ Semua contoh berhasil dijalankan!")
    print("="*60)


if __name__ == "__main__":
    main()
