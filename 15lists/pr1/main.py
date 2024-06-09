my_fruits = ["apple", "banana", "lime"]

posts_ids = [151, 245, 762, 167]

user_inputs = [True, "hi!", 10.5, '⚜️']

print(my_fruits)
print(len(my_fruits))  # 3
print(my_fruits[0])  # "apple"

del user_inputs[1]
print(user_inputs)  # [True, 10.5, '⚜️']

users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
]
print(users[0]['user_id'])  # 134
# print(my_fruits[10]) # error, out of range
