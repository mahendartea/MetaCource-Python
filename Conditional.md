<h1> 🔀 Operator Kondisi </h1>

# Kondisi pada Pemrograman Python

## 📚 PreRequisite
- Algoritma
- Diagram Alur
- Strukut Data

Cek di [Algoritma](https://www.dicoding.com/blog/flowchart-adalah/)

## 🛠️ 1.1 Kondisi 

### 1.1.1 Kondisi if

Kondisi if merupakan sebuah percabangan yang akan dieksekusi jika sebuah syarat bernilai benar. Contoh: `if a == 10`

```
Sintaks : if

if syarat:
    Pernyataan1
    Pernyataan2
    dst
```

Contoh penggunaan if

```python
a = 10
if a == 10:
    print("Benar")
```

### 1.1.2 Kondisi if-else

Kondisi if-else merupakan sebuah percabangan yang akan dieksekusi jika sebuah syarat bernilai benar dan jika syarat bernilai salah. Contoh: `if a == 10: print("Benar") else: print("Salah")`

```
Sintaks : if-else
if syarat:
    Pernyataan1
else:
    Pernyataan2
```

contoh penggunaan if-else

```python
a = 10
if a == 10:
    print("Benar")
else:
    print("Salah")
```

### 1.1.3 Kondisi if-elif-else

Kondisi if-elif-else merupakan sebuah percabangan yang akan dieksekusi jika sebuah syarat bernilai benar, jika syarat bernilai salah, dan jika syarat bernilai salah, jika syarat bernilai salah.

Contoh penggunaan if-elif-else

```
Sintaks : if-elif-else
if syarat:
    Pernyataan1
elif syarat:
    Pernyataan2
else:
    Pernyataan3
```

```python
a = 10
if a == 10:
    print("Benar")
elif a == 20:
    print("Salah")
else:
    print("Salah")
```

### 1.1.4 Kondisi dengan Nilai Boolean

Kondisi dengan Nilai Boolean adalah sebuah kondisi yang didefinisikan menggunakan tipe data boolean. Contoh: `a = True`, `b = False`, `c = True`

contoh penggunaan kondisi dengan nilai boolean

```python
a = True
b = False
c = True

if a:
    print("Benar")
elif b:
    print("Salah")
else:
    print("Salah")
```

### 1.1.5 Kondisi dengan Operator Logika

Kondisi dengan Operator Logika adalah sebuah kondisi yang didefinisikan menggunakan operator logika. Contoh: `a and b`, `a or b`, `not a`

Untuk ketiga operasi logika ada `and`, `or`, dan `not` cek tabel kebenaran dibawah ini:
| Operator Logika | Deskripsi |
|-----------------|-----------|
| `and` | Logika dan |
| `or` | Logika atau |
| `not` | Logika tidak

bahan logika [link](https://p2k.stekom.ac.id/ensiklopedia/Tabel_kebenaran)

contoh penggunaan kondisi dengan operator logika

```python
a = True
b = False
c = True

if a and b:
    print("Benar")
elif a or b:
    print("Salah")
else:
    print("Salah")
```

### 1.1.6 Kondisi dengan Operator Perbandingan

Kondisi dengan Operator Perbandingan adalah sebuah kondisi yang didefinisikan menggunakan operator perbandingan. Contoh: `a == b`, `a != b`, `a > b`, `a < b`, `a >= b`, `a <= b`

contoh penggunaan kondisi dengan operator perbandingan

```python
a = 10
b = 5

if a == b:
    print("Benar")
elif a != b:
    print("Salah")
else:
    print("Salah")
```


### 1.1.7 Kondisi dengan Operator Identity

Kondisi dengan Operator Identity adalah sebuah kondisi yang didefinisikan menggunakan operator identity. Contoh: `a is b`, `a is not b`

contoh penggunaan kondisi dengan operator identity

```python
a = 10
b = 5

if a is b:
    print("Benar")
elif a is not b:
    print("Salah")
```

### 1.1.8 Kondisi dengan Operator Membership

Kondisi dengan Operator Membership adalah sebuah kondisi yang didefinisikan menggunakan operator membership. Contoh: `a in b`, `a not in b`

contoh penggunaan kondisi dengan operator membership

```python
a = 10
b = [1, 2, 3, 4, 5]

if a in b:
    print("Benar")
elif a not in b:
    print("Salah")
```

## 🔄 2.1 Switch Case

### 2.1.1 Switch Case

Switch Case merupakan sebuah percabangan yang akan dieksekusi jika sebuah syarat bernilai benar. Contoh: `switch (a) {case 10: print("Benar")}`

contoh penggunaan switch case

```python
inputan = input("Masukkan angka: ")

match inputan:
    case "1":
        print("Satu")
    case "2":
        print("Dua")
    case "3":
        print("Tiga")
    case "4":
        print("Empat")
    case "5":
        print("Lima")
    case _:
        print("Salah")
```


## ⚖️ 3.1 Ternary Operator

### 3.1.1 Ternary Operator

Ternary Operator merupakan sebuah percabangan yang akan dieksekusi jika sebuah syarat bernilai benar. Contoh: `a == 10 ? print("Benar") : print("Salah")`

Contoh penggunaan ternary operator

```python
a = 10

print("Benar") if a == 10 else print("Salah")
```

## 📝 Latihan
### 1. Nilai mahasiswa
```python
nim = int(input("Masukan Nomor Induk Mahasiswa : "))
nama = str(input("Masukan Nama Mahasiswa: "))
nilai = 60
if nilai >= 80:
    status = "Lulus"
else:
    status = "Tidak Lulus"

print("Nomor induk mahasiswa : ", nim)
print("Nama lengkap mahasiswa : ", nama)
print("Nilai \t: ", nilai)
print("Status \t: ", status)
```

### 2. Nilai mahasiswa dengan simbol

```python
nim = int(input("Masukan Nomor Induk Mahasiswa : "))
nama = str(input("Masukan Nama Mahasiswa: "))
nilai = 60
if nilai >= 80:
    grade = "A"
else if nilai >= 70:
    grade = "B"
else if nilai >= 60:
    grade = "C"
else if nilai >= 50:
    grade = "D"
else:
    grade = "E"

print("Nomor induk mahasiswa : ", nim)
print("Nama lengkap mahasiswa : ", nama)
print("Nilai \t: ", nilai)
print("Simbol \t: ", grade)
```

### 3. Latihan membuat hari

```python
def senin():
    print("Senin")
def selasa():
    print("Selasa")
def rabu():
    print("Rabu")
def kamis():
    print("Kamis")
def jumat():
    print("Jumat")
def sabtu():
    print("Sabtu")
def minggu():
    print("Minggu")
def default():
    print("Hari tidak valid")

seleksi = {
    1: senin,
    2: selasa,
    3: rabu,
    4: kamis,
    5: jumat,
    6: sabtu,
    7: minggu
}

def switch(namahari):
    return selecksi.get(namahari, default)()

kode_hari = int(input("Masukan kode hari : "))
print("Hari ini adalah : ", switch(kode_hari))
``` 

[⬅️ Kembali ke Menu Utama](README.md)


