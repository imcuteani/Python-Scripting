import paramiko
import time 

#create a SSH client
client = paramiko.SSHClient()

# Set the policy to automatically add hosts to the known hosts file
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to the remote host
client.connect(
    hostname="192.168.80.129",
    username="gns3",
    password="gns3",
    look_for_keys=False,
    allow_agent=False,
)
# open an interactive SSH session
ssh_client = client.invoke_shell()

# send command 

ssh_client.send("show ip interface brief\n")
# wait for the command to be finished
time.sleep(3)
# receive and process the command output
output = ssh_client.recv(65000)
print(output.decode("ascii"))

# Close the SSH connection
ssh_client.close()

# close the client connection

client.close()