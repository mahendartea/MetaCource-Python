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
## 📏 7. Aturan & Konvensi Penamaan

Ada beberapa aturan penting dalam menulis nama variabel di Python:
1. Hanya boleh terdiri dari huruf (a-z, A-Z), angka (0-9), dan underscore (`_`).
2. Karakter pertama **harus** berupa huruf atau underscore (`_`). Tidak boleh dimulai dengan angka.
3. Bersifat *case-sensitive* (membedakan huruf besar dan kecil). Variabel `nama` berbeda dengan `Nama`.
4. Tidak boleh menggunakan spasi atau karakter spesial (seperti `@`, `#`, `$`, `%`, dll).
5. Tidak boleh menggunakan *Reserve Keyword* (kata kunci cadangan Python seperti `if`, `def`, `class`, dll).

**Contoh Penamaan Variabel yang BENAR (Diperbolehkan):**
```python
nama = "budiawan"
jabatan = "dosen"
nilai_tinggi = 170
nama1 = "budiawan rudi"
_luas = 100
```

**Contoh Penamaan Variabel yang SALAH (Memicu SyntaxError):**
```python
1nama = "budiawan"          # SALAH: Diawali angka
nama lengkap = "rudi"       # SALAH: Menggunakan spasi
nama@variable = "budiawan"  # SALAH: Menggunakan karakter spesial @
if = "aktif"                # SALAH: Menggunakan reserve keyword 'if'
```

## 🏷️ 8. Type Hinting (Python Modern)

Di Python modern (Python 3.5+), Anda dapat menuliskan tipe data variabel secara eksplisit sebagai petunjuk (*type hints*). Konsep ini sangat populer dalam pengembangan aplikasi skala besar karena membuat kode lebih mudah dibaca dan didukung oleh editor modern (seperti VS Code/Cursor).

**Cara penulisan Type Hinting:**
```python
nama_variabel: tipe_data = nilai
```

Contoh:
```python
nama: str = "Budi"
umur: int = 20
tinggi_badan: float = 170.5
is_active: bool = True
hobi: list = ["membaca", "coding"]
```
> **Catatan**: Type hinting bersifat opsional. Python tetap mendeteksi tipe data secara dinamis pada saat dijalankan (*runtime*), namun type hint sangat berguna untuk dokumentasi kode dan alat pengecek tipe data otomatis (seperti `mypy`).


## 🔢 9. Multi-variable

berikut contoh penggunaan multi-variable pada python:

```python
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)
```
## 🔍 10. Unpacking Multi-Value (Melihat semua isi variable)

Cara mengurai (*unpacking*) nilai dari list ke beberapa variabel di Python:

```python
fruit = ["apple", "banana", "orange"]
x, y, z = fruit
print(x)
print(y)
print(z)
```
[⬅️ Kembali ke Menu Utama](README.md)

