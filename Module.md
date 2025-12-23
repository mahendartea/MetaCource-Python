<h1> 🧩 Module </h1>

## 📖 1. Pendahuluan Module

### 1.1. Apa itu Module?

Module pada python merupakan sebuah library yang berisi fungsi-fungsi yang dapat kita gunakan pada program kita. Module bisa diambil dari eksternal maupun dapat kita buatkan sendiri pada project kita.

### 1.2. Beberapa module python (Eksternal)

- math
- random
- os
- datetime
- time
- sys
- json
- csv
- re
- NumPy
- pandas
- matplotlib
- seaborn
- dll

## 🏗️ 2. Membuat Module sendiri

### 2.1. Membuat module sendiri

Untuk membuat module sendiri kita hanya perlu membuat file dengan extension `.py`
misal kita punya sebuah module bernama `my_module.py` yang berisi sebuah fungsi `my_function()`. Untuk membuat module sendiri kita hanya perlu menuliskan `import my_module` pada program kita.

setelah itu kita buatkan code pada file tersebut sebagai berikut:

```python
def hello():
    print("Hello, World!")
```

kemudian kita panggil function tersebut dengan menggunakan `my_module.hello()`

```python
import my_module

my_module.hello()
```
### 2.2 Membuat module berisi variable

module berisi variable yang digunakan pada program kita.

```python
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```
kemudian kita panggil variable tersebut dengan menggunakan `person1.name`

```python
import mymodule

a = mymodule.person1["age"]
print(a)
```
## 🏷️ 3. Memberikan nama module

untuk memberikan nama pada sebuah module kita bisa menggunakan `as` saat module digunakan/dipanggil.

```python
import mymodule as mm

a = mm.person1["age"]
print(a)
```

## 📥 4. Mengimport module Built-in

kita bisa menggunakan `import` untuk mengimport module built-in

```python
import math

print(math.pi)
```

contoh lain seperti menggunakan `platform` module

```python
import platform

print(platform.system())
```

## 📦 5. Mengimport module dari package

kita bisa menggunakan `from` untuk mengimport module dari package

```python
from mymodule import person1

a = person1["age"]
print(a)
```

contoh lain, misal kita buat file module dengan nama `mymodule.py` 

```python
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```

kemudian kita panggil module tersebut dengan menggunakan `from mymodule import person1`

```python
from mymodule import person1

a = person1["age"]
print(a)
```

## 🌟 6. Mengimport semua module

kita bisa menggunakan `from` untuk mengimport semua module dari package

```python
from mymodule import *

a = person1["age"]
print(a)
```





