# Grayscale Image
- **Grayscale Image** adalah jenis citra yang hanya memiliki satu saluran (channel) informasi, yaitu intensitas cahaya, tanpa ada informasi warna. Nilai setiap pikselnya direpresentasikan dalam rentang 0 (hitam pekat) hingga 255 (putih terang).
- **Kenapa digunakan?** Gambar berwarna standar (RGB) memiliki tiga matriks data (Merah, Hijau, Biru). Mengubahnya menjadi grayscale menyusutkan ukuran data menjadi sepertiganya. Karena warna seringkali tidak relevan untuk mengenali bentuk geometri dasar, langkah ini sangat penting untuk mengurangi beban komputasi dan mempercepat pemrosesan.

# Langkah-Langkah
Berikut adalah panduan langkah demi langkah untuk mengubah gambar menjadi grayscale menggunakan Python di Google Colab. Kita akan menggunakan pustaka **OpenCV**, yang merupakan standar industri untuk Computer Vision.

:one: Persiapan Google Colab
- Buka browser dan masuk ke Google Colab
- Klik New Notebook untuk membuat lembar kerja baru
