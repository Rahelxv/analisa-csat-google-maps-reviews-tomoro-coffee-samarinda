# `scrapy-google-maps-reviews-business/`

Sub-project Scrapy untuk mengambil **data profil bisnis** dari 5 cabang Tomoro Coffee di Samarinda melalui Google Maps.

## Data yang Diambil

| Field | Keterangan |
| --- | --- |
| `nama` | Nama gerai/cabang |
| `rating_review` | Total rating & total jumlah review (digabung, dipisah saat proses cleaning) |
| `alamat` | Alamat lengkap gerai |
| `nomor_hp` | Nomor telepon gerai (jika tersedia) |
| `instagram` | Akun Instagram gerai (jika tersedia) |

## Output

Hasil scraping disimpan sebagai:
[`../../file/bisnis-profile-tomoro-samarinda.csv`](../../file/bisnis-profile-tomoro-samarinda.csv)

Total: **5 baris** (satu per cabang Tomoro Coffee Samarinda).

