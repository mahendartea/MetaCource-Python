# 🔢 NumPy: Numerical Python

NumPy (Numerical Python) adalah library fundamental untuk komputasi ilmiah di Python. NumPy menyediakan array multidimensi yang powerful dan koleksi fungsi matematika untuk bekerja dengan data numerik secara efisien.

---

## 🚀 Mengapa NumPy?

- **Performa Tinggi**: 50-100x lebih cepat dari list Python biasa
- **Memory Efficient**: Menggunakan memori lebih sedikit
- **Broadcasting**: Operasi matematis pada array dengan ukuran berbeda
- **Vectorization**: Operasi tanpa loop eksplisit
- **Foundation**: Basis untuk library data science lain (Pandas, Scikit-learn, TensorFlow)

---

## ⚙️ Instalasi NumPy

```bash
pip install numpy
```

Verifikasi instalasi:
```python
import numpy as np
print(np.__version__)
```

---

## 📊 NumPy Array Basics

### Membuat Array dari List

```python
import numpy as np

# Array 1 dimensi
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)
# Output: [1 2 3 4 5]

# Array 2 dimensi (Matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
# Output:
# [[1 2 3]
#  [4 5 6]]

# Array 3 dimensi
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d.shape)  # (2, 2, 2)
```

### Fungsi Pembuat Array

```python
# Array berisi nol
zeros = np.zeros((3, 4))
print(zeros)

# Array berisi satu
ones = np.ones((2, 3))
print(ones)

# Array dengan nilai tertentu
full = np.full((2, 2), 7)
print(full)

# Array identitas (diagonal 1)
identity = np.eye(3)
print(identity)

# Array dengan range
range_arr = np.arange(0, 10, 2)  # start, stop, step
print(range_arr)  # [0 2 4 6 8]

# Array dengan spasi linear
linspace = np.linspace(0, 1, 5)  # 5 angka dari 0 ke 1
print(linspace)  # [0.   0.25 0.5  0.75 1.  ]

# Array random
random_arr = np.random.rand(3, 3)  # 3x3 random [0, 1)
print(random_arr)

random_int = np.random.randint(0, 100, size=(3, 3))  # 3x3 random integer
print(random_int)
```

---

## 🔍 Atribut Array

```python
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)      # (2, 4) - dimensi array
print(arr.ndim)       # 2 - jumlah dimensi
print(arr.size)       # 8 - total elemen
print(arr.dtype)      # int64 - tipe data
print(arr.itemsize)   # 8 - ukuran setiap elemen (bytes)
```

---

## ✂️ Indexing dan Slicing

### Indexing Dasar

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])      # 10 - elemen pertama
print(arr[-1])     # 50 - elemen terakhir
print(arr[1:4])    # [20 30 40] - slicing
print(arr[::2])    # [10 30 50] - setiap 2 elemen
```

### Indexing Array 2D

```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr_2d[0, 0])     # 1 - baris 0, kolom 0
print(arr_2d[1, 2])     # 6 - baris 1, kolom 2
print(arr_2d[0, :])     # [1 2 3] - semua kolom baris 0
print(arr_2d[:, 1])     # [2 5 8] - semua baris kolom 1
print(arr_2d[0:2, 1:3]) # Subarray
```

### Boolean Indexing

```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Filter nilai > 3
mask = arr > 3
print(arr[mask])  # [4 5 6]

# Langsung
print(arr[arr % 2 == 0])  # [2 4 6] - nilai genap
```

---

## 🔄 Reshaping Array

```python
arr = np.arange(12)
print(arr)  # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# Reshape ke 3x4
reshaped = arr.reshape(3, 4)
print(reshaped)

# Reshape ke 2x6
reshaped2 = arr.reshape(2, 6)
print(reshaped2)

# Flatten (kembali ke 1D)
flattened = reshaped.flatten()
print(flattened)

# Transpose
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.T)  # Transpose
```

---

## ➕ Operasi Matematika

### Operasi Element-wise

```python
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

print(arr1 + arr2)   # [11 22 33 44]
print(arr1 - arr2)   # [-9 -18 -27 -36]
print(arr1 * arr2)   # [10 40 90 160]
print(arr1 / arr2)   # [0.1 0.1 0.1 0.1]
print(arr1 ** 2)     # [1 4 9 16]
```

### Operasi dengan Scalar

```python
arr = np.array([1, 2, 3, 4])

print(arr + 10)   # [11 12 13 14]
print(arr * 2)    # [2 4 6 8]
print(arr ** 2)   # [1 4 9 16]
```

### Fungsi Matematika

```python
arr = np.array([1, 4, 9, 16])

print(np.sqrt(arr))      # [1. 2. 3. 4.]
print(np.exp(arr))       # Eksponensial
print(np.log(arr))       # Logaritma natural
print(np.sin(arr))       # Sinus
print(np.cos(arr))       # Cosinus

