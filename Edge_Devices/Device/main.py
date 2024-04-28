from Navigation import GPSSensor
from Engine import EngineSensor
from Cargo import CargoSensor
from Meta_data import EdgeDeviceSimulator
import time
import random
import json



def generate_truck_data():
  """Generates combined truck sensor data"""
  gps_sensor = GPSSensor()
  engine_sensor = EngineSensor()
  cargo_sensor = CargoSensor()

  data = {
    "gps": gps_sensor.generate_data(),
    "engine": engine_sensor.generate_data(),
    "cargo": cargo_sensor.generate_data(),
    "meta":EdgeDeviceSimulator(random.randint(1, 999999)).print_details(),
    "timestamp": time.time(),  # Add timestamp
  }
  
  return data

if __name__ == "__main__":
  while True:
    data = generate_truck_data()
    # Simulate sending data (replace with actual communication method)
    #Json = json.dumps(data)
    print(data)
    time.sleep(5)  # Simulate data generation interval
