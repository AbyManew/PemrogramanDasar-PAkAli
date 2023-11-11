operator = input("Masukkan operator (+, -, *, /): ")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if operator == '+':
    hasil = angka1 + angka2
elif operator == '-':
    hasil = angka1 - angka2
elif operator == '*':
    hasil = angka1 * angka2
elif operator == '/':
    hasil = angka1 / angka2
else:
    print("Operator tidak valid")

print("Hasil:", hasil)