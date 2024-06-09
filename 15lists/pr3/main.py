my_fruits = ["apple", "banana", "lime"]

posts_ids = [151, 245, 762, 167]

user_inputs = [True, "hi!", 10.5, '⚜️']

# coping the list

# copied_fruits = my_fruits[:]
# copied_fruits = my_fruits.copy()
copied_fruits = list(my_fruits)

copied_fruits.append('peer')
print(copied_fruits)
print(my_fruits)

my_nums = [10, 50, 0, 5, 100]
my_nums.insert(1, 12)
print(my_nums)
print(my_nums.count(5))
# my_nums = []
# my_nums.clear()
# print(my_nums)  # []

my_nums.extend('abc')
print(my_nums)  # [10, 12, 50, 0, 5, 100, 'a', 'b', 'c']
other_nums = my_nums.copy()
other_nums.append(3)
print(other_nums)
