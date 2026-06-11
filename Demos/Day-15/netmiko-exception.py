from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetMikoAuthenticationException

devices = [
    {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5004",
    "username": "admin",
    "password": "cisco123",
    },
    {
    'device_type': 'cisco_ios_telnet',
        "host": "192.168.80.129",
        "port": "5005",
        "username": "admin",
        "password": "cisco123",
    },
]

# attept to establish a connection to each device and execute a show command

for device in devices:
    try:
        net_connect = ConnectHandler(**device)
        output = net_connect.send_command("show ip int brief", read_timeout=120)
        print(output)
    except NetmikoTimeoutException:
        print(f"Device {device['host']} is not reachble") 
    except NetMikoAuthenticationException:
        print(f"Authentication failed for {device['port']}")       