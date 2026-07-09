# `code/` — Notebook Analisis

Folder ini berisi notebook Python (Jupyter) yang digunakan pada tahap **Process** dan **Analyze** dari project ini.

## Daftar Notebook

| Notebook | Tahap | Deskripsi |
| --- | --- | --- |
| `Proses Pembersihan dan Penyatuan Data.ipynb` | Process | Menyatukan data review multi-sheet, pembersihan tiap kolom (tipe data, nilai kosong, kategori), rekayasa fitur (kolom `cafe`, `Tingkat Kepuasan`, pemecahan kolom `rating_review`, kolom `Kecamatan`), serta menyimpan hasil bersih ke format Parquet |
| Costumer Satisfaction Score (CSAT) Analysis.ipynb | Analyze | Perhitungan skor CSAT per cabang, analisis kuadran (Total Ulasan × CSAT), analisis tren dengan moving average, dan analisis kategori komplain (Layanan, Fasilitas, Suasana, Makanan/Minuman) |


## Ringkasan Proses per Notebook

### Pembersihan & Penyatuan Data
- Menyatukan seluruh sheet review (per cabang) menjadi satu dataframe dengan kolom `cafe` sebagai penanda cabang.
- Membersihkan 26 kolom mentah, termasuk konversi tipe data (`float` → `Int64` untuk kolom rating opsional, `object` → `category`/`string`), serta mengubah `waktu_relatif` menjadi format `datetime` (acuan tanggal pengambilan data: **26 Juni 2026**).
- Menambah kolom rekayasa fitur `Tingkat Kepuasan` (Puas / Netral / Tidak Puas berdasarkan rating 1–5).
- Menghapus kolom dengan data valid < 30 baris (ambang berdasarkan *Central Limit Theorem*), kecuali dipertimbangkan konteks bisnisnya secara khusus.
- Membersihkan data profil bisnis: standardisasi nama cabang, memisahkan kolom rating & jumlah review, membuat kolom `Kecamatan` dari alamat.
- Menyimpan hasil akhir ke format **Parquet** untuk mempertahankan tipe data.

### Analisis CSAT 
- Perhitungan skor CSAT per cabang & gabungan.
- Analisis kuadran (Total Ulasan vs. Skor CSAT) untuk kategorisasi cabang.
- Analisis tren CSAT sepanjang waktu (tahunan & bulanan) dengan moving average.
- Multi-label one-hot encoding manual pada teks review untuk kategori Pelayanan, Fasilitas, Suasana, Makanan/Minuman.

## Dependencies

```
pandas
numpy
matplotlib
seaborn
pyarrow      # untuk membaca/menulis Parquet
```
```

Jalankan notebook pembersihan terlebih dahulu sebelum notebook analisis, karena notebook analisis membaca dataset hasil pembersihan (`.parquet`) dari folder [`file/`](../file).
