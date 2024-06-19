import json

dict1 = {
    'name': 'Bob',
    'age': 30,
    'isWorking': True
}

json_user = json.dumps(dict1)

print(json_user)
print(type(json_user))
