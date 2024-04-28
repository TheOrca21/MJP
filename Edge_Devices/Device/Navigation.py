from faker import Faker

class GPSSensor:
  """Simulates GPS sensor data"""
  
  def __init__(self):
    self.faker = Faker()

  def generate_data(self):
    """Generates GPS coordinates"""
    return (self.faker.latitude(), self.faker.longitude())
