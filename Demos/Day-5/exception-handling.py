# Exception handling in python starts with try & except block. 

# the try block is responsible to put the code which might cause exceptions. If an exception occurs during running the 
# code inside it, control has been passed to the corresponding except block. 

# except block is where we define what logic to apply when there's an exception. 

try: 
    my_ip_list = []
    print(my_ip_list[0]) # exception in code 
except IndexError:
    print("IP Index doesn't exist")   


# using Paramiko library for handling SSH exception 
# 
#from paramiko import SSHException

try:
    x = int(input("What's x?"))
    result = x/2
    
except (TypeError, ValueError):
    print("A type or value error has occured")   

# input to be taken from CLI 
# 
try:
    ip_addr = input('Enter your IP addr:')
    device_name = input("provide your device name:")
    device_id = 1990 - device_name
    print(f'The IP addr {ip_addr}. And your device id is {device_id}')  
except TypeError:
    print('Type error has occurred')
except ValueError:
    print('Value Error has occurred') 
except ZeroDivisionError:
    print('zero division error occurred')               
