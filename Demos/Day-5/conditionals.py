# Conditional statements in python

# elif and else statements 

ssh_timeout = 20
if ssh_timeout == 10:
    print("SSH timeout: 10 sec")
elif ssh_timeout > 30:
    print("SSH Timeout Greater than: 30 sec")
else:
    print("Unpected SSH timeout")    

# Logical operators and conditional statements combination
# 
ssh_timeout = 20
ip_addr = "10.10.1.1"
host_reachable = True 

if host_reachable and ssh_timeout >= 10:
    print("Try to connect")
elif not host_reachable or ip_addr == "10.10.1.1":
    print("Invalid host, do not try connection")
else:
    print("Unpected error, do try connecting")        

# Nested conditional statements 
# 
ssh_timeout = 20
host_reachable = True

if host_reachable:
    if ssh_timeout is not None:                   # idiomatic expression
        print("Try to connect to the host")
    else:
        print("Unpected error, try connecting")  

# python idiomatic expressions 
# 
ssh_timeout = 10
ip_addr = None 
host_reachable = False

if ssh_timeout is None: 
    print("Error, no SSH timeout")
elif host_reachable is False or ip_addr is not None: 
    print("Error, host is reachable")
else: 
    print("No Error occurred")                  