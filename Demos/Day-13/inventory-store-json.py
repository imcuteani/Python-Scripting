# store the device data into CSV format 
# csv library or openpyxl library to format the output into csv/excel files. 

import csv 
from netmiko import ConnectHandler
import json

devices =  {
        "device_type": "cisco_ios_telnet",
        "host": "192.168.80.129",
        "port": "5004",
        "username": "admin",
        "password": "cisco123",
        "read_timeout_override": 240
    }
    

connection = ConnectHandler(**devices)
connection.disable_paging()

# collect hostname 
hostname = connection.send_command('show running-config | include hostname', read_timeout=240, expect_string=r"#")

# collect serial number 
serialnum = connection.send_command('show version | include Serial', read_timeout=240, expect_string=r"#")

# collect uptime of devices 
device_uptime = connection.send_command('show version | include uptime', read_timeout=240, expect_string=r"#")

# collect os version 
os_version = connection.send_command('show version | include Cisco IOS', read_timeout=240, expect_string=r"#")

# disconnect the devices 
connection.disconnect()

# print the device info
print(f"hostname: {hostname}")
print(f"Serial: {serialnum}")
print(f"uptime:, {device_uptime}")
print(f"OS version: {os_version}")

the_final_output = '{"hostname": "hostname R4", "Serial": "1 Serial(sync/async) interface", "uptime": "1 hour 19 min", "OS version": "Cisco IOS C1700 Software"}'
device_json = json.loads(the_final_output)
print(type(device_json),device_json)
print(device_json.keys())





# create file with context manager 
output_file = 'network_inventory.csv'
with open(output_file, 'w', newline='') as csvfile: 
    fieldnames = ['hostname', 'serial','uptime', 'os version']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in device_json.values():
        writer.writerow(row.keys())
        
    print(f"\n Inventory data saved to {output_file}")        
