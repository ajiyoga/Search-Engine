# Simple Information Retrieval (IR) Web Engine - VSM & TF-IDF

Aplikasi Web *Search Engine* mandiri berbasis **Python (Flask)** yang mengimplementasikan metode **Vector Space Model (VSM)** dan pembobotan **TF-IDF** (*Term Frequency-Inverse Document Frequency*). Proyek ini dikembangkan untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah Sistem Temu Kembali Informasi.

---

## Fitur Utama Aplikasi

Aplikasi ini dibagi menjadi 4 fitur utama sesuai dengan standar spesifikasi fungsional:

### Fitur 1: Dashboard Pencarian & Upload Dataset
<img width="1910" height="912" alt="fitur 1" src="https://github.com/user-attachments/assets/adc90364-f414-43a0-97fc-227ec3ff1216" />

* **Pencarian Cepat :** Antarmuka pencarian interaktif yang dilengkapi placeholder *"Masukkan Kata"*, tombol aksi, serta tombol *Reset* untuk mengembalikan state pencarian.
* **Multi-File Upload :** Mendukung pengunggahan berkas korpus bertahap berformat CSV (memungkinkan pengunggahan multi-file hingga mencapai target 1.000 dokumen).
* **Indikator Kapasitas Korpus :** Dilengkapi dengan *Progress Bar* dinamis untuk memantau kapasitas jumlah dokumen korpus yang aktif terindeks secara *real-time*.

---

### Fitur 2: Preprocessing Pipeline
<img width="1882" height="907" alt="fitur 2" src="https://github.com/user-attachments/assets/33627d1a-1243-4720-9bd7-f311c23225e5" />

Menampilkan audit visual tahapan pemrosesan teks secara transparan dan sistematis:
* **Case Folding :** Proses normalisasi seluruh teks menjadi huruf kecil (*lowercase*).
* **Cleaning :** Membersihkan dan menghapus karakter non-alfabet, tanda baca, serta angka.
* **Tokenizing :** Memecah kalimat atau *string* mentah menjadi satuan term dasar.
* **Stopword Removal :** Penyaringan kata umum yang tidak penting menggunakan kamus dwibahasa (Bahasa Indonesia & Inggris).
* **Stemming :** Pengembalian kata berimbuhan ke bentuk kata dasar menggunakan *Sastrawi* dan *Porter Stemmer*.

---

### Fitur 3: Mesin Hitung VSM & Bobot TF-IDF (Backend Engine)
<img width="1893" height="915" alt="fitur 3" src="https://github.com/user-attachments/assets/131a39ab-9481-438a-93d6-827d353628ea" />

* **Kalkulasi Matematis :** Menghitung frekuensi kemunculan term dalam dokumen ($\text{TF}$) serta nilai kebalikan frekuensi dokumen ($\text{IDF}$).
* **Matriks Pembobotan & Vektor Kueri :** Menampilkan tabel matriks pembobotan akhir $W_{t,d}$ serta rincian panjang norma vektor kueri ($\lVert Q \rVert$) secara transparan.

---

### Fitur 4: Hasil Pencarian (Ranking Dokumen)
<img width="1891" height="907" alt="fitur 4" src="https://github.com/user-attachments/assets/fbdf1113-bcc7-4367-a524-94ac4c8cb224" />

* **Algoritma Cosine Similarity :** Melakukan perangkingan dokumen secara otomatis berdasarkan tingkat kemiripan vektor tertinggi antara kueri dan dokumen korpus.
* **Metadata & Matched Terms :** Menampilkan cuplikan informasi jurnal lengkap (Judul ber-link aktif, Nama Jurnal, Penulis, Tahun Terbit, DOI, URL, skor kemiripan, dan *matched terms* atau kata kunci yang cocok).
