<h1> 📦 Variable </h1>

## 📖 1. Definisi

Pengenal (*identifier*) digunakan untuk memberikan nama seperti variabel.
Variable atau variabel adalah tempat untuk menyimpan nilai yang dapat diubah. Variabel dapat berisi nilai yang berbeda-beda tiap kali program dijalankan. Contoh: `a = 10`, `b = 20`, `c = 30`

## ✍️ 2. Penulisan

cara penulisan variable pada python:

```python
nama_variabel = nilai
```

contoh:

```python
a = 10
b = 20
c = 30
```

variable pada python tidak perlu di deklarasikan tipe data, karena python adalah bahasa pemrograman yang dinamis, artinya tipe data dapat berubah-ubah tiap kali program dijalankan. 
Contoh: 
`a = 10`, `a = "10"`, `a = [10, 20, 30]`, `a = (10, 20, 30)`, `a = {"key1": "value1", "key2": "value2"}`

## 🖨️ 3. Cara mencetak variable pada python:

berikut contoh penggunaan cara mencetak variable pada python yaitu dengan menggunakan `print()` yang sama seperti mencatak output pada BAB sebelumnya. Contohnya sebagai berikut:

```python
print(a)
```

## 🔄 4. Cara mengubah nilai variable pada python:

berikut contoh penggunaan cara mengubah nilai variable pada python yaitu dengan menggunakan `=`. Contohnya sebagai berikut:

```python
a = 10
a = 20
print(a)
```
## 🧬 5. Cara mengubah tipe data variable pada python:

berikut contoh penggunaan cara mengubah tipe data variable pada python yaitu dengan menggunakan `type()`. Contohnya sebagai berikut:

```python
a = 10
a = "10"
print(type(a))
```
## 🛠️ 6. Casting

Casting adalah proses mengubah tipe data dari satu tipe ke tipe data yang lain. Contoh: `int(a)`, `float(a)`, `str(a)`

contoh casting :
```python
a = 10
a = float(a)
print(type(a))
```
## 📏 7. Konvensi

1. Nama variable tidak boleh mengandung spasi, harus menggunakan underscore (`_`) sebagai pemisah antar kata. Contoh: `nama_variable`
2. Nama variable tidak boleh mengandung karakter spesial, kecuali underscore (`_`). Contoh: `nama_variable`, `nama@variable`, `nama#variable`, `nama$variable`

Contoh penamaan variable yang boleh seperti berikut
```python
nama = "budiawan"
jabatan = "dosen"
nilai_tinggi = 170
nama1 = "budiawan rudi"
_luas = 100
nama@variable = "budiawan rudi"
```

## 🔢 8. Multi-variable

berikut contoh penggunaan multi-variable pada python:

```python
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)
```
## 🔍 9. Melihat semua isi variable pada multiple value

Cara melihat semua isi variable pada multiple value pada python:

```python
fruit = ["apple", "banana", "orange"]
x, y, z = fruit
print(x)
print(y)
print(z)
```
[⬅️ Kembali ke Menu Utama](README.md)

