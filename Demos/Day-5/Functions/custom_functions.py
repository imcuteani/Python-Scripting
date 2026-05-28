# blocks of code designed to organize the code to be reusable for specific tasks. 
# It allows for efficient reuse of code segments for customized functions. 

def configure_router(router_name):
    print(f"{router_name} configuration is completed")
configure_router("R1")   # calling the function    


# return values in Functions 

def configure_device(device_name):
    print(f"configuring {device_name}")
    # note: no explict return statement, so it defaults to None

result = configure_device("Router1")
print(result)

# positional arguments -> involves passing values to a function based on the order in which parameters are listed during the function definition. 

def get_device_status(device_name):
    print(f"configuring {device_name}")
    status = "Online"
    return f"{device_name} is {status}"

device_status = get_device_status("Switch2")
print(device_status) 

# function default arguments -> provide a way to make functions callable with fewer arguments. 
# the arguments must be passed for the function to execute a task, default arguments come with predefined values 

def configure_device(device_name, configuration_mode="advanced"):
    print(f"configuring {device_name} in {configuration_mode} mode.")
configure_device("Router2")


# Keyword (named) arguments -> sending arguments with the key=value syntax, known as named arguments. 
# it provides a flexible way to call networking functions where the order of the arguments becomes independent. 

def configure_network_device(device_name, configuration_mode="basic", interface="eth0"):
    print(f"Configuring {device_name} in {configuration_mode} mode on interface {interface}.")
configure_network_device("Router1", configuration_mode="advanced", interface="eth1")    
