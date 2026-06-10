# pydantic is a python library for defining data models and validating them using standard python type hints. 

# Pydantic works with basemodel classes -> you can create classes inherting from Basemodel to define the 
# data structure , fields can have types, defaults, you can add constraints. 

# Pydantic can use validators -> built in validation, lets you add the custom validators 
# Custom types -> supports IPvAnyinterface for IP addresses 
# pydantic models are act as self documenting code for your data. 

# Real time scenario -> validation of inventory data, site details, BGP policies, VLAN/IPAM info, API payloads. 

# validation of layer 3 interface 

from pydantic import BaseModel, IPvAnyAddress, Field
from typing import Literal, Optional, Union
import ipaddress

class L3Interface(BaseModel):
    name: str
    address: str
    #address: Union[ipaddress.IPv4Address, ipaddress.IPv6Address]
    vrf: str = "default"
    enabled: bool = True
    platform: Literal["iosxe", "nxos", "iosxr"]

intf = L3Interface(name="Loopback0", address="192.168.1.10/24", platform="iosxe")
print(intf.model_dump())  # safe to feed into jinja2 or napalm  
print(intf.address)  # assigned IP address 
print(intf.platform) # assigned device platform