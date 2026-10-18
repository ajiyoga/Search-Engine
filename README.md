# Simple Information Retrieval (IR) Web Engine - VSM & TF-IDF
Aplikasi Web Search Engine mandiri berbasis Python (Flask) yang mengimplementasikan metode Vector Space Model (VSM) dan pembobotan TF-IDF (Term Frequency-Inverse Document Frequency). Proyek ini dikembangkan untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah Sistem Temu Kembali Informasi.
# Fitur Utama Aplikasi
Aplikasi ini dibagi menjadi 4 fitur utama sesuai dengan standar spesifikasi fungsional:
# Fitur 1: Dashboard Pencarian & Upload Dataset
<img width="1897" height="910" alt="Cuplikan layar 2026-10-15 020547" src="https://github.com/user-attachments/assets/5045f303-3a02-4dd3-b679-9b6e67cb4fc9" />
- Antarmuka pencarian cepat dengan placeholder interaktif dan tombol Reset.
- Mendukung fitur Multi-File Upload untuk file korpus bertahap berformat CSV (memungkinkan pengunggahan hingga 1.000 dokumen target).
- Indikator Progress Bar dinamis untuk memantau kapasitas dokumen korpus yang aktif terindeks.
  
# Fitur 2: Preprocessing Pipeline
<img width="1876" height="915" alt="Cuplikan layar 2026-10-15 020604" src="https://github.com/user-attachments/assets/c7dcaf99-b1fb-4a4e-a1f3-5428113e2858" />
Menampilkan audit visual tahapan pemrosesan teks secara transparan:
- Case Folding (konversi huruf kecil).
- Cleaning (penghapusan tanda baca dan angka).
- Tokenizing (pemecahan string menjadi term).
- Stopword Removal (penyaringan kata umum dwibahasa: Bahasa Indonesia & Inggris).
- Stemming (pengembalian kata ke bentuk dasar menggunakan Sastrawi dan Porter Stemmer).
  
# Fitur 3: Mesin Hitung VSM & Bobot TF-IDF (Backend Engine)
<img width="1886" height="908" alt="Screenshot (116)" src="https://github.com/user-attachments/assets/5617d50f-8af2-462f-97a6-9f9c13d70bb6" />
- Menghitung frekuensi kemunculan kata dalam dokumen (TF) dan nilai kebalikan frekuensi dokumen (IDF).
- Menampilkan matriks tabel matematis pembobotan akhir $W_{t,d}$ serta panjang norma vektor kueri ($\lVert Q \rVert$).
  
# Fitur 4: Hasil Pencarian (Ranking Dokumen)
<img width="1887" height="915" alt="Cuplikan layar 2026-10-15 020651" src="https://github.com/user-attachments/assets/b67a4e40-2c87-430a-9f3f-23e8338939ca" />
- Melakukan perangkingan dokumen secara otomatis berdasarkan tingkat kemiripan tertinggi menggunakan Cosine Similarity.
- Menampilkan cuplikan metadata jurnal lengkap (Judul, Nama Jurnal, Penulis, Tahun Terbit, DOI, URL, dan matched terms).
