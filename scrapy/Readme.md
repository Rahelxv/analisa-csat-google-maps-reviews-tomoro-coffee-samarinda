# `scrapy/` — Web Scraping Pipeline

Folder ini berisi dua sub-project Scrapy terpisah yang digunakan untuk mengambil seluruh data mentah project ini dari Google Maps, berdasarkan pencarian **"Tomoro Coffee Samarinda"** (5 cabang ditemukan).

Kedua project menggunakan **Scrapy** dikombinasikan dengan **[scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright)** agar bisa merender halaman JavaScript dinamis Google Maps dan mensimulasikan perilaku scrolling manusia, guna mengurangi risiko diblokir.

## Struktur

```
scrapy/
├── scrapy-google-maps-reviews-business/   # Scraper data profil bisnis tiap cabang
└── scrapy-google-maps-all-reviews/        # Scraper seluruh ulasan pelanggan tiap cabang
```

| Sub-project | Target Data | Output |
| --- | --- | --- |
| [`scrapy-google-maps-reviews-business/`](./scrapy-google-maps-reviews-business) | Alamat, nomor HP, Instagram, total rating, total review per cabang | `file/bisnis-profile-tomoro-samarinda.csv` |
| [`scrapy-google-maps-all-reviews/`](./scrapy-google-maps-all-reviews) | Seluruh ulasan pelanggan (nama, rating, waktu, teks review, kategori rating opsional Google) | `file/samarinda-tomorow-rev-overnight.xlsx` |

## Kenapa 2 project terpisah?

Data bisnis dan data review Google Maps butuh strategi navigasi halaman yang berbeda (halaman profil bisnis vs. panel ulasan dengan infinite scroll), sehingga dipisah menjadi 2 spider/project agar masing-masing lebih mudah di-maintain dan didebug.

## Catatan Eksekusi

- Total waktu eksekusi kedua project: **± 6 jam**.
- Waktu ini bisa dipangkas dengan mempercepat interval scroll Playwright, namun ada trade-off risiko IP/session diblokir oleh Google Maps.
- Data diambil pada rentang **23–26 Juni 2026**.