# Pembulatan
arr_float = np.array([1.2, 2.7, 3.5, 4.1])
print(np.round(arr_float))   # [1. 3. 4. 4.]
print(np.floor(arr_float))   # [1. 2. 3. 4.]
print(np.ceil(arr_float))    # [2. 3. 4. 5.]
```

---

## 📈 Agregasi Statistik

```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(np.sum(arr))        # 45 - total semua elemen
print(np.mean(arr))       # 5.0 - rata-rata
print(np.median(arr))     # 5.0 - median
print(np.std(arr))        # 2.58... - standar deviasi
print(np.var(arr))        # 6.66... - varians
print(np.min(arr))        # 1 - nilai minimum
print(np.max(arr))        # 9 - nilai maksimum

# Agregasi per axis
print(np.sum(arr, axis=0))   # [12 15 18] - sum per kolom
print(np.sum(arr, axis=1))   # [ 6 15 24] - sum per baris

print(np.argmin(arr))        # 0 - index nilai minimum
print(np.argmax(arr))        # 8 - index nilai maksimum
```

---

## 🔗 Menggabungkan Array

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenate (gabung)
concat = np.concatenate([arr1, arr2])
print(concat)  # [1 2 3 4 5 6]

# Stack vertikal
arr_2d_1 = np.array([[1, 2], [3, 4]])
arr_2d_2 = np.array([[5, 6], [7, 8]])

vstack = np.vstack([arr_2d_1, arr_2d_2])
print(vstack)

# Stack horizontal
hstack = np.hstack([arr_2d_1, arr_2d_2])
print(hstack)
```

---

## ✂️ Memisahkan Array

```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Split menjadi 3 bagian
split = np.split(arr, 3)
print(split)  # [array([1, 2]), array([3, 4]), array([5, 6])]

# Split 2D
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

vsplit = np.vsplit(arr_2d, 2)  # Split horizontal
hsplit = np.hsplit(arr_2d, 2)  # Split vertikal
```

---

## 🎲 Broadcasting

Broadcasting memungkinkan operasi pada array dengan shape berbeda:

```python
# Array 2D + Array 1D
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_1d = np.array([10, 20, 30])

result = arr_2d + arr_1d
print(result)
# [[11 22 33]
#  [14 25 36]]

# Matrix 3x3 + Scalar
matrix = np.ones((3, 3))
result = matrix * 5
print(result)
```

---

## 💾 Menyimpan dan Memuat Array

```python
# Simpan ke file
arr = np.array([1, 2, 3, 4, 5])
np.save('my_array.npy', arr)

# Load dari file
loaded = np.load('my_array.npy')
print(loaded)

# Simpan/load multiple arrays
np.savez('arrays.npz', arr1=arr, arr2=arr*2)
data = np.load('arrays.npz')
print(data['arr1'])
print(data['arr2'])

# Simpan ke text file
np.savetxt('data.txt', arr)
loaded_txt = np.loadtxt('data.txt')
```

---

## 🛠️ Contoh Praktis

### 1. Normalisasi Data

```python
data = np.array([10, 20, 30, 40, 50])

# Min-Max Normalization (0-1)
normalized = (data - np.min(data)) / (np.max(data) - np.min(data))
print(normalized)  # [0.   0.25 0.5  0.75 1.  ]

# Z-score Normalization
z_score = (data - np.mean(data)) / np.std(data)
print(z_score)
```

### 2. Operasi Matrix

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Perkalian matrix
C = np.dot(A, B)
print(C)

# Atau menggunakan @
C = A @ B
print(C)

# Transpose
print(A.T)

# Determinan
det = np.linalg.det(A)
print(det)

# Inverse
inv = np.linalg.inv(A)
print(inv)
```

### 3. Simulasi Data

```python
# Simulasi nilai ujian 100 siswa
np.random.seed(42)  # Untuk reproducibility
scores = np.random.normal(75, 10, 100)  # mean=75, std=10

print(f"Rata-rata: {np.mean(scores):.2f}")
print(f"Median: {np.median(scores):.2f}")
print(f"Std Dev: {np.std(scores):.2f}")
print(f"Nilai tertinggi: {np.max(scores):.2f}")
print(f"Nilai terendah: {np.min(scores):.2f}")

# Hitung persentase yang lulus (>= 70)
lulus = np.sum(scores >= 70)
persentase = (lulus / len(scores)) * 100
print(f"Persentase lulus: {persentase:.1f}%")
```

---

## 📝 Latihan

1. Buatlah array 5x5 dengan nilai random integer 1-100
2. Hitung rata-rata setiap baris dan kolom
3. Temukan nilai maksimum dan posisinya
4. Buat mask untuk nilai > 50 dan hitung jumlahnya
5. Normalisasi array tersebut ke range 0-1

---

## 🚀 Langkah Selanjutnya

Setelah menguasai NumPy, lanjutkan ke:
- **Pandas**: Manipulasi data tabular
- **Matplotlib**: Visualisasi data
- **Scikit-learn**: Machine Learning

---

[⬅️ Kembali ke Menu Utama](README.md)
