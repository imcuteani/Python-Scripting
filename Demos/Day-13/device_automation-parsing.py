from netmiko import ConnectHandler

devices = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5001",
    "username": "admin",
    "password": "cisco123",
}

connection = ConnectHandler(**devices)

# collect hostname using textfsm
ip_route_fsm = connection.send_command('show ip route', read_timeout=120, use_textfsm=True)
print(ip_route_fsm)
ip_route_genie = connection.send_command('show ip interface brief', read_timeout=120, use_genie=True)
print(ip_route_genie)
ip_route_ttp = connection.send_command('show vlan brief', read_timeout=120, use_ttp=True)
print(ip_route_ttp)