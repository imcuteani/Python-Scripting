# Looping through multiple devices (Cisco 7200 IOS routers)
from netmiko import ConnectHandler

devices = [
    {
        'device_type': 'cisco_ios_telnet',
        "host": "192.168.80.129",
        "port": "5004",
        "username": "admin",
        "password": "cisco123",
    },
    {
    'device_type': 'cisco_ios_telnet',
        "host": "192.168.80.129",
        "port": "5001",
        "username": "admin",
        "password": "cisco123",
    },
]

# looping through multiple devices 

for device in devices: 
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip interface brief", read_timeout=120)
    print(f"Device {device['host']}:\n{output}")
    net_connect.disconnect()