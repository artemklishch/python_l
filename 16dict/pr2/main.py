my_disk = {}

print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80
print(my_disk)
print(my_disk.items())
print(type(my_disk.items()))  # dict_items([('brand', 'Samsung'), ('price', 80)])
print(my_disk.keys())  # dict_keys(['brand', 'price'])
print(list(my_disk.keys()))
print(my_disk.popitem())  # deletes the last element ('price', 80) and returns it
print(my_disk)

other_disk = my_disk.copy()
my_disk['new_prop'] = "some new prop"
print(my_disk)
print(other_disk)

my_list = [['first', 0], ['second', True]]
my_list1 = [('first', 0), ['second', True]]

my_dict = dict(my_list)
my_dict1 = dict(my_list1)
print(my_dict)  # {'first': 0, 'second': True}
print(my_dict1)  # {'first': 0, 'second': True}
