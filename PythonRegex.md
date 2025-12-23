# 🔍 Python Regex: Menguasai Regular Expressions

**Regular Expression** (Regex atau RegExp) adalah urutan karakter yang membentuk pola pencarian. Di Python, kita menggunakan modul bawaan `re` untuk mencari, mencocokkan, dan memanipulasi teks berdasarkan pola tertentu.

---

## 🚀 Memulai dengan `re`

Impor modul `re` sebelum memulai:

```python
import re
```

---

## 🛠️ Fungsi Utama Modul `re`

Ada empat fungsi yang paling sering digunakan:

| Fungsi | Deskripsi |
| :--- | :--- |
| `findall()` | Mengembalikan daftar berisi semua kecocokan. |
| `search()` | Mengembalikan objek Match jika ada kecocokan di bagian mana pun dalam string. |
| `split()` | Mengembalikan daftar di mana string telah dipisahkan pada setiap kecocokan. |
| `sub()` | Mengganti satu atau banyak kecocokan dengan string lain. |

### Contoh Penggunaan:
```python
teks = "Hujan di Jakarta, Jakarta sangat dingin"

# findall
x = re.findall("Jakarta", teks)
print(x) # Output: ['Jakarta', 'Jakarta']

# search
y = re.search("^Hujan", teks)
if y:
  print("Ya, teks dimulai dengan 'Hujan'")

# sub
z = re.sub("\s", "-", teks) # Ganti spasi dengan tanda hubung
print(z) # Output: Hujan-di-Jakarta,-Jakarta-sangat-dingin
```

---

## 🧱 Metakarakter (Karakter Khusus)

Metakarakter adalah karakter dengan makna khusus:

| Karakter | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `[]` | Satu set karakter | `[a-m]` |
| `.` | Karakter apa pun (kecuali baris baru) | `he..o` |
| `^` | Dimulai dengan | `^Halo` |
| `$` | Diakhiri dengan | `dunia$` |
| `*` | Nol atau lebih kemunculan | `aix*` |
| `+` | Satu atau lebih kemunculan | `aix+` |
| `?` | Nol atau satu kemunculan | `aix?` |
| `\|` | Salah satu dari | `jatuh\|bangkit` |

---

## 🧬 Special Sequences (Urutan Khusus)

Urutan khusus dimulai dengan `\` diikuti oleh karakter tertentu:

- `\d` : Mencocokkan angka (0-9).
- `\w` : Mencocokkan karakter kata (huruf, angka, underscore).
- `\s` : Mencocokkan spasi (whitespace).
- `\b` : Mencocokkan awal atau akhir kata.

---

## 💡 Contoh Praktis: Validasi Email Sederhana

Regex sangat powerful untuk melakukan validasi input.

```python
import re

email_pola = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
test_email = "contoh.user@gmail.com"

if re.match(email_pola, test_email):
    print("Email Valid!")
else:
    print("Email Tidak Valid!")
```
*Catatan: Prefiks `r` sebelum string menandakan "raw string" agar backslash `\` tidak diproses oleh Python.*

---

## 🛠️ Latihan Kecil
Cobalah buat kode untuk mengekstrak semua angka dari kalimat berikut:
`"Pesanan saya ada 3 burger, 2 kentang, dan 5 minuman."`

**Jawaban:**
```python
import re
teks = "Pesanan saya ada 3 burger, 2 kentang, dan 5 minuman."
angka = re.findall(r"\d+", teks)
print(f"Jumlah pesanan: {angka}") 
# Output: ['3', '2', '5']
```

---

### ⚠️ Tips
Gunakan situs seperti [regex101.com](https://regex101.com) untuk mencoba pola regex Anda secara visual sebelum menerapkannya di kode Python.
