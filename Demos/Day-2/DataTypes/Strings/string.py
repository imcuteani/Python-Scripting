# Creating strings

my_var = 'Switch-A'
print(my_var)

# mixed quotes 

mixed_quotes = "It's a great day to learn Python with 'Network Automation'!"
print(mixed_quotes)

# multi-line strings , mixed quotes will not work for multiline strings
multi_line = '''This is the first network switch A,
this is the second network switch B'''
print(multi_line)

# String methods 
# String methods create a new string and leave the origin string unchanged. To keep the result, you need t
# assign it to a new variable or overwrite the original one. 

my_var = "Cisco router AB"
my_var = my_var.upper()
print(my_var)

# split() methods in string of Python 

# The .split() method breaks down strings into smaller parts. By default, it splits the strings at spaces, 
# turning a sentence into individual words and returning them as a list. 
# 
sentence = "This is a sentence for firewall and load balancer configuration"
words = sentence.split()
print(words) 

# you can customize the .split() method by specifying a seperator. To split an IP addr. 

ip_addr = "172.30.20.15"
components = ip_addr.split(".")
print(components)

# The .splitlines() method splits a string into seperate lines based on line breaks. This is useful for multiline 
# text data. 

multiline_text = "the first network switch A.\nsecond switch B.\nAnd third network switch C."
lines = multiline_text.splitlines()
print(lines)


# join() method 
# The join() method in python strings is the opposite of split method. It lets to merge a list of strings
# into one string. This is useful for creating strings with custom seperators. 

octets = ['172', '31','15', '21']
ip_address = ".".join(octets)
print(ip_address)

# .strip() method for Strings in Python 

# The .strip() method removes the leading and trailing whitespaces from a string. This includes 
# tabs, spaces, newline characters. 

sentence = " In this example, we can use leading and whitespaces for IP CIDR declaration.  "
cleaned_sentence = sentence.strip()
print(cleaned_sentence)

# to remove leading spaces 

sentence = " In this example, we can use leading and whitespaces for IP CIDR declaration.  "
cleaned_sentence = sentence.lstrip()
print(cleaned_sentence)

# to remove only trailing spaces 

sentence = " In this example, we can use leading and whitespaces for IP CIDR declaration.  "
cleaned_sentence = sentence.rstrip()
print(cleaned_sentence)


# search substrings in Python 

# searching for specific keywords or patterns in configuration file is essential. 
# The find() method helps you to locate substrings within a string and determine their position. 
# 
config = "hostiname R1\nip address 192.168.1.1"
position = config.find("ip address") # index of "ip address"
print(position) 

# startswith() & endswith() methods 

ipaddr = '10.1.1.1'
print(ipaddr.startswith('20'))
print(ipaddr.endswith('5'))

