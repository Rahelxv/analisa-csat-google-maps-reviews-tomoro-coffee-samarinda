# `scrapy-google-maps-all-reviews/`

Sub-project Scrapy untuk mengambil **seluruh ulasan pelanggan** dari 5 cabang Tomoro Coffee di Samarinda melalui Google Maps.

## Data yang Diambil

| Field | Keterangan |
| --- | --- |
| `nama_reviewer` | Nama akun Google pengulas |
| `rating` | Rating keseluruhan (1–5) |
| `waktu_relatif` | Waktu review relatif (mis. "2 hari lalu") |
| `review` | Teks review (opsional) |
| `Makanan`, `Layanan`, `Suasana` | Rating spesifik opsional dari Google (1–5) |
| `Tarif per orang`, `Tingkat kebisingan`, `Waktu tunggu`, `Jenis pesanan`, `Jenis makanan`, `Tempat parkir`, `Opsi tempat parkir`, dll. | Atribut tambahan opsional yang disediakan Google Maps |

Total kolom mentah yang diambil: **26 kolom** — total baris hasil akhir: **1.558 review**.

## Output

Setiap cabang disimpan sebagai sheet terpisah dalam satu file Excel:
[`../../file/samarinda-tomorow-rev-overnight.xlsx`](../../file/samarinda-tomorow-rev-overnight.xlsx)
