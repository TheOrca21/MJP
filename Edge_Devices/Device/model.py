import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
from Meta_data import EdgeDeviceSimulator

# Step 1: Generate dataset using EdgeDeviceSimulator
num_samples = 10000
data = [EdgeDeviceSimulator(device_id).generate_data() for device_id in range(num_samples)]
df = pd.DataFrame(data)

# Step 2: Feature Engineering
X = df[['cpu_usage', 'memory_consumption', 'network_bandwidth']]
y = df['workload']

# Step 3: Model Selection
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Step 4: Training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Step 6: Save the trained model
joblib.dump(model, 'resource_allocation_model.pkl')
print("Model saved as 'resource_allocation_model.pkl'")
