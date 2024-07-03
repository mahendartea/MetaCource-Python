from module_mtk import *
import math
import platform
import os
import numpy as np

hasil = tambah(10, 20)

datakita = data

mengurangi = kurang(10, 20)

print(f"Hasil penjumlahan 10 + 20 = {hasil}")
print(datakita["nama"])

# math build in module dan sqrt function dari module math
print(math.sqrt(9))

# platform build in module
print(platform)
print(platform.release())
print(platform.version())

# os build in module
print(os.getcwd())

a = np.array([1, 2, 3, 4, 5])
print(a)