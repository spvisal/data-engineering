from urllib import request
import requests

url="https://api.github.com/users/spvisal/repos"

payload={}
headers={}

# Passing the empty header and payload.
response=requests.request("GET",url,headers=headers,data=payload)

#Check the response variable type.
#print(type(response))

#Following methods are available on top of response

# First Method
#print(response.text)
#Type of the response.text -> string
#print(type(response.text))

# Second Method
#print(response.json())
#Type of the response.JSON -> list of dict
#print(type(response.json()))

# Third Method
#print(response.content)
#Type of the response.content -> bytes
#print(type(response.content))

# Fourth Method- decode the content to string
print(response.content.decode('utf-8'))
# Type of the response.content.decode -> bytes
print(type(response.content.decode('utf-8')))
