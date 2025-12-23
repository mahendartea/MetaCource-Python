<h1> 🧬 Data Type atau Tipe Data</h1>

## 📊 1. Integer

Integer atau tipe data integer adalah tipe data yang berisi angka yang tidak ada koma atau disebut juga sebagai bilangan bulat. Contoh: `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`

Contoh penggunaan bilangan integer:

```python
a = 10
b = 20
c = a + b
print(c)

d = -20
e = 20
print(d+e)
```

## 🌊 2. Float

Float atau tipe data float adalah tipe data yang berisi angka yang ada koma atau disebut juga sebagai bilangan riil. Contoh: `1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10`

```python
a = 10.1
b = 20.2
c = a + b
print(c)

c = 3.14
d = 2.18
print(a*d)

# conoth lain
def calculate_area(radius):
    return 3.14159 * radius * radius

print(calculate_area(5.0))

```

## 📝 3. String

String atau tipe data string adalah tipe data yang berisi karakter. Contoh: `"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"`

```python
a = "Hello"
b = "World"
c = a + b
print(c)
```
Contoh lain implementasi tipe data string
```python
ucapan = "hello"
nama = "Budiawan"
pesan = ucapata + ", "+ name + "!"
print(pesan)

# Multiline string
multiline_string = """This is a string that spans
multiple lines within triple quotes."""
print(multiline_string)
```

## ⚖️ 4. Boolean

Boolean atau tipe data boolean adalah tipe data yang berisi nilai True atau False. Contoh: `True, False`

```python
a = True
b = False
print(a)
print(b)

#contoh lain
is_active = True
has_license = False

# menggunakan boolean pada kondisi 
if is_active
    print("akun anda sudah aktif")
else:
    print("akun anda belum aktif")

```


## 📜 5. List

List atau tipe data list adalah tipe data yang berisi nilai yang dapat diubah. Contoh: `[1, 2, 3, 4, 5]`

```python
a = [1, 2, 3, 4, 5]
print("daftar angka: ", a)

# akses elemen list
print("Angka pertama:", a[0])
print("Angka terakhir:", a[1])

#tambah daftar list
a.append(6)
print("daftar ke enam telah ditambahkan:", a)

```
## 🔒 6. Tuple

Tuple atau tipe data tuple adalah tipe data yang berisi nilai yang tidak dapat diubah. Contoh: `(1, 2, 3, 4, 5)`

```python
a = (1, 2, 3, 4, 5)
print(a)

print(a[1])
print(a[2])

sub_tuple = a[1:4]
print("Subtuple from index 1 to 4:", sub_tuple)

#Tuple Unpacking
a, b, c, d, e = a
print("Urai tuple: ", a,b,c,d,e)
```



## 📖 7. Dictionary

Dictionary atau tipe data dictionary adalah tipe data yang berisi nilai yang dapat diubah. Contoh: `{"key1": "value1", "key2": "value2", "key3": "value3"}`

```python
a = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(a)

example_dict = {"name": "John", "age": 30, "city": "New York"}
print("Dictionary:", example_dict)

# Accessing dictionary elements
print("Name:", example_dict["name"])
print("Age:", example_dict["age"])

example_dict["email"] = "john@example.com"
print("Dictionary after adding email:", example_dict)

# Removing a key-value pair
del example_dict["city"]
print("Dictionary after removing city:", example_dict)

# Dictionary comprehension
squared_numbers = {x: x*x for x in range(6)}
print("Dictionary of squared numbers:", squared_numbers)
```
## 🛡️ 8. Set

Set atau tipe data set adalah tipe data yang berisi nilai yang tidak dapat diubah. Contoh: `{1, 2, 3, 4, 5}`

```python
a = {1, 2, 3, 4, 5}
print(a)

# Example of set data type
example_set = {1, 2, 3, 4, 5}
print("Set:", example_set)

# Adding elements to a set
example_set.add(6)
print("Set after adding an element:", example_set)

# Removing elements from a set
example_set.discard(2)
print("Set after removing an element:", example_set)
```

## 🛠️ 9. Fungsi Tipe Data

Fungsi tipe data ini digunakan untuk mengubah tipe data dari satu tipe ke tipe data yang lain. Contoh: `int(a)`, `float(a)`, `str(a)`

```python
a = 10
a = float(a)
print(type(a))
b = long(a)
print(type(b))
c = str(a)
print(type(c))
```

**Beberapa fungsi tipe data adalah sebagai berikut :**

|**Nama Fungsi**|**Deskrips**i|
|---|---|
|int()|Mengubah tipe data dari satu tipe ke tipe data **integer**.|
|long()|Mengubah tipe data dari satu tipe ke tipe data **integer Panjang**.|
|float()|Mengubah tipe data dari satu tipe ke tipe **float**.|
|bool()|Mengubah tipe data dari satu tipe ke tipe data **boolean**.|
|chr()|Mengubah tipe data dari satu tipe ke tipe data **char**.|
|str()|Mengubah tipe data dari satu tipe ke tipe data **string**|
|bin()|Mengubah tipe data dari satu tipe ke tipe data **binary**|
|hex()|Mengubah tipe data dari satu tipe ke tipe data **hexadecimal**|
|oct()|Mengubah tipe data dari satu tipe ke tipe data **octal**|

contoh

```python
# Contoh konversi tipe 
initial_value = 10
converted_to_float = float(initial_value)
print("Original integer:", initial_value, "Converted to float:", converted_to_float)

```


[⬅️ Kembali ke Menu Utama](README.md)