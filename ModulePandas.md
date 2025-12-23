# 🐼 Pandas: Python Data Analysis Library

Pandas adalah library Python yang powerful untuk analisis dan manipulasi data. Pandas menyediakan struktur data yang mudah digunakan dan efisien untuk bekerja dengan data tabular (seperti spreadsheet atau database).

---

## 🚀 Mengapa Pandas?

- **Data Manipulation**: Mudah membersihkan, mengubah, dan menganalisis data
- **Flexible I/O**: Baca/tulis dari CSV, Excel, SQL, JSON, dan format lainnya
- **Missing Data Handling**: Tools untuk menangani data yang hilang
- **Group By**: Agregasi dan transformasi data yang powerful
- **Time Series**: Fungsi khusus untuk data time series
- **Integration**: Bekerja sempurna dengan NumPy, Matplotlib, dan Scikit-learn

---

## ⚙️ Instalasi Pandas

```bash
pip install pandas
```

Verifikasi instalasi:
```python
import pandas as pd
print(pd.__version__)
```

---

## 📊 Komponen Utama Pandas

Pandas memiliki dua struktur data utama:

### 1. Series (1 Dimensi)

Series adalah array 1 dimensi berlabel, mirip dengan kolom di spreadsheet.

```python
import pandas as pd

# Membuat Series dari list
data = pd.Series([10, 20, 30, 40, 50])
print(data)

# Output:
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

# Series dengan index kustom
data = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(data)

# Akses data
print(data['a'])  # 10
print(data[0])    # 10
```

### 2. DataFrame (2 Dimensi)

DataFrame adalah tabel 2 dimensi dengan baris dan kolom berlabel.

```python
# Membuat DataFrame dari dictionary
data = {
    'Nama': ['Andi', 'Budi', 'Citra', 'Dedi'],
    'Umur': [25, 30, 22, 35],
    'Kota': ['Jakarta', 'Bandung', 'Surabaya', 'Jakarta']
}

df = pd.DataFrame(data)
print(df)

#      Nama  Umur      Kota
# 0    Andi    25   Jakarta
# 1    Budi    30   Bandung
# 2   Citra    22  Surabaya
# 3    Dedi    35   Jakarta
```

---

## 📥 Membaca Data

### Dari CSV

```python
# Membaca file CSV
df = pd.read_csv('data.csv')

# Dengan parameter tambahan
df = pd.read_csv('data.csv', 
                 sep=';',           # Delimiter
                 encoding='utf-8',  # Encoding
                 na_values=['NA', 'null'])  # Nilai null
```

### Dari Excel

```python
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
```

### Dari JSON

```python
df = pd.read_json('data.json')
```

### Dari SQL Database

```python
import sqlite3

conn = sqlite3.connect('database.db')
df = pd.read_sql_query("SELECT * FROM tabel", conn)
```

---

## 💾 Menyimpan Data

```python
# Ke CSV
df.to_csv('output.csv', index=False)

# Ke Excel
df.to_excel('output.xlsx', index=False)

# Ke JSON
df.to_json('output.json', orient='records')

# Ke SQL
df.to_sql('nama_tabel', conn, if_exists='replace', index=False)
```

---

## 👀 Melihat Data

```python
# 5 baris pertama
print(df.head())

# 10 baris pertama
print(df.head(10))

# 5 baris terakhir
print(df.tail())

# Informasi dataset
print(df.info())

# Statistik deskriptif
print(df.describe())

# Ukuran DataFrame (baris, kolom)
print(df.shape)

# Nama kolom
print(df.columns)

# Tipe data setiap kolom
print(df.dtypes)
```

---

## 🔍 Seleksi Data

### Memilih Kolom

```python
# Satu kolom (Series)
nama = df['Nama']

# Satu kolom (DataFrame)
nama = df[['Nama']]

# Multiple kolom
subset = df[['Nama', 'Umur']]
```

### Memilih Baris dengan `.loc` dan `.iloc`

