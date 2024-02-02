# Mengimpor pustaka yang diperlukan
import random
import string

# Tentukan panjang kata sandi
panjang_Password = 8

# Tentukan karakter-karakter yang dapat digunakan dalam kata sandi
karakter = string.ascii_letters + string.digits + string.punctuation

# Tentukan fungsi untuk menghasilkan kata sandi acak
def generate_password(panjang, karakter):
    # Inisialisasi string kata sandi kosong
    Password = ""
    
    # Melakukan perulangan sesuai dengan panjang yang diinginkan dari kata sandi
    for i in range(panjang):
        # Secara acak memilih sebuah karakter dari string karakter
        karakter_terpilih = random.choice(karakter)
        # Menambahkan karakter yang terpilih secara acak ke string kata sandi
        Password += karakter_terpilih
    
    # Mengembalikan kata sandi yang dihasilkan
    return Password

# Menghasilkan sebuah kata sandi acak dengan panjang yang ditentukan
Password = generate_password(panjang_Password, karakter)

# Mencetak kata sandi yang dihasilkan
print("Password yang dihasilkan:")
print(Password)

# Mencetak pesan untuk mengonfirmasi bahwa program telah selesai berjalan
print("password berhasil dibuat")
