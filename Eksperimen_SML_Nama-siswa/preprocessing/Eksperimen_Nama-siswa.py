import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('namadataset_raw/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Display the first 5 rows of the dataframe
print('First 5 rows of the dataset:')
print(df.head())

# Display basic information about the dataset
print('\nDataset Info:')
df.info()

# Display descriptive statistics
print('\nDescriptive Statistics:')
print(df.describe())

# Check for missing values
print('\nMissing Values:')
print(df.isnull().sum())

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

print('\nDataFrame after preprocessing:')
print(df.head())
print('\nDataset Info after preprocessing:')
df.info()

