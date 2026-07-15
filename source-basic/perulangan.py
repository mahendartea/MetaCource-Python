#membuat list nama bulan

# list_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

# for bulan in list_bulan:
#     # print(bulan) #output
#     print(bulan, end=' ', flush=True) #inline output

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# for i in range(10):
#     print(i)
# else:
#     for j in range(5):
#         print(j)

# a = 10
# b = 5

# while a > b:
#     print("looping  ")

# i = 0
# while i < 10: # true 
#     print("looping")
#     i = i + 1

# list_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
# i = 0
# while i < len(list_hari):
#     print(list_hari[i])
#     i = i + 1

# angka = 0
# while angka < 10:
#     angka = int(input("Masukkan angka: "))
#     print(angka)

# y = "y"
# while y == "y":
#     nama = input("Masukkan nama: ")
#     print("Halo", nama)
#     y = input("Apakah anda ingin melanjutkan (y/t)? ")

# jawab = "y"
# while jawab == "y":
#     angka = int(input("Masukkan angka: "))
#     if angka > 1:
#         for i in range(2, angka):
#             if angka % i == 0:
#                 print(f"{angka} bukan bilangan prima")
#                 print(f"Karena {angka} habis dibagi oleh {i}")
#                 break
#         else:
#             print(f"{angka} adalah bilangan prima")
#     else:
#         print(f"{angka} bukan bilangan prima")
#     print()
#     jawab = input("Apakah anda ingin melanjutkan (y/t)? ")
# jawab = "y"
# while jawab == "y":
#     angka = int(input("Masukkan angka: "))
#     if(angka % 4 == 0):
#         if(angka % 100 == 0):
#             if(angka % 400 == 0):
#                 print(angka, "adalah tahun kabisat")
#             else:
#                 print(angka, "bukan tahun kabisat")
#         else:
#             print(angka, "adalah tahun kabisat")
#     else:
#         print(angka, "bukan tahun kabisat")
#     print()
#     jawab = input("Apakah anda ingin melanjutkan (y/t)? ")

# Calculate the sum of numbers until user enters 0
# number = int(input('Enter a number: '))

# total = 0

# # iterate until the user enters 0
# while number != 0:
#     total += number
#     number = int(input('Enter a number: '))

# print('The sum is', total)