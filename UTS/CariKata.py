# Meminta input dari pengguna
teks = input("Masukkan teks: ")
kata = input("Masukkan kata yang ingin dicari: ")

# Mencari kata dalam teks
if kata in teks:
    print(f"'{kata}' ditemukan dalam teks.")
else:
    print(f"'{kata}' tidak ditemukan dalam teks.")