```python
# .loc - berdasarkan label/index
baris_0 = df.loc[0]  # Baris index 0

# .iloc - berdasarkan posisi integer
baris_pertama = df.iloc[0]  # Baris pertama

# Slicing baris
df.loc[0:2]   # Baris 0, 1, 2 (inclusive)
df.iloc[0:2]  # Baris 0, 1 (exclusive)

# Kombinasi baris dan kolom
df.loc[0:2, ['Nama', 'Umur']]
df.iloc[0:3, 0:2]
```

### Filtering dengan Kondisi

```python
# Filter umur > 25
dewasa = df[df['Umur'] > 25]

# Multiple kondisi (AND)
jakarta_dewasa = df[(df['Kota'] == 'Jakarta') & (df['Umur'] > 25)]

# Multiple kondisi (OR)
muda_atau_jakarta = df[(df['Umur'] < 25) | (df['Kota'] == 'Jakarta')]

# Filter dengan .isin()
kota_tertentu = df[df['Kota'].isin(['Jakarta', 'Bandung'])]

# Filter berdasarkan string
nama_awalan_a = df[df['Nama'].str.startswith('A')]
```

---

## ➕ Menambah dan Menghapus

### Menambah Kolom

```python
# Kolom baru dengan nilai tetap
df['Negara'] = 'Indonesia'

# Kolom berdasarkan kalkulasi
df['Umur_5_Tahun'] = df['Umur'] + 5

# Kolom berdasarkan kondisi
df['Kategori'] = df['Umur'].apply(lambda x: 'Muda' if x < 30 else 'Dewasa')
```

### Menambah Baris

```python
# Menambah satu baris
baris_baru = pd.DataFrame({'Nama': ['Eka'], 'Umur': [28], 'Kota': ['Medan']})
df = pd.concat([df, baris_baru], ignore_index=True)
```

### Menghapus Kolom

```python
# Drop kolom
df = df.drop('Negara', axis=1)

# Drop multiple kolom
df = df.drop(['Kolom1', 'Kolom2'], axis=1)

# Inplace (langsung mengubah df)
df.drop('Negara', axis=1, inplace=True)
```

### Menghapus Baris

```python
# Drop baris berdasarkan index
df = df.drop(0)  # Hapus baris index 0

# Drop berdasarkan kondisi
df = df[df['Umur'] > 20]  # Hanya simpan umur > 20
```

---

## 🧹 Menangani Missing Values

### Deteksi Missing Values

```python
# Cek nilai null
print(df.isnull())

# Hitung jumlah null per kolom
print(df.isnull().sum())

# Cek apakah ada null
print(df.isnull().any())
```

### Menghapus Missing Values

```python
# Hapus baris dengan null
df_clean = df.dropna()

# Hapus kolom dengan null
df_clean = df.dropna(axis=1)

# Hapus hanya jika semua nilai null
df_clean = df.dropna(how='all')

# Hapus jika ada null di kolom tertentu
df_clean = df.dropna(subset=['Umur'])
```

### Mengisi Missing Values (Imputation)

```python
# Isi dengan nilai tertentu
df['Umur'].fillna(0, inplace=True)

# Isi dengan mean
df['Umur'].fillna(df['Umur'].mean(), inplace=True)

# Isi dengan median
df['Umur'].fillna(df['Umur'].median(), inplace=True)

# Forward fill (isi dengan nilai sebelumnya)
df['Umur'].fillna(method='ffill', inplace=True)

# Backward fill (isi dengan nilai sesudahnya)
df['Umur'].fillna(method='bfill', inplace=True)
```

---

## 🔄 Transformasi Data

### Rename Kolom

```python
# Rename satu atau beberapa kolom
df = df.rename(columns={'Nama': 'Name', 'Umur': 'Age'})
```

### Ubah Tipe Data

```python
# Ubah tipe data kolom
df['Umur'] = df['Umur'].astype(int)
df['Kota'] = df['Kota'].astype('category')
```

### Sorting

```python
# Sort berdasarkan satu kolom
df_sorted = df.sort_values('Umur')

# Sort descending
df_sorted = df.sort_values('Umur', ascending=False)

# Sort berdasarkan multiple kolom
df_sorted = df.sort_values(['Kota', 'Umur'])
```

### Apply Function

