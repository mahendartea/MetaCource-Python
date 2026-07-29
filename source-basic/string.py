# Multiline String

# a = """WhatsApp is often contested as the world’s most popular 
# messaging app, allowing its users to communicate securely and 
# in real-time. As a business owner, you can build upon the speed 
# and security provided by WhatsApp to engage with your customers, 
# send alerts and notifications, provide customer support, 
# or even send One-Time Passwords (OTPs) to your customers.."""
# print(a[:8])
#
# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)

#Slicing
# b = "Hello, World!"
# print(b[-5:-2])

a = " HELOO SEMUANYA "
print(a.upper())
print(a.lower())
print(a.capitalize())

print(a.strip())

b = "Mr."
c = "Jhon Doe"
print(b + " " + c)

# String repetition
# repeat_string = "Python! " * 3
# print(repeat_string)

# Accessing string characters
# sample_string = "Hello World"
# first_letter = sample_string[0]
# print("First letter:", first_letter)
# last_letter = sample_string[-1]
# print("Last letter:", last_letter)


# String length
# string_length = len(sample_string)
# print("Length of string:", string_length)

# String methods
# lowercase_string = sample_string.lower()
# print("Lowercase:", lowercase_string)
# uppercase_string = sample_string.upper()
# print("Uppercase:", uppercase_string)

# String formatting
age = 30
name = "Budiawan"
info = "My name is {} and I am {} years old.".format(name, age)
print(info)

# f-string (available from Python 3.6+)
info_fstring = f"My name is {name} and I am {age} years old."
print(info_fstring)

nama = "Mahendar"
umur = 35
nidn = 1331108701
tinggal = "Lambaro, Aceh Besar"
tempatLahir = "Lhokseumawe"
tglLahir = "33 november 1988"

sertifikat = f"""
Sertifikat Pelatihan Pemrograman Python :
=========================================
Nama \t \t \t: {nama}
umur\t \t \t: {umur}
nomor Induk \t \t : {nidn}
Alamat \t: {tinggal}
tempat/tglLahir \t: {tempatLahir} / {tglLahir}

ini merupakan sertifikat "otentik"
"""
print(sertifikat)

z = "INi adalah ijazah otentik \"Otentik\". \nJadi adalahaaaa adalah jangan disalahgunakan! / diganti"
print(z.count("adalah"))

repeat_string = "Python! " * 10
print(repeat_string)

# Accessing string characters
sample_string = "Hello World"
first_letter = sample_string[0]
print("First letter:", first_letter)
last_letter = sample_string[-1]
print("Last letter:", last_letter)

# ==========================================
# LATIHAN-LATIHAN STRING
# ==========================================

# # 1. Format Biodata Sederhana
# nama = input("Masukkan Nama: ")
# pekerjaan = input("Masukkan Pekerjaan: ")
# kota = input("Masukkan Kota Asal: ")
# print(f"Halo, saya {nama}. Saya bekerja sebagai {pekerjaan} dan berasal dari {kota}.")

# # 2. Validasi & Pembersihan Email
# email = input("Masukkan email Anda: ")
# email_bersih = email.strip().lower()
# print(f"Email setelah dibersihkan: {email_bersih}")
# apakah_gmail = "@gmail.com" in email_bersih
# print(f"Apakah ini akun Gmail? {apakah_gmail}")

# # 3. Slicing & Sensor Kata (Replace)
# kalimat = "Belajar Python sangat menyenangkan dan seru!"
# kata_pertama = kalimat[:7]
# print(f"Kata pertama: {kata_pertama}")
# kalimat_sensor = kalimat.replace("menyenangkan", "***********")
# print(f"Kalimat setelah disensor: {kalimat_sensor}")

