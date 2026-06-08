# perform interface status check 

from netmiko import ConnectHandler

cisco_router = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5001",
    "username": "admin",
    "password": "cisco123",
    
}

net_connect = ConnectHandler(**cisco_router)
output = net_connect.send_command('show interface description')
print(output)
net_connect.disconnect()
