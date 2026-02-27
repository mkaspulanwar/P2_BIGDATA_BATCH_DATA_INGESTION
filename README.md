# PRAKTIKUM 2 BATCH DATA INGESTION & PROCESSING WITH SPARK

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img alt="PySpark" src="https://img.shields.io/badge/PySpark-000000?style=for-the-badge&logo=apachespark&logoColor=white" />
  <img alt="Java 17" src="https://img.shields.io/badge/Java%2017-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" />
  <img alt="Parquet" src="https://img.shields.io/badge/Parquet-50B848?style=for-the-badge&logo=apache&logoColor=white" />
  <img alt="Ubuntu Environment" src="https://img.shields.io/badge/Ubuntu%20Environment-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" />
  <img alt="venv" src="https://img.shields.io/badge/.venv-306998?style=for-the-badge&logo=python&logoColor=white" />
</p>

## Deskripsi Praktikum

Praktikum Week 2 ini berfokus pada Batch Data Ingestion dan Processing menggunakan Apache Spark melalui PySpark dengan pendekatan enterprise workflow. Kamu memproses dataset transaksi e commerce dari format CSV dengan tahap ingestion, pembersihan dan validasi data, transformasi, serta agregasi untuk menghasilkan metrik bisnis yang siap analitik. Hasil pemrosesan disimpan ke Data Lake berlapis raw clean curated menggunakan format Parquet yang lebih efisien, sekaligus menerapkan partitioning agar pembacaan data lebih optimal. Seluruh pekerjaan dijalankan di Ubuntu environment melalui WSL dan dikembangkan dengan VS Code Remote WSL, serta menggunakan Python venv untuk menjaga dependency tetap rapi dan konsisten.

---

## Tim Developer

| Peran | Nama | NIM | Profil GitHub |
| :--- | :--- | :--- | :--- |
| **Pengembang Proyek** | M. Kaspul Anwar | 230104040212 | [![](https://img.shields.io/badge/GitHub-M.KaspulAnwar-181717?style=flat&logo=github)](https://github.com/mkaspulanwar) |
| **Dosen Pengampu** | Muhayat, M. IT | - | [![](https://img.shields.io/badge/GitHub-Muhayat,M.IT-181717?style=flat&logo=github)](https://github.com/muhayat-lab) |

---

## Tujuan Praktikum
Setelah praktikum ini, kamu diharapkan mampu:

1. Menggunakan **Linux environment melalui WSL** sebagai lingkungan kerja data engineering yang menyerupai server production.
2. Mengintegrasikan **VS Code Remote WSL** agar proses coding di Windows tetapi eksekusi dan file system berjalan di Linux environment.
3. Mengelola **Python virtual environment (venv)** untuk menjaga dependency project tetap konsisten, rapi, dan reproducible.
4. Mengimplementasikan **batch ingestion** menggunakan Spark, mulai dari membaca data CSV skala besar menjadi DataFrame.
5. Melakukan **data cleaning dan transformation** secara terstruktur untuk meningkatkan kualitas data sebelum dianalisis.
6. Mendesain struktur **Data Lake berlapis** dengan konsep **Raw Clean Curated** agar data mudah ditelusuri, diaudit, dan dipelihara.
7. Menggunakan format **Parquet** sebagai output utama untuk efisiensi ukuran file dan kecepatan baca pada analitik.
8. Menerapkan **partitioning strategy** untuk mengoptimalkan performa query dan meminimalkan I O melalui partition pruning.
9. Menghasilkan pipeline yang lebih **enterprise ready**, bukan sekadar script berjalan, tetapi memiliki alur jelas, output terstandar, dan praktik terbaik pengolahan data.

---

## Gambaran Arsitektur Pipeline
Pipeline yang dibangun mengikuti alur batch processing berlapis. Alur ini memisahkan data berdasarkan tingkat “kematangan” data sehingga setiap layer punya fungsi yang jelas.

### Diagram Pipeline
```text
                 ┌──────────────────────────┐
                 │   CSV Source Dataset      │
                 │   ecommerce_raw.csv       │
                 └─────────────┬────────────┘
                               │
                               ▼
                 ┌──────────────────────────┐
                 │        RAW LAYER          │
                 │   data/raw (CSV)          │
                 │   Data mentah disimpan    │
                 └─────────────┬────────────┘
                               │
                               ▼
                 ┌──────────────────────────┐
                 │  CLEANING & VALIDATION    │
                 │  - drop duplicates        │
                 │  - handle nulls           │
                 │  - filter nilai invalid   │
                 │  - parse tanggal          │
                 └─────────────┬────────────┘
                               │
                               ▼
                 ┌──────────────────────────┐
                 │     TRANSFORMATION        │
                 │  - feature engineering    │
                 │  - contoh: total_amount   │
                 └─────────────┬────────────┘
                               │
                               ▼
                 ┌──────────────────────────┐
                 │       CLEAN LAYER         │
                 │   data/clean (Parquet)    │
                 │   Data bersih & konsisten │
                 └─────────────┬────────────┘
                               │
                               ▼
                 ┌──────────────────────────┐
                 │ CURATED LAYER (AGGREGATE) │
                 │ data/curated (Parquet)    │
                 │ - revenue per category    │
                 │ - top products            │
                 │ - avg transaction/customer│
                 └─────────────┬────────────┘
                               │
                               ▼
                 ┌──────────────────────────┐
                 │   PARTITIONED DATA LAKE   │
                 │  clean/partitioned_by_*   │
                 │  Optimasi query & storage │
                 └──────────────────────────┘
```
## Konsep yang Dipakai
1. Batch Processing: data diproses dalam satu run (tidak real time).
2. Distributed Computing: Spark membagi pekerjaan ke beberapa core/worker (di praktikum ini local mode).
3. Medallion Architecture: Raw (bronze), Clean (silver), Curated (gold) untuk memisahkan kualitas dan fungsi data.
4. Columnar Storage (Parquet): format kolom yang efisien untuk analitik dan kompresi.
5. Partition Pruning: optimasi baca saat query hanya membaca partisi yang relevan.

## Struktur Folder Project
Struktur folder mengikuti standar data lake berlapis agar alur kerja jelas dan mudah dikembangkan.
```markdown
bigdata-project/
├── .venv
├── screenshots
├── data/
│   ├── raw/                          # Data mentah (CSV) sebagai source of truth
│   ├── clean/                        # Data bersih (Parquet) termasuk output partisi
│   │   ├── parquet/                  # Output clean utama dalam Parquet
│   │   └── partitioned_by_category/  # Output clean yang dipartisi (contoh: category)
│   └── curated/                      # Dataset terkurasi (hasil agregasi/metrik bisnis)
│       ├── category_revenue/         # Revenue per category
│       ├── top_products/             # Top produk terlaris
│       └── avg_transaction/          # Rata-rata transaksi per customer
├── logs/                             # Log eksekusi pipeline untuk debugging dan audit
└── scripts/                          # Script PySpark pipeline
    └── batch_pipeline_enterprise.py  # Script utama Week 2
```
