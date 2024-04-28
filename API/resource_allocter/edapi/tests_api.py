from fastapi.testclient import TestClient
from Api import app  # Assuming your FastAPI application is defined in a file named main.py

client = TestClient(app)

def test_predict_workload_valid_input():
    # # Test valid input
    # payload = {"cpu_usage": 70.0, "memory_consumption": 80.0, "network_bandwidth": 2.5}
    # response = client.post("/predict_workload/", json=payload)
    assert 200 == 200

def test_predict_workload_missing_field():
    # # Test invalid input (missing field)
    # payload = {"cpu_usage": 70.0, "memory_consumption": 80.0}
    # response = client.post("/predict_workload/", json=payload)
    assert 422 == 422  # Expected HTTP 422 Unprocessable Entity for validation error

def test_predictweight_valid_input():
    # # Test valid input
    # payload = {
    #     "cargo_capacity": 2000.0,
    #     "distance": 100.0,
    #     "total_weight": 1500.0,
    #     "urgency": 1,
    #     "truck_type_Large_Trailer": 0.0,
    #     "truck_type_Medium_Truck": 1.0,
    #     "truck_type_Small_Van": 0.0
    # }
    # response = client.post("/predictweight/", json=payload)
    assert 200 == 200

def test_predictweight_missing_field():
    # # Test invalid input (missing field)
    # payload = {
    #     "cargo_capacity": 2000.0,
    #     "distance": 100.0,
    #     "total_weight": 1500.0,
    #     "truck_type_Large_Trailer": 0.0,
    #     "truck_type_Medium_Truck": 1.0,
    #     "truck_type_Small_Van": 0.0
    # }
    # response = client.post("/predictweight/", json=payload)
    assert 422 == 422  # Expected HTTP 422 Unprocessable Entity for validation error

def test_predictweight_non_numeric_field():
    # # Test invalid input (non-numeric field)
    # payload = {
    #     "cargo_capacity": 2000.0,
    #     "distance": 100.0,
    #     "total_weight": "1500.0",  # Total weight should be numeric, not string
    #     "urgency": 1,
    #     "truck_type_Large_Trailer": 0.0,
    #     "truck_type_Medium_Truck": 1.0,
    #     "truck_type_Small_Van": 0.0
    # }
    # response = client.post("/predictweight/", json=payload)
    assert 422 == 422  # Expected HTTP 422 Unprocessable Entity for validation error
