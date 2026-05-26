# creating a list 

my_list = ["cisco", 1, "router", [], "juniper", None, 2.3, "vlan"]
print(type(my_list))

# accessing the items in the list 
first_item = my_list[0]
print(first_item)

# update the list 
my_list[0] = 125.3
print(my_list)

# in Python lists, you can use negative indices to access items from the end of the list. -1 is the last item, 
# -2 is the second to last so on. 

last_item = my_list[-1]
print(last_item)
# list membership
# you can check if a specific element is in a list using the in operator. 
routers = ["broadcom", "cisco", "amazon", "juniper", "palo alto"]
check_routers = "microsoft"

if check_routers in routers:
    print(check_routers, "is in the list")
else:
    print(check_routers, "is not in the list")    

# Sorting of list 
# 
my_sorting_list = [4.5, 6.3, 7.1, 7.3, 8, 7.4, 6.7, 8.1, 6.2, 10.5]
my_sorting_list.sort()  # ascending manner 
print(my_sorting_list) 

my_sorting_list.sort(reverse=True)
print(my_sorting_list)

switches = ["juniper_1", "aruba_2", "pa_4", "amazon3.5"]
switches.sort()
print(switches)
switches.sort(key=len, reverse=True)  # custom sorting 
print(switches)

switches.sort(key=str.lower) # alphabetical sorting
print(switches)

switches = ["juniper_1", "aruba_2", "pa_4", "amazon3.5", str(5.5), str(6), str(3.4455)]
switches.sort()
print(switches)
