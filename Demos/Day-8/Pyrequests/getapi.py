# Python requests library with HTTP requests and web resources. 

# The python requests module comes with GET, POST, PUT, DELETE HTTP operations. 
# HTTP GET is to retrieve the contents from REST API 

# parameters are used - 
# 1. url -> The URL you would like to send to (required)
# 2. params -> Dictionary or bytes to be sent in the query string for GET requests (optional)
# 3. **kwargs -> Additional optional arguments such as headers, cookiesm authentication, timeout, proxies etc. 
# Return type -> response object 
# 
# Make a simple GET request 
# 

import requests
response = requests.get("https://www.google.com")
print(response.status_code) 

# sending GET request with Parameters 

import requests
response = requests.get("https://api.github.com/users/imcuteani")
print(response.status_code)
print(response.content)