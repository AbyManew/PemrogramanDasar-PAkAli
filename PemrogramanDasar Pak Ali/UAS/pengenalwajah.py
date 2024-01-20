# Import library yang diperlukan
import cv2
import face_recognition

# Fungsi untuk menggambar kotak di sekitar wajah yang terdeteksi
def draw_rectangle(frame, top, right, bottom, left):
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

# Fungsi untuk menampilkan teks label di sekitar wajah yang terdeteksi
def draw_text(frame, text, x, y):
    cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

# Load gambar wajah yang akan dijadikan referensi (harus berupa gambar .jpg)
reference_image = face_recognition.load_image_file("path/to/reference/image.jpg")

# Dapatkan encoding wajah dari gambar referensi
reference_encoding = face_recognition.face_encodings(reference_image)[0]

# Inisialisasi kamera
video_capture = cv2.VideoCapture(0)

while True:
    # Ambil frame dari kamera
    ret, frame = video_capture.read()

    # Temukan semua wajah dalam frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Bandingkan encoding wajah dalam frame dengan encoding wajah referensi
        matches = face_recognition.compare_faces([reference_encoding], face_encoding)

        name = "Unknown"

        # Jika ada wajah yang cocok dengan referensi, beri label nama
        if True in matches:
            name = "Name_of_the_person"  # Ganti dengan nama orang yang sesuai

        # Gambar kotak di sekitar wajah dan tampilkan teks nama
        draw_rectangle(frame, top, right, bottom, left)
        draw_text(frame, name, left + 6, bottom - 6)

    # Tampilkan frame yang telah dimodifikasi
    cv2.imshow('Video', frame)

    # Hentikan program dengan menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup kamera dan jendela tampilan
video_capture.release()
cv2.destroyAllWindows()
