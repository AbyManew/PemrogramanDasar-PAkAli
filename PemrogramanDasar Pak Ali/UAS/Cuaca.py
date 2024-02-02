import requests

def prediksi_cuaca(kota):
    api_key = '0f3e49432869423022c8c894df4b4b89'  # Ganti dengan API key Anda dari OpenWeatherMap
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    # Membuat URL untuk melakukan permintaan cuaca berdasarkan nama kota
    complete_url = f"{base_url}q={kota}&appid={api_key}"

    # Melakukan permintaan GET ke OpenWeatherMap API
    response = requests.get(complete_url)
    data = response.json()

    if 'main' in data:
        # Mendapatkan data cuaca dari respons JSON
        cuaca = data['weather'][0]['description']
        suhu = data['main']['temp']
        kelembaban = data['main']['humidity']
        tekanan_udara = data['main']['pressure']

        # Mencetak prediksi cuaca
        print(f"Prediksi cuaca di {kota}:")
        print(f"Cuaca: {cuaca}")
        print(f"Suhu: {suhu} Kelvin")
        print(f"Kelembaban: {kelembaban}%")
        print(f"Tekanan Udara: {tekanan_udara} hPa")
    else:
        print("Data cuaca tidak ditemukan!")

# Meminta pengguna untuk memasukkan nama kota
kota = input("Masukkan nama kota: ")

# Memanggil fungsi prediksi_cuaca untuk mendapatkan prediksi cuaca
prediksi_cuaca(kota)
