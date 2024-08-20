import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    # Convert TotalCharges to numeric (if not already) and handle any missing values
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(0)  # Handle missing values with 0
    
    # Encode categorical variables
    df = pd.get_dummies(df, columns=['gender', 'Partner', 'Dependents',
                                     'Contract', 'PaymentMethod'], drop_first=True)
    

    return df

if __name__ == "__main__":
    file_path = '/Users/rajhabib/customer-churn-prediction/data/telco_customer_churn.csv'  
    df = load_data(file_path)  # Load data into df variable
    
    # Preprocess data
    df = preprocess_data(df)
    
    # Save preprocessed data to a new CSV file
    output_file_path = '/Users/rajhabib/customer-churn-prediction/data/preprocessed_data.csv'  
    df.to_csv(output_file_path, index=False)
