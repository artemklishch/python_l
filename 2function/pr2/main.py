import datetime


def date_foo():
    return datetime.MAXYEAR


print(date_foo())

my_number = 10
my_name = 'Artem'
is_valid = True

# immutable objects
# string, int, float, bool, tuple, None

# mutable objects
# list, dict, set, user classes

print(id(10))  # the 'id' method returns the identifier of object in memory

my_name1 = "Artem"
print(id(my_name1))

my_num = 100
other_num = my_num
print(id(my_num))
print(id(other_num))
