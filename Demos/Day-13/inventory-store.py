# store the device data into CSV format 
# csv library or openpyxl library to format the output into csv/excel files. 

import csv 
from netmiko import ConnectHandler

devices = [
    {
        'device_type': 'cisco_ios_telnet',
        "host": "192.168.80.129",
        "port": "5004",
        "username": "admin",
        "password": "cisco123",
        "read_timeout_override": 240,
    },
    {
    'device_type': 'cisco_ios_telnet',
        "host": "192.168.80.129",
        "port": "5001",
        "username": "admin",
        "password": "cisco123",
        "read_timeout_override": 240,
    },
]
for device in devices: 
    net_connect = ConnectHandler(**device)
    net_connect.disable_paging()
   # collect hostname 
hostname = net_connect.send_command('show running-config | include hostname', read_timeout=240, expect_string=r"#")

# collect serial number 
serialnum = net_connect.send_command('show version | include Serial', read_timeout=240,expect_string=r"#")

# collect uptime of devices 
device_uptime = net_connect.send_command('show version | include uptime', read_timeout=240,expect_string=r"#")

# collect os version 
os_version = net_connect.send_command('show version | include Cisco IOS', read_timeout=240,expect_string=r"#")
    
 # print the device info
print(f"hostname: {hostname}")
print(f"Serial: {serialnum}")
print(f"uptime:, {device_uptime}")
print(f"OS version: {os_version}") 
#net_connect.disconnect()  

# create file with context manager 
output_file = 'network_inventory.csv'
with open(output_file, 'w', newline='') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames=['device_type', 'host', 'port', 'username', 'password', 'read_timeout_override'])
    writer.writeheader()
    for row in devices:
        writer.writerow(row)
        net_connect.disconnect()
print(f"\n Inventory data saved to {output_file}")        
