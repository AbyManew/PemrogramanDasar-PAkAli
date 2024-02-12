# Program kasir dengan fitur tambahan

# Inisialisasi dictionary untuk menyimpan daftar barang dan harganya
daftar_barang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 10000,
    "semangka": 15000
}

# Inisialisasi dictionary untuk menyimpan stok barang
stok_barang = {
    "apel": 10,
    "pisang": 20,
    "jeruk": 15,
    "anggur": 8,
    "semangka": 5
}

# Inisialisasi variabel untuk menyimpan total pembelian
total_pembelian = 0

# Fungsi untuk menambah item ke keranjang belanja
def tambah_item(keranjang, barang, jumlah):
    keranjang.append((barang, jumlah))

# Fungsi untuk menghapus item dari keranjang belanja
def hapus_item(keranjang, barang):
    for item in keranjang:
        if item[0] == barang:
            keranjang.remove(item)
            break

# Fungsi untuk menghitung total harga pembelian
def hitung_total(keranjang):
    total = 0
    for item in keranjang:
        total += daftar_barang[item[0]] * item[1]
    return total

# Fungsi untuk menampilkan struk pembayaran
def tampilkan_struk(keranjang):
    print("\n======= Struk Pembelian =======")
    for item in keranjang:
        nama_barang = item[0]
        harga_barang = daftar_barang[nama_barang]
        jumlah_barang = item[1]
        subtotal = harga_barang * jumlah_barang
        print(f"{nama_barang}\t\t x{jumlah_barang}\t\t Rp {subtotal}")
    print("===============================")
    print(f"Total Pembelian \t\t Rp {hitung_total(keranjang)}")

# Program utama
keranjang_belanja = []

while True:
    print("\n===== Menu Kasir =====")
    print("1. Tambah item ke keranjang")
    print("2. Hapus item dari keranjang")
    print("3. Lihat keranjang belanja")
    print("4. Selesai belanja")
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == '1':
        print("\nDaftar Barang:")
        for barang in daftar_barang:
            print(f"{barang}: Rp {daftar_barang[barang]} (Stok: {stok_barang[barang]})")
        barang = input("Masukkan nama barang: ")
        if barang in daftar_barang:
            jumlah = int(input("Masukkan jumlah barang: "))
            if jumlah <= stok_barang[barang]:
                tambah_item(keranjang_belanja, barang, jumlah)
                stok_barang[barang] -= jumlah
            else:
                print("Stok barang tidak mencukupi!")
        else:
            print("Barang tidak ditemukan!")

    elif pilihan == '2':
        if keranjang_belanja:
            print("\nKeranjang Belanja:")
            for i, item in enumerate(keranjang_belanja, 1):
                print(f"{i}. {item[0]} x{item[1]}")
            indeks = int(input("Pilih item yang akan dihapus: "))
            if 1 <= indeks <= len(keranjang_belanja):
                hapus_item(keranjang_belanja, keranjang_belanja[indeks - 1][0])
            else:
                print("Indeks tidak valid!")
        else:
            print("Keranjang belanja kosong!")

    elif pilihan == '3':
        if keranjang_belanja:
            tampilkan_struk(keranjang_belanja)
        else:
            print("Keranjang belanja kosong!")

    elif pilihan == '4':
        if keranjang_belanja:
            tampilkan_struk(keranjang_belanja)
            print("\nTerima kasih telah berbelanja!")
        else:
            print("Anda belum membeli apapun. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")
