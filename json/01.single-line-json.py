#single line JSON object
person='{"id":1,"first_name":"saurabh","last_name":"visal","email":"saurabhvisal92@gmail.com","gender":"Male","ip_address":"192.168.0.1"}'

#Single JSON span over multiple lines

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
print(type(person))
print(type(person_multiLine))