```python
# Apply function ke kolom
df['Umur_Kuadrat'] = df['Umur'].apply(lambda x: x ** 2)

# Apply function ke DataFrame
def kategorisasi(row):
    if row['Umur'] < 25:
        return 'Muda'
    elif row['Umur'] < 35:
        return 'Dewasa'
    else:
        return 'Senior'

df['Kategori'] = df.apply(kategorisasi, axis=1)
```

---

## 📊 Agregasi dan Grouping

### Group By

```python
# Group by satu kolom
grouped = df.groupby('Kota')

# Hitung rata-rata per group
print(grouped['Umur'].mean())

# Multiple agregasi
print(grouped['Umur'].agg(['mean', 'min', 'max', 'count']))

# Group by multiple kolom
grouped = df.groupby(['Kota', 'Kategori'])
print(grouped['Umur'].mean())
```

### Pivot Table

```python
# Pivot table
pivot = df.pivot_table(
    values='Umur',
    index='Kota',
    aggfunc='mean'
)
print(pivot)
```

---

## 🔗 Menggabungkan DataFrame

### Concat (Menggabungkan Vertikal/Horizontal)

```python
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Concat vertikal (menambah baris)
result = pd.concat([df1, df2], ignore_index=True)

# Concat horizontal (menambah kolom)
result = pd.concat([df1, df2], axis=1)
```

### Merge (Join)

```python
df_karyawan = pd.DataFrame({
    'ID': [1, 2, 3],
    'Nama': ['Andi', 'Budi', 'Citra']
})

df_gaji = pd.DataFrame({
    'ID': [1, 2, 4],
    'Gaji': [5000000, 6000000, 7000000]
})

# Inner join
merged = pd.merge(df_karyawan, df_gaji, on='ID', how='inner')

# Left join
merged = pd.merge(df_karyawan, df_gaji, on='ID', how='left')

# Right join
merged = pd.merge(df_karyawan, df_gaji, on='ID', how='right')

# Outer join
merged = pd.merge(df_karyawan, df_gaji, on='ID', how='outer')
```

---

## 📈 Visualisasi Sederhana

Pandas terintegrasi dengan Matplotlib untuk visualisasi cepat:

```python
import matplotlib.pyplot as plt

# Line plot
df['Umur'].plot(kind='line')
plt.show()

# Bar chart
df['Kota'].value_counts().plot(kind='bar')
plt.show()

# Histogram
df['Umur'].plot(kind='hist', bins=10)
plt.show()

# Box plot
df.boxplot(column='Umur', by='Kota')
plt.show()
```

---

## 🛠️ Contoh Praktis: Analisis Data Penjualan

```python
import pandas as pd

# Buat data dummy
data = {
    'Tanggal': pd.date_range('2025-01-01', periods=10),
    'Produk': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Jumlah': [10, 15, 8, 20, 12, 18, 25, 10, 14, 22],
    'Harga': [50000, 75000, 50000, 100000, 75000, 50000, 100000, 75000, 50000, 100000]
}

df = pd.DataFrame(data)

# Hitung total penjualan
df['Total'] = df['Jumlah'] * df['Harga']

# Statistik per produk
print(df.groupby('Produk')['Total'].agg(['sum', 'mean', 'count']))

# Produk terlaris
print(df.groupby('Produk')['Jumlah'].sum().sort_values(ascending=False))

# Total penjualan per hari
print(df.groupby('Tanggal')['Total'].sum())
```

---

## 📝 Latihan

1. Buat DataFrame dengan data 10 siswa (Nama, Nilai Matematika, Nilai Bahasa Indonesia)
2. Hitung rata-rata nilai setiap siswa
3. Temukan siswa dengan nilai tertinggi dan terendah
4. Filter siswa yang lulus (rata-rata >= 70)
5. Buat kolom baru "Status" (Lulus/Tidak Lulus)
6. Simpan hasilnya ke file CSV

---

## 🚀 Langkah Selanjutnya

Setelah menguasai Pandas, lanjutkan ke:
- **Matplotlib/Seaborn**: Visualisasi data yang lebih advanced
- **Scikit-learn**: Machine Learning
- **SQL**: Integrasi dengan database

---

[⬅️ Kembali ke Menu Utama](README.md)
