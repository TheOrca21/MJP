import pandas as pd
import random
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import joblib

# Define truck types and capacities
truck_types = ["Small Van", "Medium Truck", "Large Trailer"]
capacities = {
    "Small Van": (1500, 2500),
    "Medium Truck": (4000, 6000),
    "Large Trailer": (8000, 12000)
}

# Define distance and weight ranges
distance_range = (20, 500)
weight_range = (0, 1)  # Weight as a proportion of capacity (0 to 1)

# Generate more data with delivery urgency
data = []
for _ in range(5000):  # Increase for a larger dataset
    truck_type = random.choice(truck_types)
    capacity = random.randint(capacities[truck_type][0], capacities[truck_type][1])
    distance = random.randint(distance_range[0], distance_range[1])
    weight_proportion = random.uniform(weight_range[0], weight_range[1])
    total_weight = int(capacity * weight_proportion)
    workload = total_weight
    urgency = random.choice([0, 1])  # 0: non-urgent, 1: urgent
    data.append({
        "truck_type": truck_type,
        "cargo_capacity": capacity,
        "distance": distance,
        "total_weight": total_weight,
        "workload": workload,
        "urgency": urgency
    })

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Encode categorical variable (truck_type)
encoder = OneHotEncoder()
encoded_truck_type = encoder.fit_transform(df[['truck_type']])
encoded_truck_type_df = pd.DataFrame(encoded_truck_type.toarray(), columns=encoder.get_feature_names_out(['truck_type']))
df_encoded = pd.concat([df, encoded_truck_type_df], axis=1).drop(columns=['truck_type'])

# Feature selection (replace with your chosen features)
features = ["cargo_capacity", "distance", "total_weight", "urgency"] + list(encoded_truck_type_df.columns)
target = "workload"  # workload represents total cargo weight delivered

# Separate features and target variable
X = df_encoded[features]
y = df_encoded[target]

# Train-test split (customize test size as needed)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on test data
y_pred = model.predict(X_test)

# Evaluate model performance (e.g., using mean squared error)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Predict workload for a new delivery (replace with specific values)
new_truck_type = "Small Van"
new_cargo_capacity = 2000  # weight units
new_distance = 50  # kilometers
new_total_weight = 1500  # weight units
new_urgency = 1  # urgent delivery

# Encode new data
new_data = pd.DataFrame({
    "cargo_capacity": [new_cargo_capacity],
    "distance": [new_distance],
    "total_weight": [new_total_weight],
    "urgency": [new_urgency],
    **{col: [0] for col in encoded_truck_type_df.columns}  # Initialize all one-hot encoded columns to 0
})
new_data["truck_type_" + new_truck_type] = 1  # Set the appropriate truck_type column to 1

predicted_workload = model.predict(new_data)[0]
print(f"Predicted workload for new delivery: {predicted_workload:.2f} weight units")

# Save the trained model
joblib.dump(model, 'model.pkl')
