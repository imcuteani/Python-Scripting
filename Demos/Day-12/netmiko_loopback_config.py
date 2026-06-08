from netmiko import ConnectHandler

cisco_router = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5001",
    "username": "admin",
    "password": "cisco123",
    
}
net_connect = ConnectHandler(**cisco_router)
# loopback interface configuration 

config_commands = [
    'interface Loopback0',
    'ip address 10.0.0.1 255.255.255.255',
    'no shutdown',
]

loopback_config = net_connect.send_config_set(config_commands, read_timeout=120)
print(loopback_config)
net_connect.disconnect()