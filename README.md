# Simple Information Retrieval (IR) Web Engine - VSM & TF-IDF
# Aplikasi Web Search Engine mandiri berbasis Python (Flask) yang mengimplementasikan metode Vector Space Model (VSM) dan pembobotan TF-IDF (Term Frequency-Inverse Document Frequency). Proyek ini dikembangkan untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah Sistem Temu Kembali Informasi.
# Fitur Utama Aplikasi
Aplikasi ini dibagi menjadi 4 fitur utama sesuai dengan standar spesifikasi fungsional:
# Fitur 1: Dashboard Pencarian & Upload Dataset
- Antarmuka pencarian cepat dengan placeholder interaktif dan tombol Reset.
- Mendukung fitur Multi-File Upload untuk file korpus bertahap berformat CSV (memungkinkan pengunggahan hingga 1.000 dokumen target).
- Indikator Progress Bar dinamis untuk memantau kapasitas dokumen korpus yang aktif terindeks.
  
# Fitur 2: Preprocessing Pipeline
Menampilkan audit visual tahapan pemrosesan teks secara transparan:
- Case Folding (konversi huruf kecil).
- Cleaning (penghapusan tanda baca dan angka).
- Tokenizing (pemecahan string menjadi term).
- Stopword Removal (penyaringan kata umum dwibahasa: Bahasa Indonesia & Inggris).
- Stemming (pengembalian kata ke bentuk dasar menggunakan Sastrawi dan Porter Stemmer).
  
# Fitur 3: Mesin Hitung VSM & Bobot TF-IDF (Backend Engine)
- Menghitung frekuensi kemunculan kata dalam dokumen (TF) dan nilai kebalikan frekuensi dokumen (IDF).
- Menampilkan matriks tabel matematis pembobotan akhir $W_{t,d}$ serta panjang norma vektor kueri ($\lVert Q \rVert$).
  
# Fitur 4: Hasil Pencarian (Ranking Dokumen)
- Melakukan perangkingan dokumen secara otomatis berdasarkan tingkat kemiripan tertinggi menggunakan Cosine Similarity.
- Menampilkan cuplikan metadata jurnal lengkap (Judul, Nama Jurnal, Penulis, Tahun Terbit, DOI, URL, dan matched terms).
