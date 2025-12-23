<h1> ➕ Operasi Pada Python </h1>

## 📖 Pengertian Operasi pada Python
Operation atau operasi adalah suatu proses yang dilakukan pada suatu data. Contoh operasi yang sering digunakan adalah operasi aritmatika, logika, dan lainnya.

Operasi pada pemrograman menggunhakan operator yang terbagi menjadi beberapa group yaitu:

1. **Arithmetic operators**: Operator aritmatika adalah operator yang digunakan untuk melakukan operasi aritmatika seperti penjumlahan, pengurangan, perkalian, dan pembagian. Contoh operator aritmatika yaitu +, -, *, dan /.
2. **Assignment operators**: Operator assignment adalah operator yang digunakan untuk melakukan operasi assignment seperti penugasan, penambahan, pengurangan, perkalian, dan pembagian. Contoh operator assignment yaitu =, +=, -=, *=, dan /=.
3. **Comparison operators**: Operator pembanding adalah operator yang digunakan untuk melakukan operasi pembanding seperti sama dengan, tidak sama dengan, lebih besar dari, lebih kecil dari, dan lainnya. Contoh operator pembanding yaitu ==, !=, >, <, dan lainnya.
4. **Logical operators**: Operator logika adalah operator yang digunakan untuk melakukan operasi logika seperti AND, OR, dan NOT. Contoh operator logika yaitu AND, OR, dan NOT.
5. **Identity operators**: Operator identitas adalah operator yang digunakan untuk melakukan operasi identitas seperti sama dengan, tidak sama dengan. Contoh operator identitas yaitu ==, !=.
6. **Membership operators**: Operator membership adalah operator yang digunakan untuk melakukan operasi membership seperti in, not in. Contoh operator membership yaitu in, not in.
7. **Bitwise operators**: Operator bitwise adalah operator yang digunakan untuk melakukan operasi bitwise seperti AND, OR, XOR, dan NOT. Contoh operator bitwise yaitu &, |, ^, dan ~.

## 🔢 Operand dan Operator
`Operand` dan `Operator` sering digunakan pada saat membuat program, kita harus paham apa yang dimaksud dengan `operand` dan `operator`. Berikut penjelasannya

- **Operand** : nilai yang digunakan dalam sebuah opersi, misalnya dalam sebuah operasi matematis.

- **Operator** : simbol yang digunakan untuk melakukan operasi, misalnya dalam sebuah operasi matematis.

Contoh dalam operasi matematika seperti berikut: `A+B` maka `A` dan `B` adalah `Operand` dan `+` adalah `Operator`.

## 🧬 Operator Unary, Binary, Ternary
Berdasarkan jumlah `operand`nya maka kita mengenal operator : `unary`, `binary`, dan `ternary`. Berikut deskripsi tentang ketiganya.

1. **Unary Operator**: Operator unary adalah operator yang digunakan untuk melakukan operasi unary, seperti negasi, increment, decrement, dan lain-lain. Contoh operator unary yaitu -.

    |Operator|Nama Operator|Contoh|
    |---|---|---
    |unary|negasi|`-a`|
    |unary|increment|`a++`|
    |unary|decrement|`a--`|

    ```python
    a = 10
    print(-a) # -10
    print(a++) # 10 digunakan untuk looping
    print(a--) # 11 digunakan untuk looping
    ```

2. **Binary Operator**: Operator binary adalah operator yang digunakan untuk melakukan operasi binary, seperti penjumlahan, pengurangan, perkalian, dan pembagian. Contoh operator binary yaitu +.

    |Operator|Deskripsi Operator|Contoh|
    |---|---|---
    |binary|penjumlahan|`a+b`|
    |binary|pengurangan|`a-b`|
    |binary|perkalian|`a*b`|
    |binary|pembagian|`a/b`|

    ```python
    a = 10
    b = 5
    print(a + b) # 15
    print(a - b) # 5
    print(a * b) # 50
    print(a / b) # 2
    ```

3. **Ternary Operator**: Operator ternary adalah operator yang digunakan untuk melakukan operasi ternary, seperti pengkondisian. Contoh operator ternary yaitu ?.
Tujuan operator ini adalah untuk memutuskan nilai mana yang akan diberikan ke variabel. Sintaks dari operator ini adalah sebagai berikut:
    ```
    [on_true] if [expression] else [on_false]
    ```

    ```python
    a = 10
    b = 5
    print("a lebih besar" if a > b else "b lebih besar")
    ```

## 📐 1. Operator Aritmatika
Contoh operasi aritmatika yaitu:

```python
a = 10
b = 5

print(a + b) # 15
print(a - b) # 5
print(a * b) # 50
print(a / b) # 2
print(a % b) # 0
print(a ** b) # 100000
print(a // b) # 2
```
## ✍️ 2. Operator Assignment (Penugasan)
Contoh operasi assignment yaitu:

```python
a = 10
b = 5

a += b
a -= b
a *= b
a /= b
a %= b
a **= b
a //= b

print(a)
```

## ⚖️ 3. Operator Pembanding
Contoh operasi pembanding yaitu:

```python
a = 10
b = 5

print(a == b) # False
print(a != b) # True
print(a > b) # True
print(a < b) # False
print(a >= b) # True
print(a <= b) # False
```
## 🧠 4. Operator Logika
Contoh operasi logika yaitu:

bahan logika [link](https://p2k.stekom.ac.id/ensiklopedia/Tabel_kebenaran)

```python
a = 10
b = 5

print(a > b and a > b) # True
print(a > b and a < b) # False
print(a < b and a > b) # False
print(a < b and a < b) # False
print(a > b or a > b) # True
print(a > b or a < b) # True
print(a < b or a > b) # True
print(a < b or a < b) # False
```
## 🆔 5. Operator Identitas
Contoh operasi identitas yaitu:

```python
a = 10
b = 5

print(a is b) # False
print(a is not b) # True
```
## 👥 6. Operator Membership
Contoh operasi membership yaitu:

```python
a = 10
b = 5

print(a in [1, 2, 3, 4, 5]) # false
print(a not in [1, 2, 3, 4, 5]) # true
```

## 👾 7. Operator Bitwise
Contoh operasi bitwise yaitu:

```python
a = 10
b = 5

print(a & b) # 0
print(a | b) # 15
print(a ^ b) # 15
print(~a) # -11
```

## 📝 Latihan
### 1. Membuat aplikasi luas segitiga sederhana
```python
alas = int(input("Masukkan alas segitiga: "))
tinggi = int(input("Masukkan tinggi segitiga: "))
luas = 0.5 alas * tinggi
print("Luas segitiga adalah", luas)
```
### 2. Membuat aplikasi kalkulator
```python
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
tambah = angka1 + angka2
kurang = angka1 - angka2
kali = angka1 * angka2
bagi = angka1 / angka2
print("Hasil penjumlahan:", tambah)
print("Hasil pengurangan:", kurang)
print("Hasil perkalian:", kali)
print("Hasil pembagian:", bagi)
```

### 3. Membuat aplikasi luas, keliling lingkaran
```python
phi = 3.14
jari_jari = float(input("Masukkan jari-jari lingkaran: "))
luas = phi * jari_jari * jari_jari
keliling = 2 * phi * jari_jari
print("Luas lingkaran adalah", luas)
print("Keliling lingkaran adalah", keliling)
```

[⬅️ Kembali ke Menu Utama](README.md)

