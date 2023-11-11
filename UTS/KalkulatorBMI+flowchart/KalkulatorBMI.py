berat = float(input("Masukkan berat (kg): "))
tinggi = float(input("Masukkan tinggi (m): "))

bmi = berat / (tinggi ** 2)

if bmi < 18.5:
    kategori = "Kurus"
elif 18.5 <= bmi < 24.9:
    kategori = "Normal"
elif 25 <= bmi < 29.9:
    kategori = "Gemuk"
else:
    kategori = "Obesitas"

print("BMI Anda:", bmi)
print("Kategori BMI:", kategori)
