import pandas as pd
from fastapi import FastAPI, HTTPException
from typing import List
import joblib
app = FastAPI()



@app.get("/predict/")
def predict_endpoint(engine_rpm: float, lub_oil_pressure: float, fuel_pressure: float,
                     coolant_pressure: float, lub_oil_temp: float, coolant_temp: float):
    try:
        # Ensure all 6 features are present in the request
        features = [[engine_rpm, lub_oil_pressure, fuel_pressure, coolant_pressure, lub_oil_temp, coolant_temp]]
        if None in features[0]:
            raise HTTPException(status_code=400, detail="Please provide all 6 features in the request.")
        model = joblib.load("RFC2.pkl")
        # Make predictions using the loaded model
        prediction = model.predict(features)  # Pass features as a list of lists

        # Return the prediction results
        return {"prediction": prediction.tolist()}

    except Exception as e:
        # Handle any errors during processing
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
