# collection device facts - hostname, model, serial, os and uptime. 

# once the devices are discovered, the device facts are to be collection for network documentation
# to build the CMDB. 
# Maintain the device inventory using libraries like Netmiko or NAPALM , engineers can automate SSH sessions
# to network devices, parse the output to extract relevant facts. 
# to retreive the hostname and serial number from Cisco IOS router

from netmiko import ConnectHandler

devices = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5001",
    "username": "admin",
    "password": "cisco123",
}

connection = ConnectHandler(**devices)

# collect hostname 
hostname = connection.send_command('show running-config | include hostname', read_timeout=120)

# collect serial number 
serialnum = connection.send_command('show version | include Serial', read_timeout=120)

# collect uptime of devices 
device_uptime = connection.send_command('show version | include uptime', read_timeout=120)

# collect os version 
os_version = connection.send_command('show version | include Cisco IOS', read_timeout=120)

# disconnect the devices 
connection.disconnect()

# print the device info
print(f"hostname: {hostname}")
print(f"Serial: {serialnum}")
print(f"uptime:, {device_uptime}")
print(f"OS version: {os_version}")