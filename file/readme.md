# `file/` — Dataset

Folder ini berisi seluruh file data mentah (hasil scraping), data pendukung eksternal, dan data hasil pembersihan yang digunakan dalam project ini.

## Daftar File

| File | Tipe | Sumber | Keterangan |
| --- | --- | --- | --- |
| `bisnis-profile-tomoro-samarinda.csv` | Mentah | [`scrapy-google-maps-reviews-business`](../scrapy/scrapy-google-maps-reviews-business) | Profil bisnis 5 cabang Tomoro Coffee Samarinda (alamat, kontak, total rating & review) |
| `samarinda-tomorow-rev-overnight.xlsx` | Mentah | [`scrapy-google-maps-all-reviews`](../scrapy/scrapy-google-maps-all-reviews) | Seluruh 1.558 ulasan pelanggan, satu sheet per cabang |
| `Penduduk, Laju Pertumbuhan Penduduk, ... Kota Samarinda, 2026.xlsx` | Eksternal | [BPS Kota Samarinda](https://samarindakota.bps.go.id/) | Data jumlah & kepadatan penduduk per kecamatan, digunakan untuk analisis pendukung geografis (cadangan lokal jika link BPS tidak dapat diakses) |

> Jika project ini juga mengekspor dataset hasil pembersihan (mis. `.parquet`), tambahkan baris untuk masing-masing file di tabel di atas — format parquet dipilih pada tahap *Process* karena mempertahankan tipe data dengan lebih baik dibanding CSV.

## Alur Data

```
Google Maps  →  scrapy/  →  file/ (data mentah)  →  code/ (cleaning & analisis)  →  file/ (data bersih, .parquet)  →  reports/
```

## Catatan

- Data review diambil dalam format multi-sheet Excel (satu sheet per cabang) dan disatukan menjadi satu dataframe pada tahap pembersihan di [`code/`](../code).
