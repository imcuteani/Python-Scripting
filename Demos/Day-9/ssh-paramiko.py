import paramiko
import time

# Create SSH client
client = paramiko.SSHClient()

# Set policy to automatically add hosts to known hosts file
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote host
client.connect(
    hostname="192.168.80.128",
    username="gns3",
    password="gns3",
    look_for_keys=False,
    allow_agent=False,
)

# Open an interactive SSH session
ssh_client = client.invoke_shell()

# Send command
ssh_client.send("ip a")

# Wait for the command to be finished
time.sleep(3)

# Receive and process command output
output = ssh_client.recv(65000)
print(output.decode("ascii"))

# Close the SSH session
ssh_client.close()

# Close the connection
client.close()