# Create a dictionary with curly braces 

net_dict = {
    "rtr1": "10.100.1.1",
    "rtr2": "10.100.1.2", 
    "rtr3": "10.100.1.3"
}
print(net_dict)

# Create a dictionary with dict() constructor 

alt_dic = dict(rtr1="10.100.1.1", rtr2="10.100.1.2", rtr3="10.100.1.3")
print(alt_dic)

alt_dic = alt_dic.keys()
print(alt_dic)

alt_dic = net_dict.values()
print(alt_dic)

alt_dic = net_dict.items()
print(alt_dic)

# nested dictionary where you can have a dictionary where each key's value in another disctionary
nested_dict = {
    'rtr1':{
        'host': 'router1',
        'device_type': 'cisco',
    },
    'rtr2':{
        'host': 'router2',
        'device_type': 'junos'
    }
}
print(nested_dict)