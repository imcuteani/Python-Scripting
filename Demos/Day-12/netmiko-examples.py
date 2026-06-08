# using netmiko processing multiple commands

from netmiko import ConnectHandler

cisco_router = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5004",
    "username": "admin",
    "password": "cisco123",
}

net_connect = ConnectHandler(**cisco_router)
# backup device configuration
output = net_connect.send_command('show running-config')
with open('backup-config.txt', 'w') as file:
    file.write(output)
net_connect.disconnect()
