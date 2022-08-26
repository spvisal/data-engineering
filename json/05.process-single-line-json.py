import json

#single line JSON document
person='{"id":1,"first_name":"saurabh","last_name":"visal","email":"saurabhvisal92@gmail.com","gender":"Male","ip_address":"192.168.0.1"}'

#Single JSON document over multiple lines
person_multiLine= '''
    {
        "id":1,
        "first_name":"saurabh",
        "last_name":"visal",
        "email":"saurabhvisal92@gmail.com",
        "gender":"Male",
        "ip_address":"192.168.0.1"
    }
'''

# Here we will be using loads method which takes "JSON in string" and returns the "dict"
person_dict=json.loads(person)
#Check the data type of person_dict variable.
print(type(person_dict))

#Once the data is in the dictonary format you can perform the dict operation

print(person_dict['id'])
print(person_dict['first_name'])
#Here you will set type object as keys in dict are unique.
print(person_dict.keys())
# It will return the item in the form of tuple.
print(person_dict.items())