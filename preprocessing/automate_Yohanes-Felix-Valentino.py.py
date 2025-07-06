import pandas as pd

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
    # Mengubah 'Churn' secara manual
    df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})

    # One-Hot Encoding untuk sisa kolom kategorikal
    df_processed = pd.get_dummies(df, drop_first=True)
    print("Encoding data kategorikal selesai.")

    # 7. Menyimpan Data yang Sudah Diproses
    df_processed.to_csv(output_path, index=False)
    print(f"Data yang sudah diproses telah disimpan di: {output_path}")

if __name__ == "__main__":
    # Definisikan path input dan output
    raw_data_path = '../namadataset_raw/WA_Fn-UseC_-Telco-Customer-Churn.csv'
    processed_data_path = '../namadataset_preprocessing/churn_data_processed.csv'

    # Jalankan fungsi preprocessing
    preprocess_data(raw_data_path, processed_data_path)