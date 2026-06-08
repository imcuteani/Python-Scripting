import napalm
import json

# Create a NAPALM driver for Cisco IOS
driver = napalm.get_network_driver("eos")

# Connect to the device
device = driver(hostname="192.168.4.131", username="admin", password="cisco123", optional_args={"port": 5001},timeout= 60)
device.open()

# Perform operations on the device
# Retrieve the running configuration
device_facts = device.get_facts()

# Print the running configuration
print(json.dumps(device_facts, indent=4))


# Close the connection
device.close()