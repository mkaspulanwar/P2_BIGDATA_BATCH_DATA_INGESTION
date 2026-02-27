# Contributing Guide

Terima kasih sudah tertarik untuk berkontribusi ke repository **P2_BIGDATA_BATCH_DATA_INGESTION**. Dokumen ini menjelaskan cara berkontribusi, standar penulisan kode, struktur perubahan yang diterima, serta aturan penting terkait dataset dan environment agar repository tetap rapi dan mudah direplikasi oleh orang lain. :contentReference[oaicite:0]{index=0}

---

## Ruang Lingkup Kontribusi

Kontribusi yang paling relevan untuk project praktikum ini antara lain:

- Perbaikan dokumentasi (README, penjelasan langkah setup, troubleshooting)
- Perbaikan script pipeline (cleaning, transformasi, agregasi, struktur output)
- Peningkatan reproducibility (requirements, petunjuk venv, catatan versi)
- Penambahan contoh verifikasi hasil (cek output Parquet, partisi, schema)
- Penataan folder dan file agar lebih rapi (tanpa mengubah tujuan praktikum)
- Perbaikan minor bug dan peningkatan kualitas kode (tanpa mengubah output utama)

---

## Aturan Penting Sebelum Kontribusi

### 1) Jangan commit environment lokal
Jangan pernah commit folder environment seperti:
- `.venv/` atau `venv/`
- cache Python `__pycache__/`
- file IDE/OS seperti `.vscode/`, `.idea/`, `Thumbs.db`, `.DS_Store`

Jika folder `.venv` terlanjur ada di repo, kontribusi yang baik adalah memastikan `.gitignore` mengabaikan environment tersebut dan repository tidak “membengkak”. :contentReference[oaicite:1]{index=1}

### 2) Jangan commit dataset mentah besar (raw data)
- File seperti `data/raw/ecommerce_raw.csv` umumnya berukuran besar dan tidak ideal untuk disimpan di GitHub.
- Jika perlu contoh data, gunakan dataset kecil (sample) atau dokumentasikan cara mendapatkan dataset.

### 3) Output hasil eksekusi tidak perlu masuk repo
Folder output seperti:
- `data/clean/`
- `data/curated/`
- `logs/` (kecuali contoh log kecil untuk demonstrasi)
sebaiknya tidak di-commit kecuali ada instruksi khusus dari dosen atau memang dibutuhkan untuk penilaian.

### 4) Screenshots boleh, tapi terstruktur
Boleh menambahkan screenshot sebagai bukti praktikum, tapi:
- Simpan di folder `screenshots/` (atau folder bukti yang sudah ada)
- Beri nama file konsisten dan jelas (mis. `01-run-pipeline.png`)

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
