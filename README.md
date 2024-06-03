# sentiment-analysis

Ini adalah aplikasi web analisis sentimen yang bertujuan untuk menampilkan hasil dari data yang di analisis dalam bentuk table data dan pie chart untuk melihat persentase data. Aplikasi ini menggunakan framework Streamlit dan data diambil dari Kaggle.

## Deskripsi

aplikasi ini menggunakan metode analisis sentimen untuk menentukan apakah suatu teks memiliki sentimen positif, negatif, atau netral. Metode yang digunakan dapat mencakup penggunaan kamus kata-kata positif dan negatif, algoritma pembelajaran mesin, atau pendekatan lainnya.

## Persiapan

1. Buat dan aktifkan lingkungan virtual.
    ```bash
    python -m venv .venv
    . .venv/Scripts/activate
    ```
2. Install dependensi aplikasi.
    ```bash
    pip install -r requirements.txt
    ```
3. Jalankan skrip app.py.
    ```bash
    stramlit run app.py
    ```