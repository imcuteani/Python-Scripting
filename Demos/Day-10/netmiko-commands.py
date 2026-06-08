# using netmiko sending configuration commands
from netmiko import ConnectHandler

cisco_router = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5004",
    "username": "admin",
    "password": "cisco123",
    
}

net_connect = ConnectHandler(**cisco_router)
config_commands = [
    'interface Serial0',
    'description Connected to LAN',
    'ip address 192.168.3.1 255.255.255.0',
    'no shutdown'
]

#output = net_connect.send_config_set(config_commands, read_timeout=120)
#print(output)
ip_interface = net_connect.send_command("show ip interface brief", read_timeout=120)
print(ip_interface)
net_connect.disconnect()