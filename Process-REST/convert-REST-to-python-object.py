import requests

url="https://api.github.com"

headers={}
payload_data={}

# response=requests.request("GET",url,headers=headers,data=payload_data).content.decode('utf-8')

# A string with valid JSON
# print(response)
# print(type(response))
# response_dict=requests.request("GET",url=url,headers=headers,data=payload_data).json()

# dict
# print(response_dict)
# print(type(response_dict))


# Example of JSON array to list

url_with_json_array="https://api.github.com/users/spvisal/repos"

response_with_json_array=requests.request("GET",url=url_with_json_array,headers=headers,data=payload_data).json()

# Get the length
print(len(response_with_json_array))
# Get the first element
#print(response_with_json_array[0])
# Get the names of repo only
name=list(map(lambda repo:repo['name'],response_with_json_array))
print(name)