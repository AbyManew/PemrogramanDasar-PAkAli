# Program ini akan meminta pengguna untuk memasukkan dua bilangan bulat
# dan kemudian menampilkan hasil penjumlahan, pengurangan, perkalian, dan pembagian.

# Meminta pengguna untuk memasukkan dua bilangan bulat
num1 = int(input("Masukkan bilangan bulat pertama: "))
num2 = int(input("Masukkan bilangan bulat kedua: "))

# Menghitung penjumlahan, pengurangan, perkalian, dan pembagian
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Menampilkan hasil penjumlahan, pengurangan, perkalian, dan pembagian
print("Hasil penjumlahan:", addition)
print("Hasil pengurangan:", subtraction)
print("Hasil perkalian:", multiplication)
print("Hasil pembagian:", division)

# Memeriksa apakah bilangan pertama lebih besar dari bilangan kedua
if num1 > num2:
    print("Bilangan pertama lebih besar dari bilangan kedua.")
elif num1 < num2:
    print("Bilangan kedua lebih besar dari bilangan pertama.")
else:
    print("Bilangan pertama dan kedua sama besar.")

# Menghitung dan menampilkan rata-rata dari dua bilangan
average = (num1 + num2) / 2
print("Rata-rata:", average)

# Memeriksa apakah kedua bilangan sama
if num1 == num2:
    print("Bilangan pertama dan kedua sama.")
else:
    print("Bilangan pertama dan kedua berbeda.")

# Menampilkan bilangan terbesar
max_num = max(num1, num2)
print("Bilangan terbesar:", max_num)

# Menampilkan bilangan terkecil
min_num = min(num1, num2)
print("Bilangan terkecil:", min_num)

# Menghitung hasil pembagian bulat dari dua bilangan
integer_division = num1 // num2
print("Hasil pembagian bulat:", integer_division)

# Menghitung sisa pembagian dari dua bilangan
modulus = num1 % num2
print("Sisa pembagian:", modulus)

# Menghitung pangkat dari dua bilangan
power = num1 ** num2
print("Hasil pangkat:", power)

# Memeriksa apakah bilangan pertama negatif, positif, atau nol
if num1 > 0:
    print("Bilangan pertama adalah bilangan positif.")
elif num1 < 0:
    print("Bilangan pertama adalah bilangan negatif.")
else:
    print("Bilangan pertama adalah nol.")

# Memeriksa apakah bilangan kedua negatif, positif, atau nol
if num2 > 0:
    print("Bilangan kedua adalah bilangan positif.")
elif num2 < 0:
    print("Bilangan kedua adalah bilangan negatif.")
else:
    print("Bilangan kedua adalah nol.")

# Menampilkan bilangan bulat terdekat untuk setiap bilangan
rounded_num1 = round(num1)
rounded_num2 = round(num2)
print("Bilangan bulat terdekat untuk bilangan pertama:", rounded_num1)
print("Bilangan bulat terdekat untuk bilangan kedua:", rounded_num2)

# Mengonversi bilangan bulat menjadi biner
binary_num1 = bin(num1)
binary_num2 = bin(num2)
print("Representasi biner bilangan pertama:", binary_num1)
print("Representasi biner bilangan kedua:", binary_num2)

# Mengonversi bilangan bulat menjadi heksadesimal
hexadecimal_num1 = hex(num1)
hexadecimal_num2 = hex(num2)
print("Representasi heksadesimal bilangan pertama:", hexadecimal_num1)
print("Representasi heksadesimal bilangan kedua:", hexadecimal_num2)

# Mengonversi bilangan bulat menjadi oktal
octal_num1 = oct(num1)
octal_num2 = oct(num2)
print("Representasi oktal bilangan pertama:", octal_num1)
print("Representasi oktal bilangan kedua:", octal_num2)
