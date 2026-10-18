# Simple Information Retrieval (IR) Web Engine - VSM & TF-IDF

Aplikasi Web *Search Engine* mandiri berbasis **Python (Flask)** yang mengimplementasikan metode **Vector Space Model (VSM)** dan pembobotan **TF-IDF** (*Term Frequency-Inverse Document Frequency*). Proyek ini dikembangkan untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah Sistem Temu Kembali Informasi.

---

## Fitur Utama Aplikasi

Aplikasi ini dibagi menjadi 4 fitur utama sesuai dengan standar spesifikasi fungsional:

### Fitur 1: Dashboard Pencarian & Upload Dataset
<p align="center">
  <img width="100%" alt="Dashboard & Upload" src="https://github.com/user-attachments/assets/5045f303-3a02-4dd3-b679-9b6e67cb4fc9" />
</p>

* **Pencarian Cepat:** Antarmuka pencarian interaktif yang dilengkapi placeholder *"Masukkan Kata"*, tombol aksi, serta tombol *Reset* untuk mengembalikan state pencarian.
* **Multi-File Upload:** Mendukung pengunggahan berkas korpus bertahap berformat CSV (memungkinkan pengunggahan multi-file hingga mencapai target 1.000 dokumen).
* **Indikator Kapasitas Korpus:** Dilengkapi dengan *Progress Bar* dinamis untuk memantau kapasitas jumlah dokumen korpus yang aktif terindeks secara *real-time*.

---

### Fitur 2: Preprocessing Pipeline
<p align="center">
  <img width="100%" alt="Preprocessing Pipeline" src="https://github.com/user-attachments/assets/c7dcaf99-b1fb-4a4e-a1f3-5428113e2858" />
</p>

Menampilkan audit visual tahapan pemrosesan teks secara transparan dan sistematis:
* **Case Folding:** Proses normalisasi seluruh teks menjadi huruf kecil (*lowercase*).
* **Cleaning:** Membersihkan dan menghapus karakter non-alfabet, tanda baca, serta angka.
* **Tokenizing:** Memecah kalimat atau *string* mentah menjadi satuan term dasar.
* **Stopword Removal:** Penyaringan kata umum yang tidak penting menggunakan kamus dwibahasa (Bahasa Indonesia & Inggris).
* **Stemming:** Pengembalian kata berimbuhan ke bentuk kata dasar menggunakan *Sastrawi* dan *Porter Stemmer*.

---

### Fitur 3: Mesin Hitung VSM & Bobot TF-IDF (Backend Engine)
<p align="center">
  <img width="100%" alt="Mesin Hitung VSM" src="https://github.com/user-attachments/assets/5617d50f-8af2-462f-97a6-9f9c13d70bb6" />
</p>

* **Kalkulasi Matematis:** Menghitung frekuensi kemunculan term dalam dokumen ($\text{TF}$) serta nilai kebalikan frekuensi dokumen ($\text{IDF}$).
* **Matriks Pembobotan & Vektor Kueri:** Menampilkan tabel matriks pembobotan akhir $W_{t,d}$ serta rincian panjang norma vektor kueri ($\lVert Q \rVert$) secara transparan.

---

### Fitur 4: Hasil Pencarian (Ranking Dokumen)
<p align="center">
  <img width="100%" alt="Hasil Pencarian" src="https://github.com/user-attachments/assets/b67a4e40-2c87-430a-9f3f-23e8338939ca" />
</p>

* **Algoritma Cosine Similarity:** Melakukan perangkingan dokumen secara otomatis berdasarkan tingkat kemiripan vektor tertinggi antara kueri dan dokumen korpus.
* **Metadata & Matched Terms:** Menampilkan cuplikan informasi jurnal lengkap (Judul ber-link aktif, Nama Jurnal, Penulis, Tahun Terbit, DOI, URL, skor kemiripan, dan *matched terms* atau kata kunci yang cocok).
