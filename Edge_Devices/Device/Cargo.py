import random
class CargoSensor:
  """Simulates cargo sensor data"""

  def __init__(self):
    pass

  def generate_data(self):
    """Generates cargo data (temperature, weight)"""
    return {
      "temperature": random.uniform(-10, 20),
      "weight": random.randint(1000, 10000),
    }
