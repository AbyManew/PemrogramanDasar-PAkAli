import requests

def get_weather(api_key, city):
    # URL dasar API OpenWeatherMap
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Parameter untuk dikirimkan ke API, termasuk kunci API, nama kota, dan unit suhu (Celsius)
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Untuk mendapatkan suhu dalam satuan Celsius
    }

    # Mengirim permintaan GET ke API
    response = requests.get(base_url, params=params)
    weather_data = response.json()

    # Memeriksa status kode respons
    if response.status_code == 200:
        # Mendapatkan informasi utama tentang cuaca dari respons JSON
        main_info = weather_data['main']
        weather_description = weather_data['weather'][0]['description']
        temperature = main_info['temp']
        humidity = main_info['humidity']

        # Menampilkan hasil cuaca
        print(f"Weather in {city}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        # Menampilkan pesan kesalahan jika gagal mendapatkan data cuaca
        print(f"Failed to fetch weather data. Status code: {response.status_code}")
        print(weather_data)

if __name__ == "__main__":
    # Ganti 'YOUR_API_KEY' dengan kunci API OpenWeatherMap Anda
    api_key = 'YOUR_API_KEY'
    city = input("Enter city name: ")
    
    # Memanggil fungsi untuk mendapatkan data cuaca
    get_weather(api_key, city)
