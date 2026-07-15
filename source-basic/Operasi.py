# a = 10
# b = -a
# c = +a
# print(c)

# a = 10
# b = 5
# print("a lebih besar" if a > b else "b lebih besar")

# print(a + b) # 15
# print(a - b) # 5
# print(a * b) # 50
# print(a / b) # 2
# print(a % b) # 0
# print(a ** b) # 100000
# print(a // b) # 2

# operator assignment

# a += b
# a *= b
# a /= b
# a %= b
# a **= b
# a //= b

# print(a)

# a = 10
# b = 5

# print(a == b) # False
# print(a != b) # True
# print(a > b) # True
# print(a < b) # False
# print(a >= b) # True
# print(a <= b) # False

# c = 10
# d = "10"

# print(c == d)
# print(a > b and a > b) # True
# print(a > b and a < b) # False
# print(a < b and a > b) # False
# print(a < b and a < b) # False
# print(a > b or a > b) # True
# print(a > b or a < b) # True
# print(a < b or a > b) # True
# print(a < b or a < b) # False

# uts = True
# absen = False

# print(uts and absen)

# a = 10
# b = 5
# print(b in [1, 2, 3, 4, 5]) # false
# print(b not in [1, 2, 3, 4, 5]) # true

# alas = int(input("Masukkan alas segitiga: "))
# tinggi = int(input("Masukkan tinggi segitiga: "))
# luas = 0.5 * alas * tinggi
# print("Luas segitiga adalah", luas)

# angka1 = int(input("Masukkan angka pertama: "))
# angka2 = int(input("Masukkan angka kedua: "))
# tambah = angka1 + angka2
# kurang = angka1 - angka2
# kali = angka1 * angka2
# bagi = angka1 / angka2
# print("Hasil penjumlahan:", tambah)
# print("Hasil pengurangan:", kurang)
# print("Hasil perkalian:", kali)
# print("Hasil pembagian:", bagi)

# phi = 3.14
# jari_jari = float(input("Masukkan jari-jari lingkaran: "))
# luas = phi * jari_jari * jari_jari
# keliling = 2 * phi * jari_jari
# print("Luas lingkaran adalah", luas)
# print("Keliling lingkaran adalah", keliling)

# konversi dari celcius ke farenheit (9/5 x temperatur Celcius) + 32

# celcius = float(input("Masukan suhu dalam celcius : "))
# farenheit = (9/5) * celcius + 32
# print("Hasil konversi celcius dengan derajat ", celcius, "adalah : ")
# print(farenheit)

# rumus celcius ke farenheit 4/5 C
# celcius = float(input("Masukan nilai celcius : "))
# reamur = (4/5) * celcius 
# print("Konversi ke reamur adalah: ", reamur)

# konversi kilometer ke meter
# km = float(input("masukan Kilometer : "))
# meter = km * 1000
# print("Hasil dari meter ke meter adalah", meter)

# import math

# print("Nilai akar (9): ", math.sqrt(9))

print('=' * 25)
print('Operasi Matematika')
print('  1. Jumlah \t [+]')
print('  2. Kurang \t [-]')
print('  3. Kali \t [*]')
print('  4. Bagi \t [/]')
print('=' * 25)

operasi = input('Pilih operasi (1/2/3/4): ')
bilangan_1 = float(input('Masukkan bilangan pertama: '))
bilangan_2 = float(input('Masukkan bilangan kedua: '))

print('=' * 25)

if operasi == '1':
  print('User memilih penjumlahan')
elif operasi == '2':
  print('User memilih pengurangan')
elif operasi == '3':
  print('User memilih perkalian')
elif operasi == '4':
  print('User memilih pembagian')
else:
  print('Tidak valid')

if operasi == '1':
  hasil = bilangan_1 + bilangan_2
  print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
elif operasi == '2':
  hasil = bilangan_1 - bilangan_2
  print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
elif operasi == '3':
  hasil = bilangan_1 * bilangan_2
  print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')
elif operasi == '4':
  hasil = bilangan_1 / bilangan_2
  print(f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')
else:
  print('Tidak valid')


