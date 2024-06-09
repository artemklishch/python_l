my_fruits = ('apple', 'banana', 'lime')

other_fruits = ('banana', 'apple', 'lime')

print(other_fruits == my_fruits)  # False

posts_ids = (151, 245, 762, 167)

user_inputs = (True, 'hi!', 10.5, None)

print(len(posts_ids))
print(posts_ids[1])

users = (
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
)

print(users[1]['user_id'])  # 831
users[1]['user_id'] = 100;
print(users[1]['user_id'])  # 100
# print(users[10]) # error

internal_ids = (151, 245)
external_ids = (624, 23)
all_ids = internal_ids + external_ids + (1,)
print(all_ids)

my_nums = (10, 5, 100, 0, 5, 5)
index1 = my_nums.index(5)
index2 = my_nums.index(5, index1 + 1)
index3 = my_nums.index(5, index2 + 1)

print(index1)
print(index2)
print(index3)

my_list = list(my_nums)
my_list.append("ererer")
my_nums = tuple(my_list)
print(my_nums)

my_tuple = tuple('abcd')
print(my_tuple)
