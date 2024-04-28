import random
import requests

class EngineSensor:
  """Simulates engine sensor data"""

  def __init__(self):
    self.normal_rpm_range = (700, 3000)  # Adjust for your engine type
    self.normal_oil_pressure_range = (3.0, 6.0)  # Units (adjust based on sensor)
    self.normal_fuel_pressure_range = (10.0, 15.0)  # Units (adjust based on sensor)
    self.normal_coolant_pressure_range = (0.5, 1.5)  # Units (adjust based on sensor)
    self.normal_temp_range = (70, 90)  # Celsius (adjust based on engine)

  def generate_data(self):
    """Generates engine sensor data"""
    # Simulate normal engine operation
    rpm = random.randint(*self.normal_rpm_range)
    oil_pressure = random.uniform(*self.normal_oil_pressure_range)
    fuel_pressure = random.uniform(*self.normal_fuel_pressure_range)
    coolant_pressure = random.uniform(*self.normal_coolant_pressure_range)
    lub_oil_temp = random.randint(*self.normal_temp_range)
    coolant_temp = random.randint(*self.normal_temp_range)

    # Introduce occasional variations to simulate minor fluctuations
    rpm += random.randint(-50, 50)  # Minor RPM variation
    oil_pressure += random.uniform(-0.2, 0.2)  # Minor oil pressure variation
    fuel_pressure += random.uniform(-0.5, 0.5)  # Minor fuel pressure variation
    coolant_pressure += random.uniform(-0.1, 0.1)  # Minor coolant pressure variation
    lub_oil_temp += random.randint(-2, 2)  # Minor oil temperature variation
    coolant_temp += random.randint(-2, 2)  # Minor coolant temperature variation

    # Enforce limits to prevent unrealistic data (optional)
    rpm = max(self.normal_rpm_range[0], min(rpm, self.normal_rpm_range[1]))
    oil_pressure = max(self.normal_oil_pressure_range[0], min(oil_pressure, self.normal_oil_pressure_range[1]))
    fuel_pressure = max(self.normal_fuel_pressure_range[0], min(fuel_pressure, self.normal_fuel_pressure_range[1]))
    coolant_pressure = max(self.normal_coolant_pressure_range[0], min(coolant_pressure, self.normal_coolant_pressure_range[1]))
    lub_oil_temp = max(self.normal_temp_range[0], min(lub_oil_temp, self.normal_temp_range[1]))
    coolant_temp = max(self.normal_temp_range[0], min(coolant_temp, self.normal_temp_range[1]))
    url = f"http://127.0.0.1:8000/predict/?engine_rpm={rpm}&lub_oil_pressure={oil_pressure}&fuel_pressure={fuel_pressure}&coolant_pressure={coolant_pressure}&lub_oil_temp={lub_oil_temp}&coolant_temp={coolant_temp}"
    
    response = requests.get(url)
    print(response.text)
    return {
      "rpm": rpm,
      "oil_pressure": oil_pressure,
      "fuel_pressure": fuel_pressure,
      "coolant_pressure": coolant_pressure,
      "lub_oil_temp": lub_oil_temp,
      "coolant_temp": coolant_temp
    }
EngineSensor().generate_data()