# Consuming JSON API in Python using HTTP requests 

# Sending the data to an JSON API 

# work with local json data 

# a) json.loads() -> Parses a string to a python object. (JSON -> Python)
# b) json.load() -> Reads from a file object into Python (File -> Python)
# c) json.dump() -> Writes python data into a JSON formatted string (Python -> File)
# d) json.dumps -> converts python data into JSON string (Python -> JSON)

# Consuming a JSON API 

import requests

# send a GET request to the API endpoint 

response = requests.get("https://jsonplaceholder.typicode.com/posts")

# check if the connection is successful or not 

if response.status_code == 200:
    # automatically parse the JSON into python dictionary 
    data = response.json()
    print(data[2]["title"]) # based on position of items access the json keys
  
else: 
    print(f"Error: {response.status_code}")

# sending JSON data to an API (Post request)
# 
# To send data into an API , pass a dictionary to the json parameter inside the requests.post(). This automatically sets 
# correct header (Content-Type: application/json) and stringifies the http payload 
# 

import requests

payload = {
    "deviceId": "XE01",
    "deviceName": "CiscoIOS"
}

response = requests.post("https://httpbin.org/post", json=payload)
print(response.json())

# string manipulation with JSON API 

import json 

# convert a json string to python dict (deserialization)

json_str = '{"deviceno": "IOS01", "devicetype": "cisco", "active": true}'
python_dict = json.loads(json_str)
print(python_dict)           # output python dict
print(type(python_dict))     # output of 'class dict'   
print(python_dict["devicetype"])  # output of json key

# Converting python Dict into a formatted JSON string (serialization)

formatted_str = json.dumps(python_dict, indent=2)  # for indentation 
print(formatted_str)