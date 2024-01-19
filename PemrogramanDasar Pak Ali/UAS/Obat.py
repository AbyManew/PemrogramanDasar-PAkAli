def hitung_dosis_obat(berat_badan, dosis_per_kg):
    # Menghitung dosis total obat berdasarkan berat badan dan dosis per kilogram
    dosis_total = berat_badan * dosis_per_kg
    return dosis_total

def input_berat_badan():
    while True:
        try:
            # Meminta pengguna memasukkan berat badan, dan memvalidasi bahwa input adalah nilai numerik positif
            berat_badan = float(input("Masukkan berat badan pasien (kg): "))
            if berat_badan <= 0:
                raise ValueError("Berat badan harus positif.")
            return berat_badan
        except ValueError as e:
            # Menangani kesalahan jika pengguna memasukkan input yang tidak valid
            print(f"Error: {e}. Silakan masukkan angka yang valid.")

def input_dosis_per_kg():
    while True:
        try:
            # Meminta pengguna memasukkan dosis obat per kilogram, dan memvalidasi bahwa input adalah nilai numerik positif
            dosis_per_kg = float(input("Masukkan dosis obat per kg berat badan: "))
            if dosis_per_kg <= 0:
                raise ValueError("Dosis per kg harus positif.")
            return dosis_per_kg
        except ValueError as e:
            # Menangani kesalahan jika pengguna memasukkan input yang tidak valid
            print(f"Error: {e}. Silakan masukkan angka yang valid.")

def main():
    print("Program Penghitung Dosis Obat")

    # Meminta input berat badan dan dosis obat per kilogram
    berat_badan = input_berat_badan()
    dosis_per_kg = input_dosis_per_kg()

    # Menghitung dosis total obat
    dosis_total = hitung_dosis_obat(berat_badan, dosis_per_kg)

    # Menampilkan hasil perhitungan dosis obat
    print(f"Dosis obat yang direkomendasikan untuk pasien dengan berat badan {berat_badan} kg adalah {dosis_total:.2f} unit.")

if __name__ == "__main__":
    main()
