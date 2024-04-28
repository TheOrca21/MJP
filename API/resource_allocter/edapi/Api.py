import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError

app = FastAPI()
workload = joblib.load("edapi//resource_allocation_model.pkl")

class InputFeatures(BaseModel):
    cpu_usage: float
    memory_consumption: float
    network_bandwidth: float

@app.post("/predict_workload/")
def predict_workload(features: InputFeatures):
    try:
        # Make predictions using the loaded model
        prediction = workload.predict([[features.cpu_usage, features.memory_consumption, features.network_bandwidth]])

        # Return the prediction result
        return {"predicted_workload": prediction[0]}

    except Exception as e:
        # Handle any errors during processing
        raise HTTPException(status_code=500, detail=str(e))
# Define a Pydantic model to validate the request body
class InputFeatures(BaseModel):
    cargo_capacity: float
    distance: float
    total_weight: float
    urgency: int  # New feature for delivery urgency
    truck_type_Large_Trailer: float
    truck_type_Medium_Truck: float
    truck_type_Small_Van: float

# Load the trained model
model = joblib.load("edapi//model.pkl")  # Update with the actual file path of your trained model

@app.post("/predictweight/")
def predict_endpoint(features: InputFeatures):
    try:
        # Make predictions using the loaded model
        prediction = model.predict([[
            features.cargo_capacity, features.distance, features.total_weight, features.urgency,
            features.truck_type_Large_Trailer, features.truck_type_Medium_Truck, features.truck_type_Small_Van
        ]])

        # Return the prediction results
        return {"prediction": prediction.tolist()}

    except Exception as e:
        # Handle any errors during processing
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
