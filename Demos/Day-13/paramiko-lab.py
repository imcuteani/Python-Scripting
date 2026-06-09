# Differences between Netmiko and Paramiko 

# Network hardwares is associated with Netmiko (Routers, Switches, FW). Paramiko works with Linux/Unix servers. 
# Netmiko is high level abstractions (handling prompts, paging automatically) & paramiko has low level abstraction 
# Netmiko automatically bypasses paging but paramiko requires explicit manual command to stop paging
# Netmiko returns clean text strings directly whereas paramiko return raw stdout and stdin byte channels
# netmiko has support for 90+ network OS and paramiko has platform neutral layers and requires manual logic per OS

import paramiko
import time

try:
# create a SSH client 
 client = paramiko.SSHClient()

# set policy to automatically add hosts to known hosts file 
 client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote host 
 client.connect(
    hostname="192.168.80.129",
    port="5004",
    username="admin",
    password="cisco123",
    look_for_keys=False,
    allow_agent=False,
    banner_timeout=200
)

# open an interactive SSH session
 ssh_client = client.invoke_shell()

# send command 
 ssh_client.send("sh ip int bri\n")

# wait for the command to be finished
 time.sleep(3)

# receive and process the command output 
 output = ssh_client.recv(65000)
 print(output.decode("utf-8"))

# close the ssh connection
 ssh_client.close()

# close the device connection
 client.close()

except paramiko.AuthenticationException:
 print("Authentication failed, please verify the credentials") 
