import getpass
import telnetlib

user = input("Enter Username:")
password = getpass.getpass()
print('Successfully passed getpass')

tn = telnetlib.Telnet(host="192.168.80.129", port="5004")
print('Successfully passed telnet')
tn.write(b"show ip interface brief\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"int loopback 1\n")
tn.write(b"ip add 1.1.1.1 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"exit\n")
print(tn.read_all().decode("ascii"))


   
    