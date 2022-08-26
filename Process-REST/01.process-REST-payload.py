# Below code will process the REST data using python core modules and methods.

from urllib import response
import requests
import itertools as iter

url="https://api.github.com/repositories"

input_since=input("Enter the repo id from which you want to get the repositories: ")

payload={
    'since':{input_since}
}
headers={}

response=requests.request("GET",url=url,headers=headers,params=payload).json()

# Getting repo name and URL
# for repo in response:
#     print(f"{repo['name']}:{repo['url']}")

# Another way of doing it
#repo_urls=[{'name':repo['name'], 'repo_url':repo['url']} for repo in response]

# Using the lambda function
#repo_urls=list(map(lambda repo:{'name':repo['name'],'repo_url':repo['url']},response))

# Some of the common operation

#Operation 1. Get the length
#print(len(response))

#Get the repository name, url and owner type of all repositories. Each element in the new list should be of type "tuple"
#processed_data=list(map(lambda repo: (repo['name'],repo['url'],repo['owner']['type']),response))
#print(processed_data)

#Get distinct owner type from all the repositories. The output should be of type list
# processed_data=list(set(map(lambda repo:repo['owner']['type'],response)))
# print(processed_data)

#Get the number of repositories where owner type is User
# processed_data=len(list(filter(lambda repo:repo['owner']['type']=='User',response)))
# print(processed_data)

#Get the number of repositories where owner type is Organization
# processed_data=len(list(filter(lambda repo:repo['owner']['type']=='Organization',response)))
# print(processed_data)

#Get the number of repositories by each owner type

#before performing the group by operation data must be sorted

#sorted_data=sorted(map(lambda repo:repo['owner']['type'],response))

# First approach
# for item in iter.groupby(sorted_data):
#     print((item[0],len(list(item[1]))))

# Second approach
# processed_data=list(map(lambda repo: (repo[0], len(list(repo[1]))),iter.groupby(sorted_data)))

# print(processed_data)

# Sort the data by owner type and then by id.

# sorted_data=sorted(response,key=lambda repo:(repo['owner']['type']))

# print(sorted_data)

