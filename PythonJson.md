# 📄 Python JSON: Mengolah Data Format JSON

**JSON** (*JavaScript Object Notation*) adalah format populer yang digunakan untuk menyimpan dan bertukar data. Di Python, kita menggunakan modul bawaan `json` untuk bekerja dengan data JSON.

---

## 🚀 Memulai dengan `json`

Impor modul `json` sebelum memulai:

```python
import json
```

---

## 🔁 Konversi Antar Tipe Data

Dua operasi utama dalam JSON adalah:
1.  **Parsing JSON**: Mengubah string JSON menjadi Dictionary Python (`loads`).
2.  **Serialisasi JSON**: Mengubah Dictionary Python menjadi string JSON (`dumps`).

### 1. JSON ke Python (`json.loads`)
Jika Anda memiliki string JSON, Anda bisa mengubahnya menjadi dictionary Python agar datanya bisa diakses dengan kunci.

```python
# String JSON
data_json = '{"nama": "Andi", "umur": 25, "kota": "Jakarta"}'

# Parsing ke Dictionary
data_python = json.loads(data_json)

print(data_python["nama"]) # Output: Andi
```

### 2. Python ke JSON (`json.dumps`)
Jika Anda memiliki objek Python (seperti dictionary), Anda bisa mengubahnya menjadi string JSON untuk dikirim ke API atau disimpan ke file.

```python
# Dictionary Python
user = {
  "nama": "Budi",
  "hobi": ["Musik", "Coding"],
  "premium": True
}

# Konversi ke string JSON
hasil_json = json.dumps(user)

print(hasil_json)
# Output: {"nama": "Budi", "hobi": ["Musik", "Coding"], "premium": true}
```

---

## 🎨 Mempercantik Tampilan JSON

Secara default, `json.dumps()` menghasilkan string satu baris tanpa spasi. Untuk membuatnya lebih mudah dibaca (pretty print), gunakan parameter `indent`.

```python
print(json.dumps(user, indent=4, sort_keys=True))
```

---

## 📂 Bekerja dengan File JSON

Jika Anda ingin membaca dari file `.json` atau menyimpan data ke file, gunakan fungsi `load()` dan `dump()` (tanpa 's').

### Menyimpan ke File (`dump`)
```python
with open("data.json", "w") as file:
    json.dump(user, file, indent=4)
```

### Membaca dari File (`load`)
```python
with open("data.json", "r") as file:
    data = json.load(file)
    print(data["nama"])
```

---

## ⚖️ Tabel Konversi Python vs JSON

| Python | JSON |
| :--- | :--- |
| dict | Object (`{}`) |
| list, tuple | Array (`[]`) |
| str | String (`""`) |
| int, float | Number |
| True | true |
| False | false |
| None | null |

---

## 💡 Contoh Praktis: Mengolah Response API
Banyak data dari internet dikirim dalam format JSON.

```python
import json

# Simulasi data dari internet
respon_api = '[{"id": 1, "tugas": "Belajar Python"}, {"id": 2, "tugas": "Belajar JSON"}]'

daftar_tugas = json.loads(respon_api)
for item in daftar_tugas:
    print(f"Tugas {item['id']}: {item['tugas']}")
```

---

### 🛠️ Latihan Kecil
Buatlah sebuah dictionary berisi data buah-buahan (nama, warna, harga) lalu simpan ke dalam file bernama `buah.json`!
