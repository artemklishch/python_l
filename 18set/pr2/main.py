my_fruits = {'apple', 'banana', 'lima'}
other_fruits = {'banana', 'apple', 'lima'}
posts_ids = {151, 245, 762, 167, 167, 151}

user_inputs = {True, 'hi!', 10.5}

my_set = {10, 10, 5, 15, 15, (10, 10)}
print(my_set)
my_set.add(12)
print(my_set)

other_set = {"fff", "ccc", 15}

union_set = my_set.union(other_set)  # same - my_set | other_set
print(union_set)
print(my_set.intersection(other_set))

my_set1 = {1, 20, 10, 12}
my_subset1 = {1, 10}
print(my_subset1.issubset(my_set1))

my_set2 = {'abc', 'd', 'f', 'y'}
other_set2 = {'a', 'f', 'd'}
print(my_set2.intersection('abc'))  # set()
print(my_set2.intersection('abcd'))  # {'d'} as if we pass ['a', 'b', 'c', 'd'] or ('a', 'b', 'c', 'd')

print(my_set2.difference(other_set2))  # {'abc', 'y'}
print(other_set2.difference(my_set2))  # {'a'}
print(my_set2 & other_set2)  # {'f', 'd'}

my_set2.discard('y')  # deleting method
print(my_set2)
