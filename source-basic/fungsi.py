buku = []
# fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print("Belum ada data")
    else:
        for indeks in range(len(buku)):
            print(f"[{indeks}] {buku[indeks]}")

# fungsi untuk menambahkan data
def tambah_buku():
    buku_baru = input("BUKU BARU : ")
    buku.append(buku_baru)
    print("DATA BERHASIL DISIMPAN")

# fungsi untuk edit data
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if indeks >= len(buku):
        print("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru
        print("DATA BERHASIL DIUPDATE")

# fungsi untuk menghapus data
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if indeks >= len(buku):
        print("ID salah")
    else:
        del buku[indeks]

def show_menu():
    print("\n")
    print("----------- MENU ----------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    
    menu = int(input("PILIH MENU> "))
    print("\n")

    if menu == 1:
        show_data()
    elif menu == 2:
        tambah_buku()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        return False
    else:
        print("Salah pilih!")
    return True

if __name__ == "__main__":
    while True:
        running = show_menu()
        if not running:
            print("Terima kasih!")
            break