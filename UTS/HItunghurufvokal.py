# Meminta input dari pengguna
kata = input("Masukkan sebuah kata: ")
vokal = 'AEIOUaeiou'
jumlah_vokal = 0

# Menghitung jumlah huruf vokal dalam kata
for huruf in kata:
    if huruf in vokal:
        jumlah_vokal += 1

print(f"Jumlah huruf vokal dalam '{kata}' adalah {jumlah_vokal}.")
