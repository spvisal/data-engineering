import json

#Open the file in read mode and pass it to json.load method. This method takes the file pointer as an input. It will return a dict

single_json=json.load(open('single-document.json'))

print(single_json.keys())