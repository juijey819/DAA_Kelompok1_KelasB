# Edit Distance: Greedy vs Dynamic Programming (Levenshtein)

![Python](https://img.shields.io/badge/Python-3-blue)
![Pandas](https://img.shields.io/badge/Pandas-latest-purple)
![Matplotlib](https://img.shields.io/badge/Matplotlib-latest-green)
![Seaborn](https://img.shields.io/badge/Seaborn-latest-blueviolet)

## Anggota Kelompok:
1. Ahnaf Sega Fausta (L0224048)
2. Jalu Agil Nugroho (L0224032)
3. Irfan Akmal Muzakki (L0224049)

---
## Gambaran Umum

Repositori ini berisi implementasi dan eksperimen perbandingan **Algoritma Greedy Edit Distance** dan **Edit Distance berbasis Dynamic Programming (Levenshtein)**. Proyek ini bertujuan untuk menganalisis perbedaan **efisiensi waktu eksekusi** dan **kualitas solusi** (optimalitas jarak edit) antara pendekatan heuristik greedy dan pendekatan optimal berbasis dynamic programming.

Eksperimen dilakukan dengan membangkitkan dataset pasangan kata Bahasa Indonesia (kata asli dan kata hasil mutasi), kemudian membandingkan hasil jarak edit, waktu eksekusi, serta pola kesalahan algoritma greedy menggunakan visualisasi grafik, scatter plot, dan heatmap.

---
## Tujuan Proyek

- Membandingkan waktu eksekusi algoritma Greedy dan Dynamic Programming.
- Mengukur selisih hasil jarak edit (optimality gap) antara Greedy dan solusi optimal (DP).
- Menganalisis pola kesalahan Greedy terhadap panjang string.
- Menunjukkan konsekuensi penggunaan pendekatan heuristik pada masalah pencocokan string.

---
## Struktur Proyek

```
DAA_Kelompok1_KelasB/
├── DAA-Kelompok1.ipynb/     # Implementasi proyek dalam notebook
│ ├── data/                  # Dataset
│ │ ├── indonesian-words.txt
│ ├── generate_instances.py  # Generator instance (Rill–Fake)
│ ├── run.py                 # Benchmark Greedy vs DP
└── README.md
```

---
## Implementasi Teknis

### Bahasa dan Pustaka

- **Python 3**
- **random**: pembangkitan data acak dan reprodusibilitas eksperimen (seed = 42)
- **json, csv**: penyimpanan hasil eksperimen
- **pandas**: pengolahan dan analisis dataset
- **matplotlib**: visualisasi grafik waktu eksekusi dan error
- **seaborn**: visualisasi heatmap pola kesalahan
---
## Metodologi Eksperimen

1. Dataset dibangkitkan dari daftar kata Bahasa Indonesia dengan proses mutasi acak (insert, delete, substitute).
2. Setiap pasangan kata diuji menggunakan algoritma Greedy dan Dynamic Programming.
3. Pengukuran waktu eksekusi dilakukan dengan pengulangan sebanyak 20 kali per instance.
4. Eksperimen tambahan dilakukan dengan variasi panjang string (n = 5, 10, 20, 30).
5. Selisih hasil Greedy dan DP dianalisis menggunakan scatter plot dan heatmap.

---
## Cara Menjalanka

### Menjalankan Secara Lokal (Python)

1. Pastikan Python 3 telah terpasang.
2. Clone repositori ini menggunakan Git:

```bash
git clone https://github.com/juijey819/DAA_Kelompok1_KelasB
cd DAA_Kelompok1_KelasB
```

3. Instal dependensi yang dibutuhkan:

```bash
pip install pandas matplotlib seaborn
```

4. Bangkitkan dataset (`python generate_instances.py`).
5. Buka run.py (`python run.py`).
6. Sesuaikan untuk path dataset indonesian-words.txt. Jika diperlukan.
7. Opsional, jalankan (`DAA-Kelompok1.ipynb`) jika ingin melihat implementasi lengkap beserta visualisasi      grafik.

---

## Output dan Visualisasi

- **results.csv**: hasil jarak edit Greedy dan DP.
- **greedy_mistakes.json**: daftar kasus Greedy tidak optimal.
- Grafik perbandingan waktu eksekusi (Pada `DAA-Kelompok1.ipynb`).
- Scatter plot magnitude error (Pada `DAA-Kelompok1.ipynb`).
- Heatmap distribusi kesalahan Greedy terhadap panjang string (Pada `DAA-Kelompok1.ipynb`).

---
## Dataset

Dataset kata Bahasa Indonesia diperoleh dari repositori publik:

https://github.com/damzaky/kumpulan-kata-bahasa-indonesia-KBBI

Dataset digunakan sebagai sumber kata asli dan dimodifikasi untuk membentuk instance uji khusus penelitian ini.

---
## Etika dan Lisensi

Dataset yang digunakan bersifat publik dan tidak mengandung data pribadi. Seluruh data digunakan untuk keperluan akademik dan penelitian, dengan mencantumkan sumber secara eksplisit sebagai bentuk kepatuhan terhadap etika akademik.

