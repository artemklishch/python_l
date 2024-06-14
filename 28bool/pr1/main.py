my_list = []
my_list1 = [1, 2]

print(not my_list)  # True
print(not my_list1)  # False

my_list2 = [1, 2]
other_list = ['a', 'b']
print(my_list2 or other_list)  # [1, 2]
print(len(my_list2) > 0 or other_list)  # True

print([1, 2] and {})  # {}
print(bool([1, 2] and {}))  # False

my_list2 and print('List is not empty')  # 'List is not empty'
my_list and print('List is not empty')  #
