# 1. Import pustaka yang dibutuhkan
import cv2 as cv

# 2. Membaca file gambar dari lokasi yang kamu tentukan di dalam tanda kutip
img = cv.imread("...")

# 3. Mengimpor fungsi khusus dari Google Colab untuk menampilkan gambar ke layar,
# lalu memanggil fungsi tersebut untuk menampilkan gambar asli yang ada di variabel 'img'.
from google.colab.patches import cv2_imshow
cv2_imshow(img)

# 4. Melakukan konversi gambar asli ('img') dari format warna BGR menjadi Grayscale,
# menyimpan hasilnya ke variabel 'gray', lalu menampilkannya ke layar.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv2_imshow(gray)
