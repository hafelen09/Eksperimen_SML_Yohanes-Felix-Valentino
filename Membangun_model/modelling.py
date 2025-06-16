import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import mlflow
import mlflow.sklearn
import os

# Set MLflow tracking URI to local
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Enable autologging for scikit-learn
mlflow.sklearn.autolog()

if __name__ == "__main__":
    # Load preprocessed data
    preprocessed_file_path = 
    '/home/ubuntu/Eksperimen_SML_Yohanes-Felix-Valentino/namadataset_preprocessing/WA_Fn-UseC_-Telco-Customer-Churn_preprocessed.csv'
    
    # Check if the preprocessed file exists
    if not os.path.exists(preprocessed_file_path):
        print(f"Error: Preprocessed file not found at {preprocessed_file_path}")
        print("Please ensure the GitHub Actions workflow for preprocessing has run successfully.")
        exit()

    df = pd.read_csv(preprocessed_file_path)

    # Drop customerID as it's not a feature
    df = df.drop("customerID", axis=1)

    # Define features (X) and target (y)
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a RandomForestClassifier model
    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        print(f"Accuracy: {accuracy}")
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
        print(f"F1 Score: {f1}")

        # MLflow autologging will log parameters, metrics, and model automatically
        print("MLflow autologging is enabled. Check your MLflow UI for details.")

