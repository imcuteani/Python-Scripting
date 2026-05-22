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