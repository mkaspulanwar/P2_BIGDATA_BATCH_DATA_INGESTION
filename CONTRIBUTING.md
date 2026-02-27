# Contributing Guide

Terima kasih sudah tertarik untuk berkontribusi ke repository **P2_BIGDATA_BATCH_DATA_INGESTION**. Dokumen ini menjelaskan cara berkontribusi, standar penulisan kode, struktur perubahan yang diterima, serta aturan penting terkait dataset dan environment agar repository tetap rapi dan mudah direplikasi oleh orang lain. 

---

## Ruang Lingkup Kontribusi

Kontribusi yang paling relevan untuk project praktikum ini antara lain:

1. Perbaikan dokumentasi (README, penjelasan langkah setup, troubleshooting)
2. Perbaikan script pipeline (cleaning, transformasi, agregasi, struktur output)
3. Peningkatan reproducibility (requirements, petunjuk venv, catatan versi)
4. Penambahan contoh verifikasi hasil (cek output Parquet, partisi, schema)
5. Penataan folder dan file agar lebih rapi (tanpa mengubah tujuan praktikum)
6. Perbaikan minor bug dan peningkatan kualitas kode (tanpa mengubah output utama)

---

## Aturan Penting Sebelum Kontribusi

### 1) Jangan commit environment lokal
Jangan pernah commit folder environment seperti:
1. `.venv/` atau `venv/`
2. cache Python `__pycache__/`
3. file IDE/OS seperti `.vscode/`, `.idea/`, `Thumbs.db`, `.DS_Store`

Jika folder `.venv` terlanjur ada di repo, kontribusi yang baik adalah memastikan `.gitignore` mengabaikan environment tersebut dan repository tidak “membengkak”. 

### 2) Jangan commit dataset mentah besar (raw data)
1. File seperti `data/raw/ecommerce_raw.csv` umumnya berukuran besar dan tidak ideal untuk disimpan di GitHub.
2. Jika perlu contoh data, gunakan dataset kecil (sample) atau dokumentasikan cara mendapatkan dataset.

### 3) Output hasil eksekusi tidak perlu masuk repo
Folder output seperti:
1. `data/clean/`
2. `data/curated/`
3. `logs/` (kecuali contoh log kecil untuk demonstrasi)
sebaiknya tidak di-commit kecuali ada instruksi khusus dari dosen atau memang dibutuhkan untuk penilaian.

### 4) Screenshots boleh, tapi terstruktur
Boleh menambahkan screenshot sebagai bukti praktikum, tapi:
1. Simpan di folder `screenshots/` (atau folder bukti yang sudah ada)
2. Beri nama file konsisten dan jelas (mis. `01-run-pipeline.png`)

---

## Cara Berkontribusi

### 1) Fork repository
1. Buka repository ini di GitHub
2. Klik tombol **Fork**
3. Repository akan tersalin ke akun GitHub kamu

### 2) Clone hasil fork
```bash
git clone https://github.com/<username_kamu>/P2_BIGDATA_BATCH_DATA_INGESTION.git
cd P2_BIGDATA_BATCH_DATA_INGESTION
```
### 3) Buat branch baru
Gunakan branch terpisah untuk setiap perubahan.
```bash
git checkout -b feat/nama-fitur
# atau
git checkout -b fix/nama-bug
# atau
git checkout -b docs/perbaikan-readme
```
### 4) Jalankan project secara lokal (rekomendasi)
Kontribusi dianggap baik jika perubahan kamu bisa dijalankan ulang di environment yang sama.
Rekomendasi environment:
1. Windows + WSL (Ubuntu environment)
2. Python venv
3. Java 17
4. PySpark
Jika kontribusi kamu menyentuh pipeline, pastikan:
1. Script bisa dieksekusi
2. Output terbentuk sesuai struktur data lake
3. Tidak ada error runtime

### 5) Commit dengan pesan yang jelas
Gunakan pesan commit ringkas dan deskriptif:
```bash
git add .
git commit -m "docs: perjelas langkah setup WSL dan venv"
# atau
git commit -m "fix: tangani null pada kolom tanggal sebelum parsing"
```
### 6) Push branch ke fork kamu
```bash
git push origin feat/nama-fitur
```
### 7) Buat Pull Request (PR)
1. Buka repository fork kamu di GitHub
2. Klik Compare & pull request
3. Isi deskripsi PR dengan jelas (lihat template di bawah)
4. Kirim PR ke branch main repository ini

## Template Deskripsi Pull Request
Gunakan format ini agar PR mudah direview:

Ringkasan perubahan
1. Jelaskan perubahan secara singkat (2–5 bullet)

Alasan perubahan
1. Mengapa perubahan ini diperlukan
2. Bug apa yang diperbaiki atau kualitas apa yang ditingkatkan

Cara verifikasi
1. Perintah yang dijalankan
2. Output yang diharapkan
3. Screenshot (jika relevan)

Catatan tambahan
1. Dampak terhadap struktur folder, output, atau dependency

## Standar Kode dan Gaya Penulisan

Python (scripts)
1. Gunakan penamaan yang jelas dan konsisten
2. Hindari hardcode path absolut; gunakan relative path dari root project
3. Tambahkan komentar pada bagian yang “rawan salah paham”
4. Jika menambah fungsi baru, usahakan modulable dan mudah dibaca

Logging & Output
1. Jika menambah logging, pastikan tidak terlalu “berisik”
2. Pastikan output tetap tersimpan pada folder layer yang benar (raw/clean/curated)

Dokumentasi
1. Gunakan bahasa Indonesia yang jelas
2. Hindari paragraf terlalu panjang
3. Jika menambah command, pastikan command bisa di-copy-paste dan jalan

## Checklist Sebelum Mengirim PR

Sebelum submit PR, pastikan:
1. Perubahan tidak memasukkan `.venv/` atau `venv/`
2. Tidak menambahkan dataset mentah besar ke repo
3. Tidak menambahkan output Parquet/curated yang besar (kecuali diminta)
4. Script masih bisa dijalankan
5. README/Docs tetap mudah dibaca (tidak berantakan)
6. Pesan commit jelas dan relevan
7. PR menjelaskan cara verifikasi

## Melaporkan Bug atau Mengusulkan Ide

Jika kamu menemukan bug atau ingin mengusulkan improvement:
1. Buka tab Issues di GitHub repository ini
2. Buat issue baru dengan format:
    - Apa masalahnya
    - Langkah reproduksi
    - Expected vs actual
    - Screenshot/log (jika ada)
    - Environment (Windows/WSL, versi Python, versi Java, versi pyspark)

## Lisensi
Repository ini menggunakan MIT License. Dengan mengirim kontribusi, kamu setuju kontribusimu didistribusikan di bawah lisensi yang sama.
