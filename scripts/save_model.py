import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
import pandas as pd
from imblearn.over_sampling import SMOTE

# Load your preprocessed data
file_path = '/Users/rajhabib/customer-churn-prediction/data/preprocessed_data.csv'
df = pd.read_csv(file_path)

# Separate features (X) and target variable (y)
X = df.drop(['customerID', 'Churn'], axis=1)  # Exclude non-numeric and target columns

# Encode categorical features using OneHotEncoder or get_dummies
X_encoded = pd.get_dummies(X, drop_first=True)  # Adjust drop_first as needed

# Encode target variable 'Churn' into numeric labels
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['Churn'])

# Apply SMOTE to handle class imbalance
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_encoded, y)

# Split resampled data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Define and train the model
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42),
                           param_grid=param_grid,
                           cv=5,
                           scoring='accuracy',
                           verbose=1,
                           n_jobs=-1)
grid_search.fit(X_train, y_train)

# Get the best model
best_estimator = grid_search.best_estimator_

# Save the model
joblib.dump(best_estimator, 'customer_churn_model.pkl')

print("Model saved successfully!")
