import random
import time

class EdgeDeviceSimulator:
  """Simulates sensor data and workload for an edge device."""

  def __init__(self, device_id, 
               base_cpu_usage=50, cpu_usage_deviation=10, 
               base_memory_consumption=70, memory_consumption_deviation=15, 
               base_network_bandwidth=2, network_bandwidth_deviation=0.5, 
               workload_types=["High", "Normal", "Low"], base_workload=10):
    self.device_id = device_id
    self.base_cpu_usage = base_cpu_usage
    self.cpu_usage_deviation = cpu_usage_deviation
    self.base_memory_consumption = base_memory_consumption
    self.memory_consumption_deviation = memory_consumption_deviation
    self.base_network_bandwidth = base_network_bandwidth
    self.network_bandwidth_deviation = network_bandwidth_deviation
    self.workload_types = workload_types
    self.base_workload = base_workload

  def generate_data(self):
    """Generates sensor data and workload for the device."""

    # Generate sensor data
    cpu_usage = self.generate_cpu_usage()
    memory_consumption = self.generate_memory_consumption()
    network_bandwidth = self.generate_network_bandwidth()

    # Generate workload
    workload = self.generate_workload()

    return {
        "device_id": self.device_id,
        "cpu_usage": cpu_usage,
        "memory_consumption": memory_consumption,
        "network_bandwidth": network_bandwidth,
        "workload": workload
    }

  def generate_cpu_usage(self):
    return self.base_cpu_usage + random.uniform(-self.cpu_usage_deviation, self.cpu_usage_deviation)

  def generate_memory_consumption(self):
    return self.base_memory_consumption + random.randint(-self.memory_consumption_deviation, self.memory_consumption_deviation)

  def generate_network_bandwidth(self):
    return self.base_network_bandwidth + random.uniform(-self.network_bandwidth_deviation, self.network_bandwidth_deviation)

  def generate_workload(self):
    workload_type = random.choice(self.workload_types)
    if workload_type == "High":
      return self.base_workload * 1.5
    elif workload_type == "Low":
      return self.base_workload * 0.75
    else:
      return self.base_workload

  def print_details(self):
    """Prints details of the simulated data for the device."""

    data = self.generate_data()
    formatted_data = f"Device {data['device_id']}:\n"
    formatted_data += f"  CPU Usage: {data['cpu_usage']:.2f}%\n"
    formatted_data += f"  Memory Consumption: {data['memory_consumption']:.2f}%\n"
    formatted_data += f"  Network Bandwidth: {data['network_bandwidth']:.2f} Mbps\n"
    formatted_data += f"  Workload: {data['workload']:.2f} (units)\n"

    return formatted_data


