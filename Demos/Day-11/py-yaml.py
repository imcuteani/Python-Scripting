# YAML (Yet another markup language) is a human readbale data serialization standard which is used for configuration files and data exchange. 

import yaml 

# data to be written in yaml file 

data = {
    'devicename': 'ciscoXE', 
    'deviceos' : 'ios', 
    'ip' : '192.168.224.1', 
    'devicetype' : 'router'
}

# writing to the yaml file 
with open('data.yaml', 'w') as file:
    yaml.dump(data, file)

print("Data has written to the 'data.yaml' file")   

# reading from yaml template 

import yaml 

# reading data from the yaml file 

with open('data.yaml', 'r') as file:
    loaded_data = yaml.safe_load(file)

print("Data read from 'data.yaml':")
print(loaded_data)    