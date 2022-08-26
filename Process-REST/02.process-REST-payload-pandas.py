# Below code will process the REST data using python pandas.

import requests
import pandas as pd

url="https://api.github.com/repositories"

input_since=input("Enter the repo id from which you want to get the repositories: ")

payload={
    'since':{input_since}
}
headers={}

response=requests.request("GET",url=url,headers=headers,params=payload).json()

# Convert the JSON response or list of dicts to pandas dataframe
response_df=pd.json_normalize(response)

# To get the columns
#print(response_df.columns)

#To get the column and count
#print(response_df.shape)

# Get the repository name,url and owner type
# selected_df=response_df[['name','url','owner.type']]
# print(selected_df)

#Get all unique owner type of the repositories.The output should of type list.
#unique_owner_type=response_df['owner.type'].unique()
# This returns a numpy array.
#print(unique_owner_type)
# This will return the list
# print(list(unique_owner_type))

# Get number of of repositories where owner type is User
#user_owner_type_df=response_df[response_df['owner.type']=='User']
# This will return all the columns from df where owner type is User
#print(user_owner_type_df)
# This will return a touple with count which matches our criteria along with number of columns in the DF
#print(user_owner_type_df.shape)
#This will return the count which matches our criteria
# print(user_owner_type_df.shape[0])


# Get number of of repositories where owner type is Organization
#organization_owner_type_df=response_df[response_df['owner.type']=='Organization']
# This will return all the columns from df where owner type is User
#print(organization_owner_type_df)
# This will return a touple with count which matches our criteria along with number of columns in the DF
#print(organization_owner_type_df.shape)
#This will return the count which matches our criteria
#print(organization_owner_type_df.shape[0])

# Get the number of repositories by each owner type
# count_by_owner_type_df=response_df.groupby('owner.type')['owner.type'].count()
# print(count_by_owner_type_df)

# Sort the data
sorted_data=response_df.sort_values(by=['owner.type','id'])
print(sorted_data.head(10))

