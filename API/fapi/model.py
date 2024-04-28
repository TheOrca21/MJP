# Importing the predict function
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

data = pd.read_csv("D:\\work\\Major_Project\\car_simulator\\archive\\engine_data.csv")
X = data.drop('Engine Condition', axis=1)
y = data['Engine Condition']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

            # Standardize the data
ss = StandardScaler()
x_train_scaled = ss.fit_transform(X_train)
x_test_scaled = ss.transform(X_test)

            # Train the Random Forest classifier
RFC2_model = RandomForestClassifier(criterion='entropy', max_depth=8, min_samples_split=2, n_estimators=150)
RFC2_model.fit(x_train_scaled, y_train)
joblib.dump(RFC2_model, 'RFC2.pkl')         
            