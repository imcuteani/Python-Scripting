from netmiko import ConnectHandler

cisco_router = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5001",
    "username": "admin",
    "password": "cisco123",
    
}

# apply ACLS 

net_connect = ConnectHandler(**cisco_router)
config_commands = [
    'access-list 100 permit ip any any',
    'access-list 101 deny ip 192.168.1.0 0.0.0.255 any',
]
output = net_connect.send_config_set(config_commands, read_timeout=120)
print(output)
net_connect.disconnect()