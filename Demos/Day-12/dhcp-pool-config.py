# perform dhcp pool config 

from netmiko import ConnectHandler

cisco_router = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5001",
    "username": "admin",
    "password": "cisco123",
    
}

net_connect = ConnectHandler(**cisco_router)
config_dhcp = [
    'ip dhcp pool MY_POOL',
    'network 192.168.1.0 255.255.255.0',
    'default-router 192.168.1.1',
    'dns-server 8.8.8.8 8.8.4.4',
]

dhcp_config_output = net_connect.send_config_set(config_dhcp, read_timeout=120)
print(dhcp_config_output)

# NTP server config
ntp_server_config = [
    'ntp server 192.168.2.1',
]
net_server_output = net_connect.send_config_set(ntp_server_config, read_timeout=120)
print(net_server_output)

cpu_usage = net_connect.send_command('show processes cpu', read_timeout=120)
print(cpu_usage)
net_connect.disconnect()