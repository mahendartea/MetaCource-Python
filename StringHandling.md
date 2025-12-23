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
> contoh diatas memecah string menjadi array akan mengembalikan array yaitu `['Hello', ' World!']`

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












