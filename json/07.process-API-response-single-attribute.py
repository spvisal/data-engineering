import json

# multiline JSON
persons_multiLine = '''{
    "result":[
    {
        "id":1,
        "first_name":"saurabh",
        "last_name":"visal",
        "email":"saurabhvisal92@gmail.com",
        "gender":"Male",
        "ip_address":"192.168.0.1"
    },
    {
        "id":2,
        "first_name":"neeraj",
        "last_name":"visal",
        "email":"neerajvisal@gmail.com",
        "gender":"Male",
        "ip_address":
        "192.168.0.2"
    },
    {
        "id":3,
        "first_name":"prakash",
        "last_name":"visal",
        "email":"prakashvisal@gmail.com",
        "gender":"Male",
        "ip_address":"192.168.0.3"
    },
    {
        "id":4,
        "first_name":"mrunmayee",
        "last_name":"talwalkar",
        "email":"mrunmayee.talwalkar@gmail.com",
        "gender":"Female",
        "ip_address":"192.168.0.4"
    },
    {
        "id":5,
        "first_name":"aryan",
        "last_name":"visal",
        "email":"aryanvisal@gmail.com",
        "gender":"Male",
        "ip_address":"192.168.0.5"
    },
    {
        "id":6,
        "first_name":"manasi",
        "last_name":"satbhai",
        "email":"satbhaimanasi@gmail.com",
        "gender":"Female",
        "ip_address":"192.168.0.6"
    },
    {
        "id":1,
        "first_name":"varsha",
        "last_name":"wale",
        "email":"vp.visal@gmail.com",
        "gender":"Female",
        "ip_address":"192.168.0.7"
    }
    ]
}
'''

person_dict=json.loads(persons_multiLine)

print(type(person_dict))

print(person_dict.keys())

print(person_dict['result'][0])