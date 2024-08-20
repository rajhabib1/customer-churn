from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})  # Allow all origins

# Load the saved model
model = joblib.load('customer_churn_model.pkl')

# List of columns used during training
required_columns = [
    'SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges',
    'gender_Male', 'Partner_Yes', 'Dependents_Yes', 'Contract_One year',
    'Contract_Two year', 'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check',
    'PhoneService_Yes', 'MultipleLines_No phone service',
    'MultipleLines_Yes', 'InternetService_Fiber optic',
    'InternetService_No', 'OnlineSecurity_No internet service',
    'OnlineSecurity_Yes', 'OnlineBackup_No internet service',
    'OnlineBackup_Yes', 'DeviceProtection_No internet service',
    'DeviceProtection_Yes', 'TechSupport_No internet service',
    'TechSupport_Yes', 'StreamingTV_No internet service', 'StreamingTV_Yes',
    'StreamingMovies_No internet service', 'StreamingMovies_Yes',
    'PaperlessBilling_Yes'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    
    # Ensure all required columns are present
    for col in required_columns:
        if col not in df.columns:
            df[col] = 0  # Assign a default value if column is missing
    
    # Reorder columns to match training data
    df = df[required_columns]
    
    # Predict
    prediction = model.predict(df)
    result = 'Churn' if prediction[0] == 1 else 'Not Churn'
    
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)