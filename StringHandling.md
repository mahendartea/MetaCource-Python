# 📝 String Handling

## 📑 1. Multiline String

Multiline string adalah string yang terdiri dari beberapa baris. Contoh:

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

bisa juga dengan menggunakan satu quotes
```python
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
```

## 🔪 2. Slicing

Slicing adalah operasi yang digunakan untuk mengambil bagian dari sebuah string. Contoh:

```python
b = "Hello, World!"
print(b[2:5])
```
> contoh diatas mengambil bagian dari posisi karakter `2` sampai `5` 

### 2.1 Slicing dari awal

```python
a = "Hello, World!"
print(a[:5])
```
> contoh diatas mengambil bagian dari posisi karakter `0` sampai `5`

### 2.2 Slicing dari akhir

```python
a = "Hello, World!"
print(a[2:])
```
> contoh diatas mengambil bagian dari posisi karakter `2` sampai akhir

### 2.3 Slicing dengan interval

```python
a = "Hello, World!"
print(a[2:5])
```
> contoh diatas mengambil bagian dari posisi karakter `2` sampai `5`

### 2.4 Negative Index

```python
a = "Hello, World!"
print(a[-5:-2])
```
> contoh diatas mengambil bagian dari posisi karakter `-5` sampai `-2`

## 🛠️ 3. Modifikasi String

### 3.1 Uppercase

```python
a = "Hello, World!"
print(a.upper())
```
> contoh diatas mengubah semua karakter menjadi huruf kapital

### 3.2 Lowercase

```python
a = "Hello, World!"
print(a.lower())
```
> contoh diatas mengubah semua karakter menjadi huruf kecil

### 3.3 Capitalize

```python
a = "hello, world!"
print(a.capitalize())
```
> contoh diatas mengubah karakter pertama menjadi huruf kapital

### 3.4 Remove whitespace

```python
a = " Hello, World! "
print(a.strip())
```
> contoh diatas menghilangkan whitespace di awal dan akhir

### 3.5 Split

```python
a = "Hello, World!"
print(a.split(","))
```
> contoh diatas memecah string berdasarkan pemisah koma `,` menjadi objek **list** dan mengembalikan: `['Hello', ' World!']`

### 3.6 Concatenation

```python
a = "Hello"
b = "World"
print(a + " " + b)

```
```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)
```
> contoh diatas menggabungkan dua string

### 3.7 Format String

```python
age = 36
txt = "My name is John, I am {}"
print(txt.format(age))
```
> contoh diatas format string

### 3.8 F string

```python
age = 36
txt = f"My name is John, I am {age}"
print(txt)
```

> **Modern F-String (Python 3.8+)**: Kita dapat menggunakan tanda `=` di dalam f-string untuk mencetak nama variabel sekaligus nilainya secara otomatis (sangat berguna untuk debugging).
> ```python
> x = 10
> print(f"{x=}")  # Output: x=10
> ```
> 
> **F-String Lanjutan (Python 3.12+)**: Di Python 3.12+, f-string kini mendukung tanda kutip yang sama di dalam ekspresi, baris baru (*newline*), komentar, dan karakter backslash secara langsung di dalam kurung kurawal `{}`.
### 3.9 Placeholder dan Modifier

```python
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
```

### 3.10 Escape Character

escape character pada string terdapat beberapa caranya yaitu 

| Character | Description |
|-----------|-------------|
| \n | new line |
| \t | tab |
| \\ | backslash |
| \' | single quote |
| \" | double quote |

contoh adalah sebagai berikut
```python
txt = "We are the so-called \"Vikings\" from the north."
```

## ⛓️ 4. String Method

Terdapat beberapa function bawaan python yang dapat digunakan pada string

| Function | Description |
|----------|-------------|
|capitalize() | capitalize string |
|upper() | convert string to uppercase |
|lower() | convert string to lowercase |
|strip() | remove whitespace |
|split() | split string into list |
|join() | join list into string |
|replace() | replace string |
|format() | format string |
|format_map() | format string |
|zfill() | fill string with zeros |
|len() | get length of string |
|dan lain-lain |    

Liat link berikut untuk selengkapnya : [link](https://www.w3schools.com/python/python_strings_methods.asp)

---

## 📝 Latihan

Berikut adalah beberapa latihan untuk menguji pemahaman Anda tentang manipulasi string di Python.

### 1. Format Biodata Sederhana
Buatlah program yang meminta input nama, pekerjaan, dan kota asal dari pengguna, lalu cetak kalimat perkenalan terformat menggunakan **f-string**.

```python
nama = input("Masukkan Nama: ")
pekerjaan = input("Masukkan Pekerjaan: ")
kota = input("Masukkan Kota Asal: ")

# Output terformat menggunakan f-string
print(f"Halo, saya {nama}. Saya bekerja sebagai {pekerjaan} dan berasal dari {kota}.")
```

### 2. Validasi & Pembersihan Email
Buatlah program yang membersihkan input email dari spasi di awal/akhir, mengubahnya menjadi huruf kecil semua, lalu memeriksa apakah email tersebut menggunakan domain `@gmail.com`.

```python
email = input("Masukkan email Anda: ")
# Hapus spasi di awal/akhir dan ubah jadi huruf kecil
email_bersih = email.strip().lower()

print(f"Email setelah dibersihkan: {email_bersih}")
# Cek apakah email mengandung domain '@gmail.com'
apakah_gmail = "@gmail.com" in email_bersih
print(f"Apakah ini akun Gmail? {apakah_gmail}")
```

### 3. Slicing & Sensor Kata (Replace)
Diberikan sebuah string `"Belajar Python sangat menyenangkan dan seru!"`. Buatlah program untuk:
1. Mengambil kata pertama (`"Belajar"`) menggunakan teknik **Slicing**.
2. Mengganti kata `"menyenangkan"` menjadi kata sensor `"***********"`.

```python
kalimat = "Belajar Python sangat menyenangkan dan seru!"

# 1. Slicing kata pertama
kata_pertama = kalimat[:7]
print(f"Kata pertama: {kata_pertama}")

# 2. Sensor kata "menyenangkan"
kalimat_sensor = kalimat.replace("menyenangkan", "***********")
print(f"Kalimat setelah disensor: {kalimat_sensor}")
```

[⬅️ Kembali ke Menu Utama](README.md)












