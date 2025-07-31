# Personal Reality Filter

## Deskripsi

Personal Reality Filter adalah program tingkat sistem operasi yang dirancang untuk meningkatkan kesejahteraan mental pengguna dengan menyesuaikan output audio dan visual secara dinamis berdasarkan data biometrik waktu nyata. Aplikasi ini terhubung dengan sensor biometrik pengguna (misalnya, monitor detak jantung) untuk mendeteksi kondisi seperti stres atau kelelahan.

Berdasarkan data ini, aplikasi dapat secara otomatis:
- **Meredam suara frekuensi tinggi** saat pengguna mengalami stres untuk menciptakan lingkungan yang lebih tenang.
- **Mempertajam teks pada layar** saat pengguna merasa lelah untuk mengurangi ketegangan mata dan meningkatkan keterbacaan.

Proyek ini bertujuan untuk memberikan pengalaman sensorik yang dipersonalisasi yang beradaptasi dengan kondisi mental pengguna, sehingga mendorong keadaan pikiran yang lebih sehat dan seimbang.

## Fitur MVP

Versi Minimum Viable Product (MVP) saat ini mencakup fitur-fitur inti berikut:
- **Integrasi Data Biometrik:** Kemampuan untuk membaca dan memproses data biometrik dasar (stres dan kelelahan).
- **Penyesuaian Audio Dinamis:** Penyesuaian output audio secara otomatis sebagai respons terhadap tingkat stres yang terdeteksi.
- **Penyesuaian Visual Dinamis:** Penyesuaian output visual secara otomatis sebagai respons terhadap tingkat kelelahan yang terdeteksi.
- **Manajemen Profil Pengguna:** Profil pengguna dasar untuk menyimpan preferensi dan riwayat data biometrik.

## Instalasi

Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah berikut:

1.  **Kloning Repositori:**
    ```bash
    git clone https://github.com/username/personal-reality-filter.git
    cd personal-reality-filter
    ```

2.  **Jalankan Aplikasi:**
    Karena proyek ini ditulis dengan Python standar tanpa dependensi eksternal, Anda dapat menjalankannya langsung dari direktori `src`.
    ```bash
    python3 src/main.py
    ```

## Penggunaan

Setelah Anda menjalankan aplikasi, simulasi akan dimulai di terminal Anda. Simulasi ini akan:
1.  Membuat profil pengguna sampel.
2.  Menghasilkan data biometrik (detak jantung dan tingkat kelelahan) secara acak untuk mensimulasikan pembacaan sensor waktu nyata.
3.  Menerapkan filter audio dan visual berdasarkan data yang dihasilkan.
4.  Mencetak status "sebelum" dan "sesudah" ke konsol untuk menunjukkan cara kerja filter.

Contoh output:
Iterasi 1: Detak Jantung=85 bpm, Kelelahan=4/10 Kondisi Awal: Audio={'high_freq_volume': 100}, Visual={'text_sharpness': 5.0} Kondisi Disesuaikan: Audio={'high_freq_volume': 100}, Visual={'text_sharpness': 5.0}

Iterasi 2: Detak Jantung=110 bpm, Kelelahan=8/10 Kondisi Awal: Audio={'high_freq_volume': 100}, Visual={'text_sharpness': 5.0} STRES TERDETEKSI (Detak Jantung: 110 bpm). Mengurangi suara frekuensi tinggi. KELELAHAN TERDETEKSI (Tingkat: 8/10). Mempertajam teks. Kondisi Disesuaikan: Audio={'high_freq_volume': 50.0}, Visual={'text_sharpness': 7.0}


## Menjalankan Pengujian

Proyek ini dilengkapi dengan serangkaian pengujian unit untuk memastikan fungsionalitas yang benar. Untuk menjalankan pengujian, gunakan perintah berikut dari direktori root:
```bash
python3 tests/test_app.py
Kontribusi
Kami menyambut baik kontribusi untuk Personal Reality Filter! Jika Anda tertarik untuk berkontribusi, silakan fork repositori dan ajukan pull request. Untuk perubahan besar, harap buka isu terlebih dahulu untuk membahas apa yang ingin Anda ubah.

Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT.
