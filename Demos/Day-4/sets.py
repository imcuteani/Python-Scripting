# Sets are type of data structure in python which store the collection of unique items. They're useful for 
# working with IP addr, network devices etc. 

addresses = {"192.168.1.1", "192.168.100.1", "192.168.100.3"}
addresses = {"192.168.1.1", "192.168.100.1", "192.168.100.3", "192.168.100.1"}
print(addresses)

# modify sets in python 
# use the .add() method to insert a new element into a set. If the element is already in the set, nothing happens.

ip_addresses = {"192.168.1.1", "192.168.100.1"}
ip_addresses.add("10.38.1.2")
print(ip_addresses)

my_set = {6.1, 2.6, 4.9, 3.2, 1.55}
my_set.add(0.11)
print(my_set)

# .update() method in sets 
network_address = {"192.168.1.1", "192.168.100.1", "192.168.100.3"}
network_address.update({"192.168.100.2", "192.168.1.1", "192.168.100.4", "192.168.100.5"})
print(network_address)

# remove() to delete a specific element from a set. If the element is not in the set, it raises an error. 

#network_address.remove("192.168.1.2")
#print(network_address)

# .discard() method to remove an element without causing an error if the element is not in the set. 

network_address.discard("192.168.100.3")
print(network_address)

# Union Ops -> combines all the elements of two sets and removes any duplicates. 
# to perform a union operation in python you can use the | operator. 
# 
dc_address = {"192.168.1.1", "192.168.100.1", "192.168.100.2", "10.34.1.1"} 
lb_address = {"10.20.1.1", "20.1.1.1", "10.34.1.1", "10.14.1.1"}

result = dc_address | lb_address
print(result)

# Intersection operations 

# retrieves the elements which are common in both sets and use & operator. 
dc_address = {"192.168.1.1", "192.168.100.1", "192.168.100.2", "10.34.1.1"} 
lb_address = {"10.20.1.1", "20.1.1.1", "10.34.1.1", "10.14.1.1"}

inter_result = dc_address & lb_address
print(inter_result)

# Symmetric difference operation 

# symmetric difference ops retrieves elements which are unique to each set. To perform a symmetric 
# # difference operation in python, you can use ^ operator. 
# 

dc_address = {"192.168.1.1", "192.168.100.1", "192.168.100.2", "10.34.1.1"} 
lb_address = {"10.20.1.1", "20.1.1.1", "10.34.1.1", "10.14.1.1"}
sym_result = dc_address ^ lb_address
print(sym_result) 


# IP address management 

# Sets can pool IP addrs (IPAM) by finding available addresses, overlapping addresses, or combinging 
# pools. You can perform difference, union, intersection, difference for the tasks. 

ipam = {'192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.5'}
assigned_ips = {'192.168.1.2', '192.168.1.4'}

# finding the available IP addrd using the difference ops 

available_ips = ipam - assigned_ips
print("Available IPs: ", available_ips)

# detecting overlaps using the intersection operation 

overlaps = ipam & assigned_ips 
print("Overlaps:", overlaps)

# combining ip pools using the union operation 
combined_pool = ipam | assigned_ips
print("Combined pools of IP: ", combined_pool)

