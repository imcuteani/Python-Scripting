from netmiko import ConnectHandler

cisco_router = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5001",
    "username": "admin",
    "password": "cisco123",
    
}
# apply BGP configuration
net_connect = ConnectHandler(**cisco_router)
config_commands = [
    'router bgp 65000',
    'neighbor 192.168.2.1 remote-as 65001',
    'network 192.168.1.0 mask 255.255.255.0',
]
output = net_connect.send_config_set(config_commands, read_timeout=120)
print(output)

# device uptime checking 
device_uptime = net_connect.send_command('show version | include uptime', read_timeout=120)
print(device_uptime)
net_connect.disconnect()

# loopback interface configuration 

config_commands = [
    'interface Loopback0',
    'ip address 10.0.0.1 255.255.255.255',
    'no shutdown',
]

loopback_config = net_connect.send_config_set(config_commands, read_timeout=120)
print(loopback_config)
net_connect.disconnect()