import json

#It will returnt the list
customer_list= open('customer.json').read().splitlines()

#check the data type
print(type(customer_list))

#check the data type of a element
print(type(customer_list[0]))

#Conver the list into dict. It will return the list of dict
customer_dict=[json.loads(customer) for customer in customer_list]

#list of dict
print(type(customer_dict))

#Check the type
print(type(customer_dict[0]))