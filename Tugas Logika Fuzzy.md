
TUGAS LOGIKA FUZZY








Eka Yuliana Rizky
240306011




Program Studi Teknologi Informasi
Fakultas Dakwah dan Ilmu Komunikasi
Universitas Islam Negeri Mataram
2026



Pertemuan2TopikFungsi Keanggotaan Variabel Usia Menggunakan Fungsi Triangle Repository-Tanggal13 September 2026	
Fungsi keanggotaan segitiga dibentuk dari dua garis lurus:
- Garis Naik: dari titik bawah kiri ke puncak
- Garis Turun: dari puncak ke titik bawah kanan
Rumus Persamaan Garis Lurus:
(y ? y?) / (y? ? y?) = (x ? x?) / (x? ? x?)
- x = Usia (tahun)
- y = Nilai Keanggotaan
- (x?, y?) = titik awal garis
- (x?, y?) = titik akhir garis
A. PERSAMAAN FUNGSI KEANGGOTAAN
  1. Bayi / Anak Usia Dini (0 – 5 tahun)
Titik: (0, 0) --> (2,5, 1) --> (5, 0)
Garis Naik (0 < x ? 2,5):
(y ? 0) / (1 ? 0) = (x ? 0) / (2,5 ? 0)  -->  y = (x ? 0) / 2,5
Garis Turun (2,5 < x < 5):
(y ? 1) / (0 ? 1) = (x ? 2,5) / (5 ? 2,5)  -->  y = (5 ? x) / 2,5

2. Anak-anak (6 – 11 tahun)
Titik: (6, 0) --> (8,5, 1) --> (11, 0)
Garis Naik (6 < x ? 8,5):
(y ? 0) / (1 ? 0) = (x ? 6) / (8,5 ? 6)  -->  y = (x ? 6) / 2,5
Garis Turun (8,5 < x < 11):
(y ? 1) / (0 ? 1) = (x ? 8,5) / (11 ? 8,5)  -->  y = (11 ? x) / 2,5
3. Remaja / Adolescent (10 – 19 tahun)
Titik: (10, 0) --> (14,5, 1) --> (19, 0)
Garis Naik (10 < x ? 14,5):
(y ? 0) / (1 ? 0) = (x ? 10) / (14,5 ? 10)  -->  y = (x ? 10) / 4,5
Garis Turun (14,5 < x < 19):
(y ? 1) / (0 ? 1) = (x ? 14,5) / (19 ? 14,5)  -->  y = (19 ? x) / 4,5
Contoh Perhitungan Usia 13 Tahun:
x = 13  -->  y = (13 ? 10) / 4,5 = 3 / 4,5 = 0,67
4. Pemuda / Youth (15 – 24 tahun)
Titik: (15, 0) --> (19,5, 1) --> (24, 0)
Garis Naik (15 < x ? 19,5):
(y ? 0) / (1 ? 0) = (x ? 15) / (19,5 ? 15)  -->  y = (x ? 15) / 4,5
Garis Turun (19,5 < x < 24):
(y ? 1) / (0 ? 1) = (x ? 19,5) / (24 ? 19,5)  -->  y = (24 ? x) / 4,5
5. Dewasa / Adult (20 – 65 tahun)
Titik: (20, 0) --> (42,5, 1) --> (65, 0)
Garis Naik (20 < x ? 42,5):
(y ? 0) / (1 ? 0) = (x ? 20) / (42,5 ? 20)  -->  y = (x ? 20) / 22,5
Garis Turun (42,5 < x < 65):
(y ? 1) / (0 ? 1) = (x ? 42,5) / (65 ? 42,5)  -->  y = (65 ? x) / 22,5
6. Lanjut Usia / Lansia (? 60 tahun)
Titik: (60, 0) --> (70, 1) --> (80, 0)
Garis Naik (60 < x ? 70):
(y ? 0) / (1 ? 0) = (x ? 60) / (70 ? 60)  -->  y = (x ? 60) / 10
Garis Turun (70 < x < 80):
(y ? 1) / (0 ? 1) = (x ? 70) / (80 ? 70)  -->  y = (80 ? x) / 10
B. GRAFIK KEANGGOTAAN
KategoriA (x?, y?)B (x?, y?)C (x?, y?)Bayi / Anak Usia Dini(0, 0)(2,5, 1)(5, 0)Anak-anak(6, 0)(8,5, 1)(11, 0)Remaja / Adolescent(10, 0)(14,5, 1)(19, 0)Pemuda / Youth(15, 0)(19,5, 1)(24, 0)Dewasa / Adult(20, 0)(42,5, 1)(65, 0)Lanjut Usia / Lansia(60, 0)(70, 1)(80, 0)Gambar 1. Fungsi Keanggotaan Bayi / Anak Usia Dini


     Gambar 2. Fungsi Keanggotaan Anak-anak
Gambar 3. Fungsi Keanggotaan Remaja / Adolescent

Gambar 4. Fungsi Keanggotaan Pemuda / Youth


     Gambar 5. Fungsi Keanggotaan Dewasa / Adult
     
     
     Gambar 6. Fungsi Keanggotaan Lanjut Usia / Lansia
     
     
     
C. KESIMPULAN
  Berdasarkan pembahasan yang telah dilakukan, fungsi keanggotaan pada variabel usia dapat direpresentasikan menggunakan fungsi keanggotaan segitiga. Setiap kategori usia memiliki titik awal, titik puncak, dan titik akhir yang digunakan untuk menentukan derajat keanggotaan suatu usia. Nilai derajat keanggotaan berada pada rentang 0 sampai 1, dengan nilai 1 berada pada titik puncak dan nilai 0 berada pada batas bawah serta batas atas.
  Adanya tumpang tindih antar kategori usia merupakan bagian dari konsep logika fuzzy, sehingga satu nilai usia dapat memiliki derajat keanggotaan pada lebih dari satu kategori. Dengan menggunakan fungsi keanggotaan ini, suatu usia dapat ditentukan tingkat keanggotaannya terhadap masing-masing kategori secara lebih fleksibel sesuai dengan karakteristik logika fuzzy.
  
Logika Fuzzy
Eka Yuliana Rizky

