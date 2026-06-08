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
commands = ['show version', 'show ip route', 'show interfaces']
for command in commands:
    output = net_connect.send_command(command)
    print(output)
#output = net_connect.send_command("show ip interface brief")
#print(output)

#print(net_connect.send_command("show version", use_textfsm=True))
net_connect.disconnect()