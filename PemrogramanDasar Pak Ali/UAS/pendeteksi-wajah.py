import cv2

# Fungsi untuk mendeteksi wajah dalam sebuah gambar
def deteksi_wajah(gambar):
    # Menginisialisasi model Haar Cascade untuk deteksi wajah
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Mengubah gambar ke skala abu-abu
    gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
    
    # Melakukan deteksi wajah dalam gambar
    wajah = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Menggambar kotak di sekitar wajah yang terdeteksi
    for (x, y, w, h) in wajah:
        cv2.rectangle(gambar, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    # Menampilkan gambar hasil deteksi wajah
    cv2.imshow('Deteksi Wajah', gambar)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Membaca gambar
gambar = cv2.imread('contoh_gambar.jpg')

# Memanggil fungsi deteksi wajah
deteksi_wajah(gambar)
