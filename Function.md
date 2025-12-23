<h1> 🛠️ Fungsi/Function </h1>

## 📖 1. Definisi
Fungsi digunakan untuk mengimplementasikan konsep modular(modularity) pada Python. Fungsi ini digunakan untuk menyelesaikan masalah pada program. Fungsi bertugas untuk menjalankan serangkaian perintah secara spesifik. Selama ini kita sudah menggunakan beberapa fungsi bawaan dari python `buldin function`, seperti `print()`, `input()`, `len()`, `append()`, dan lain-lain.
Namun kita dapat membuat fungsi sendiri sesuai kebutuhan. Fungsi yang kita buat sendiri disebut `user defined function`. Fungsi ini dapat digunakan pada program kita sendiri.

## 🏗️ 2. Membuat Fungsi
cara membuat fungsi pada python:
```python
def nama_fungsi(daftar_parameter):
    statement
    return [ekspresi]
```
keterangan:
- `def` : keyword untuk membuat fungsi
- `nama_fungsi` : nama fungsi yang ingin dibuat
- `:` : penanda akhir dari sebuah fungsi
- `daftar_parameter` : parameter yang digunakan pada fungsi
- `statement` : pernyataan yang akan dieksekusi pada fungsi
- `return` : keyword untuk mengembalikan sebuah fungsi
- `[ekspresi]` : ekspresi yang akan dikembalikan

Contoh:
```python
#membuat fungsi
def hello():
    print("Hello World!")
    return "Hello World!"
#memanggil fungsi
hello()
```

## 🔢 3. Fungsi dengan Parameter

Dalam `function` pada pemrograman python dapat menggunakan `parameter` sehingga saat pemanggilan `function` user dapat memberikan argument di dalamnya.

misalnya ada sebuah `function` untuk rumus persegi. Maka perlu ada parameter sisi yang diinputkan user.

Berikut adalah skema sintax pada function yang memilki parameter.

```python
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
```

Contoh penggunaan function pada rumus menghitung rumus segitiga adalah sebagai berikut

contoh 2: Menghitung luas segitiga

```python
def luas_segitiga(alas, tinggi):
    luas = alas * tinggi / 2
    return luas
luas = luas_segitiga(10, 5)
print(luas)
```

## 🎲 4. Arbitrary Arguments

Dalam `function` pada pemrograman python ada cara penggunaan `arbitrary arguments`. Arbitrary arguments adalah argument yang tidak didefinisikan sebelumnya. Artinya ketika kita tidak mengetahui parameter yang dapat diinput user, kita bisa menggunakan `arbitrary arguments`.

sintak `arbitrary arguments` adalah `*`

contoh:

```python
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
```

## 🔑 5. Arbitrary Argument Keyword, **

jika kita menggunakan `arbitrary arguments` pada function, kita juga bisa menggunakan `arbitrary arguments` pada `keyword arguments`

```python
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
```

## ⚙️ 6. Parameter Default

parameter default adalah parameter yang diinputkan secara otomatis ketika sebuah `function` dipanggil.

```python
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function()
my_function("India")
```

## 📜 7. Passing sebuah list sebagai argument

kita bisa memasukkan sebuah list sebagai argument pada sebuah `function`

```python
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
```

## 📝 8. Docstring

docstring adalah sebuah teks yang menunjukkan apa yang terlihat pada sebuah `function`. Docstring ini biasanya dituliskan pada `function` yang kita buat.

```python
def suhu_udara (daerah, derajat = 30, satuan = 'celcius'):
  """
  Fungsi ini bertugas untuk menampilkan teks yang memberikan informasi 
  tentang suhu udara di suatu daerah.
  """

  print("Suhu di {} adalah {} {}".format(daerah, derajat, satuan))
```

## 🏗️ Latihan
```python
def persentase (total, jumlah):
  if (total >= 0 and total <= jumlah):
    return total / jumlah * 100
  
  return False

# output 50
print(persentase(30, 60))

# output False
print(persentase(100, 60))
```

### 2. Latihan 2

```python
# membuat variabel global
nama = "Petani Kode"
versi = "1.0.0"

def help():
    # ini variabel lokal
    nama = "Programku"
    versi = "1.0.2"
    # mengakses variabel lokal
    print "Nama: %s" % nama
    print "Versi: %s" % versi


# mengakses variabel global
print "Nama: %s" % nama
print "Versi: %s" % versi

# memanggil fungsi help()
help()

```

### 3. Latihan 3

```python
buku = []
# fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print("Belum ada data")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))

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
        exit()
    else:
        print("Salah pilih!")

if __name__ == "__main__":
    while True:
        show_menu()
        show_menu()
```

[⬅️ Kembali ke Menu Utama](README.md)
