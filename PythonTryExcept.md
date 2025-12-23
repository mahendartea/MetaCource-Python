# ⚠️ Python Try & Except: Menangani Error dengan Anggun

Dalam pemrograman, kesalahan (error) pasti akan terjadi. Namun, kita tidak ingin program kita langsung "crash" atau mati saat terjadi kesalahan. Di Python, kita menggunakan blok `try...except` untuk menangani error tersebut.

---

## 🚀 Konsep Dasar

Struktur dasarnya terdiri dari beberapa bagian:

1.  **`try`**: Kode yang ingin kita jalankan namun berpotensi menyebabkan error.
2.  **`except`**: Kode yang akan dijalankan *hanya jika* terjadi error pada blok `try`.
3.  **`else`**: (Opsional) Kode yang dijalankan jika *tidak ada* error.
4.  **`finally`**: (Opsional) Kode yang akan *selalu* dijalankan, baik ada error maupun tidak.

---

## 🛠️ Contoh Sederhana

```python
try:
    angka = int(input("Masukkan sebuah angka: "))
    hasil = 10 / angka
    print(f"Hasilnya: {hasil}")
except:
    print("Terjadi kesalahan! Pastikan Anda memasukkan angka dan bukan nol.")
```

---

## 🧬 Menangani Error Spesifik

Sangat disarankan untuk menyebutkan jenis error yang ingin ditangani agar kita tahu persis apa masalahnya.

```python
try:
    file = open("data.txt")
    konten = file.read()
    angka = 10 / 0
except FileNotFoundError:
    print("Error: File tidak ditemukan!")
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan angka nol!")
except Exception as e:
    print(f"Error tidak terduga: {e}")
```

---

## 🧱 Menggunakan `else` dan `finally`

Blok `else` berguna untuk memisahkan kode yang berisiko dengan kode yang aman. Blok `finally` sangat berguna untuk "bersih-bersih", seperti menutup koneksi database atau file.

```python
try:
    f = open("demofile.txt", "w")
    f.write("Halo Python!")
except:
    print("Ada masalah saat menulis ke file.")
else:
    print("Penulisan file berhasil!")
finally:
    f.close()
    print("File telah ditutup.")
```

---

## 🚩 Membangkitkan Error (`raise`)

Terkadang kita ingin sengaja memunculkan error jika suatu kondisi tidak terpenuhi.

```python
umur = -5

if umur < 0:
    raise Exception("Umur tidak boleh negatif!")
```

---

## ⚖️ Jenis Error Umum di Python

| Nama Error | Penyebab |
| :--- | :--- |
| `IndexError` | Mengakses indeks list yang tidak ada. |
| `KeyError` | Mengakses kunci (key) dictionary yang tidak ada. |
| `TypeError` | Operasi pada tipe data yang salah (misal: string + int). |
| `ValueError` | Nilai benar tapi tipenya tidak sesuai (misal: `int("abc")`). |
| `NameError` | Menggunakan variabel yang belum didefinisikan. |

---

## 🛠️ Latihan Kecil
Buatlah fungsi pembagian yang meminta input dua angka. Gunakan `try...except` untuk menangani jika user memasukkan huruf atau membagi dengan nol!

```python
def bagi():
    try:
        a = float(input("Angka 1: "))
        b = float(input("Angka 2: "))
        print(f"Hasil: {a / b}")
    except ValueError:
        print("Input harus berupa angka!")
    except ZeroDivisionError:
        print("Jangan bagi dengan nol!")

bagi()
```
