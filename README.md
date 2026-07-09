# Analisis CSAT Google Maps Reviews Tomoro Coffee di Samarinda

Analisis kepuasan pelanggan (Customer Satisfaction Score / CSAT) 5 cabang Tomoro Coffee di Samarinda, menggunakan data ulasan Google Maps yang diambil secara mandiri dengan web scraping. Project ini mencakup keseluruhan alur data analyst: pengambilan data, pembersihan, analisis, hingga penyampaian rekomendasi bisnis dalam bentuk presentasi.

> **Status:** Selesai — 10 Juli 2026
> **Analis:** Rahel ([@Rahelxv](https://github.com/Rahelxv))

---

## 1. Latar Belakang

Tomoro Coffee adalah jaringan gerai kopi *new retail* yang tumbuh pesat di Indonesia sejak 2022, dengan model bisnis yang menggabungkan transaksi online (aplikasi) dan offline (gerai). Karena tidak ada akses ke data survei kepuasan pelanggan internal perusahaan, project ini menggunakan **rating dan ulasan Google Maps** sebagai proxy CSAT — sumber yang dianggap cukup objektif karena diberikan secara sukarela oleh pelanggan tanpa arahan perusahaan.

## 2. Tugas Bisnis (Business Task)

> Menganalisis faktor-faktor yang mempengaruhi skor CSAT tiap cabang Tomoro Coffee di Samarinda untuk merumuskan rekomendasi perbaikan operasional yang spesifik per lokasi.

**Pertanyaan yang dijawab:**
- Berapa CSAT tiap cabang Tomoro Coffee di Samarinda?
- Apakah ada tren perbaikan CSAT dari waktu ke waktu?
- Variabel bisnis apa yang paling mempengaruhi skor CSAT pelanggan?

**Indikator keberhasilan:**
- Dapat mengidentifikasi faktor-faktor yang paling mempengaruhi skor CSAT.
- Dapat mengajukan rekomendasi perbaikan langsung pada variabel-variabel terkait.

## 3. Metodologi

Project ini mengikuti kerangka kerja data analytics **Ask → Prepare → Process → Analyze → Share**:

| Tahap | Deskripsi |
| --- | --- |
| **Ask** | Merumuskan pertanyaan bisnis dan tugas analisis berdasarkan matrik CSAT |
| **Prepare** | Mengambil data ulasan & profil bisnis dari Google Maps (Scrapy-Playwright), serta data pendukung kepadatan penduduk dari BPS Samarinda |
| **Process** | Menyatukan, membersihkan, dan melakukan rekayasa fitur pada data (Pandas) |
| **Analyze** | Menghitung skor CSAT per cabang, analisis kuadran, analisis tren (moving average), dan analisis kategori komplain |
| **Share** | Menyusun temuan dan rekomendasi aksi dalam bentuk presentasi PowerPoint |

## 4. Data

| Data | Sumber | Jumlah | Keterangan |
| --- | --- | --- | --- |
| Profil bisnis 5 cabang | Google Maps (Scrapy-Playwright) | 5 baris | Alamat, nomor HP, Instagram, total rating, total review |
| Ulasan pelanggan | Google Maps (Scrapy-Playwright) | 1.558 baris | Rating, teks review, kategori rating opsional Google (Makanan, Layanan, Suasana, dll.) |
| Kepadatan penduduk per kecamatan | [BPS Kota Samarinda](https://samarindakota.bps.go.id/) | — | Data pendukung analisis geografis |

Data diambil pada 23–26 Juni 2026. Detail proses pembersihan dan pengambilan data ada di [`Langkah teknis dan analisis yang diambil dalam project (Proses).pdf`](./reports/Langkah%20teknis%20dan%20analisis%20yang%20diambil%20dalam%20project%20(Proses).pdf) — dokumentasi teknis lengkap dari tahap Ask hingga Share.

## 5. Ringkasan Temuan Utama

- **CSAT gabungan seluruh cabang: 91.01%** — di atas benchmark global CSAT industri (78%, Salesforce).
- Skor CSAT antar cabang bervariasi cukup lebar: **Sebatik (93.73%)** tertinggi, **M Yamin (86.84%)** terendah — disparitas ± 7%.
- **Analisis kuadran** (Total Ulasan × Skor CSAT):
  - *Model pembelajaran*: Merak Square, Sebatik
  - *Evaluasi total*: M Yamin
  - *Perbatasan berisiko*: PM Noor, Bung Tomo
- Dua variabel bisnis yang paling sering muncul di keluhan pelanggan di **semua cabang** adalah **Layanan** dan **Fasilitas** (terutama toilet dan WiFi) — bukan kualitas makanan/minuman.
- Prioritas perbaikan: **M Yamin** dan **PM Noor**, karena kombinasi tren CSAT menurun dan kontribusi masalah layanan/fasilitas yang tinggi.

Detail lengkap analisis kuadran, tren, dan rekomendasi per cabang ada di dokumentasi proses dan presentasi akhir.

## 6. Struktur Repository

```
.
├── scrapy/    # Dua sub-project Scrapy-Playwright untuk mengambil data dari Google Maps
├── file/      # Seluruh file data mentah & hasil pembersihan (csv, xlsx, parquet)
├── code/      # Notebook Python untuk pembersihan, penyatuan, dan analisis data
├── reports/   # Presentasi akhir (PowerPoint) & ringkasan temuan untuk stakeholder bisnis
└── Analisis_CSAT_..._pdf   # Presentasi akhir
```

Setiap folder punya README sendiri dengan penjelasan lebih detail:

| Folder | Isi | README |
| --- | --- | --- |
| `scrapy/` | Web scraper Scrapy-Playwright (data bisnis & review) | [scrapy/README.md](./scrapy/README.md) |
| `file/` | Dataset mentah & hasil pembersihan | [file/README.md](./file/README.md) |
| `code/` | Notebook analisis Python | [code/README.md](./code/README.md) |
| `reports/` | Deliverable akhir untuk stakeholder | [reports/README.md](./reports/README.md) |

## 7. Tools & Tech Stack

| Kategori | Tools |
| --- | --- |
| Web Scraping | Scrapy, Scrapy-Playwright |
| Data Processing | Python, Pandas |
| Visualisasi | Matplotlib, Seaborn |
| Penyimpanan Data | CSV, XLSX, Parquet |
| Presentasi | PowerPoint |
| Dokumentasi Proses | Google Docs |

## 8. Batasan & Catatan Metodologis

- CSAT dihitung sebagai proxy dari rating Google Maps (rating 4–5 = puas, 3 = netral, 1–2 = tidak puas), bukan dari survei kepuasan resmi Tomoro Coffee.
- Total ulasan tidak selalu mencerminkan jumlah total pengunjung — bisa dipengaruhi lama gerai beroperasi.
- Beberapa kolom data dengan baris valid < 30 (mengacu pada Central Limit Theorem sebagai ambang validitas statistik minimum) dihapus dari analisis.
- Dua cabang (Bung Tomo, M Yamin) baru buka dalam 6–11 bulan terakhir sehingga rentang data historisnya lebih pendek dibanding tiga cabang lain.

## 9. Author

**Rahel** — Data Analyst (portfolio project)
GitHub: [@Rahelxv](https://github.com/Rahelxv)

---

*Project ini dibuat sebagai bagian dari portofolio data analyst dan tidak berafiliasi resmi dengan Tomoro Coffee.*
