<h1> ⌨️ Input & Output </h1>

## 📥 1.1 Input

### 1.1.1 Input dari User

Untuk membuat input user dapat menggunakan fungsi `input()`. Fungsi ini akan mengambil input dari user dan mengembalikan nilai inputnya.

```python
input()
```

contoh dari penggunakan input dari user

```python
nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}!")
```

Contoh lain penggunaan input 

```python
nim = str(input("Masukan NIM \t:"))
nama = str(input("Masukan Nama \t:"))
uts = int(input("Masukan Nilai UTS \t:"))
tugas = int(input("Masukan nilai tugas\t:"))
uas = int(input("Masukan Nilai UAS \t:"))
```

Contoh kasus lain 
```python
nim = int(input("Masukan Nomor Induk Mahasiswa : "))
nama = str(input("Masukan Nama Mahasiswa: "))
uts = float(input("Masukan nilai UTS: "))
tugas = float(input("Masukan nilai Tugas: "))
uas = float(input("Masukan nilai UAS: "))
hasil = ((uts*0.3) + (tugas*0.2) + (uas*0.5))


```

## 📤 1.2 Output

### 1.2.1 Output ke layar

Untuk menampilkan output ke layar dapat menggunakan fungsi `print()`. Fungsi ini akan menampilkan output yang diberikan.

```python
print("Hello, World!")
```

contoh lain penggunaan output ke layar

```python
print("Nomor induk mahasiswa : ", nim)
print("Nama lengkap mahasiswa : ", nama)
print("nilai UTS : ", uts)
print("Nilai tugas : ", tugas)
print("Nilai Uas : ", uas)
print("Hasil akhir nilai mahasiswa adalah : ",hasil)
```
## 📁 1.3 Input & Output pada File

### 1.3.1 Input dari File

Untuk mengambil input dari file dapat menggunakan fungsi `open()`. Fungsi ini akan membuka file yang diberikan dan mengembalikan objek file.

```python
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
```

### 1.3.2 Output ke File

Untuk menampilkan output ke file dapat menggunakan fungsi `open()`. Fungsi ini akan membuka file yang diberikan dan mengembalikan objek file.

```python
with open('file.txt', 'w') as file:
    file.write('Hello, World!')
    print("Data telah ditambahkan")
```

## 🗄️ 1.4 Input & Output pada Database

### 1.4.1 Input dari Database

Untuk mengambil input dari database dapat menggunakan fungsi `open()`. Fungsi ini akan membuka database yang diberikan dan mengembalikan objek database.

```python
with open('database.db', 'r') as database:
    content = database.read()
    print(content)
```

## 📝 Latihan
### 1. Input dan Output Karyawan dan Gaji

```python
nama = str(input("Masukkan Nama Karyawan \t:"))
gaji = int(input("Masukkan Gaji Karyawan \t:"))
print("Nama Karyawan \t:", nama)
print("Gaji Karyawan \t: {:,.2f}".format(gaji))
tunjangan = gaji * 0.1
print("Tunjangan Karyawan \t: {:,.2f}".format(tunjangan))
pajak = gaji * 0.15
print("Pajak Karyawan \t: {:,.2f}".format(pajak))
gaji_bersih = gaji + tunjangan - pajak
print("Gaji Bersih Karyawan \t: {:,.2f}".format(gaji_bersih))

```
### 2. Input dan Output Nilai
```python
nama = str(input("Masukkan Nama \t:"))
nilai = int(input("Masukkan Nilai \t:"))
print("Nama \t:", nama)
print("Nilai \t:", nilai)
```

### 3. Mencari Luas Segitiga

```python
alas = int(input("Masukkan Alas \t:"))
tinggi = int(input("Masukkan Tinggi \t:"))
luas = alas * tinggi / 2
print("Luas Segitiga \t:", luas)
```

### 4. Konversi celcius ke kelvin
```python
celcius = int(input("Masukkan Nilai Celcius \t:"))
kelvin = celcius + 273
print("Nilai Kelvin \t:", kelvin)
```

[⬅️ Kembali ke Menu Utama](README.md)