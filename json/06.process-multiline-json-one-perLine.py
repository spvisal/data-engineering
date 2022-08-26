import json

persons='''{"id":1,"first_name":"saurabh","last_name":"visal","email":"saurabhvisal92@gmail.com","gender":"Male","ip_address":"192.168.0.1"}
{"id":2,"first_name":"neeraj","last_name":"visal","email":"neerajvisal@gmail.com","gender":"Male","ip_address":"192.168.0.2"}
{"id":3,"first_name":"prakash","last_name":"visal","email":"prakashvisal@gmail.com","gender":"Male","ip_address":"192.168.0.3"}
{"id":4,"first_name":"mrunmayee","last_name":"talwalkar","email":"mrunmayee.talwalkar@gmail.com","gender":"Female","ip_address":"192.168.0.4"}
{"id":5,"first_name":"aryan","last_name":"visal","email":"aryanvisal@gmail.com","gender":"Male","ip_address":"192.168.0.5"}
{"id":6,"first_name":"manasi","last_name":"satbhai","email":"satbhaimanasi@gmail.com","gender":"Female","ip_address":"192.168.0.6"}
{"id":1,"first_name":"varsha","last_name":"wale","email":"vp.visal@gmail.com","gender":"Female","ip_address":"192.168.0.7"}'''

#split the string into multiple line using a function called splitlines. Use \n as delimiter.

person_list=persons.splitlines()

person_list_dict=[]

#Conventional for loop
for person in person_list:
    person_list_dict.append(json.loads(person))

# print(type(person_list_dict))

# print(person_list_dict[0])

# print(person_list_dict[0]['first_name'])

# List comprehension
#person_list_dict=[json.loads(person) for person in person_list]

#print(type(person_list_dict))

# Using map function

person_list_dict_l = list(map(json.loads,person_list))

#once the data is in the list you can use row level transformation

#print only first name
print(list(map(lambda person: (person['first_name'], person['last_name'], person['email']),person_list_dict_l)))

# print only female names

#print(list(filter(lambda person:person['gender']=="Female",person_list_dict_l)))