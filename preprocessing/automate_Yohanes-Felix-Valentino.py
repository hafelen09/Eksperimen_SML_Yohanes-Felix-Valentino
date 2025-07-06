# automate_Yohanes-Felix-Valentino.py

import pandas as pd
import os # <-- Tambahkan import ini

def preprocess_data(input_path, output_path):
    """
    Memuat data mentah, melakukan preprocessing, dan menyimpan hasilnya.
    """
    # 1. Memuat Dataset
    df = pd.read_csv(input_path)
    print("Data mentah berhasil dimuat.")

    # 2. Menangani TotalCharges
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # 3. Menangani Data Kosong (Missing Values)
    df.dropna(inplace=True)
    print("Nilai kosong telah ditangani.")

    # 4. Menghapus Data Duplikat
    df.drop_duplicates(inplace=True)
    print("Data duplikat telah dihapus.")

    # 5. Menghapus Kolom Tidak Relevan
    df.drop('customerID', axis=1, inplace=True)
    print("Kolom 'customerID' telah dihapus.")

    # 6. Encoding Data Kategorikal
    df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})
    df_processed = pd.get_dummies(df, drop_first=True)
    print("Encoding data kategorikal selesai.")

    # 7. Menyimpan Data yang Sudah Diproses
    # Membuat direktori output jika belum ada
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir) and output_dir != '':
        os.makedirs(output_dir)

    df_processed.to_csv(output_path, index=False)
    print(f"Data yang sudah diproses telah disimpan di: {output_path}")

if __name__ == "__main__":
    # Ganti 'telco-customer-churn_...' dengan nama folder Anda yang sebenarnya jika berbeda
    raw_data_path = 'telco-customer-churn_raw/WA_Fn-UseC_-Telco-Customer-Churn.csv'
    processed_data_path = 'telco-customer-churn_preprocessing/churn_data_processed.csv'
    
    # Jalankan fungsi preprocessing
    preprocess_data(raw_data_path, processed_data_path)
