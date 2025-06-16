import pandas as pd
import numpy as np

def automate_preprocessing(df):
    # Handle 'No phone service' and 'No internet service' in categorical columns
    for col in ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']:
        df[col] = df[col].replace({'No internet service': 'No'})

    df['MultipleLines'] = df['MultipleLines'].replace({'No phone service': 'No'})

    # Convert 'TotalCharges' to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Handle missing values in 'TotalCharges' (replace with 0 or median/mean)
    df['TotalCharges'].fillna(0, inplace=True)

    # Convert 'Churn' to numerical (Yes=1, No=0)
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # Convert categorical features to numerical using one-hot encoding
    df = pd.get_dummies(df, columns=['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod'], drop_first=True)
    
    return df

if __name__ == '__main__':
    # Example usage:
    # Load the raw dataset
    raw_df = pd.read_csv('/home/ubuntu/SMSML_Nama-siswa/namadataset_raw/WA_Fn-UseC_-Telco-Customer-Churn.csv')
    
    # Perform automated preprocessing
    preprocessed_df = automate_preprocessing(raw_df)
    
    print('Preprocessed DataFrame Head:')
    print(preprocessed_df.head())
    print('\nPreprocessed DataFrame Info:')
    preprocessed_df.info()

