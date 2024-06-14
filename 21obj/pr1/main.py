from copy import deepcopy

n1 = 10
n2 = 10
print(id(n1))
print(id(n2))
n2 += 2
print(id(n1))
print(id(n2))

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)
print(id(l1))
print(id(l2))

obj1 = {
    'name': "Bob",
    'age': 20
}
ref1 = obj1
print(id(obj1))
print(id(ref1))

obj2 = obj1.copy()
print(id(obj2))

obj3 = {
    'name': 'Alice',
    'is_instructor': True,
    'reviews': [1, 2]
}
# obj4 = obj3.copy()  # it does not do deep copy
# obj3['reviews'].append(12)
# print(obj3)
# print(obj4)
obj4 = deepcopy(obj3)
obj3['reviews'].append(12)
print(obj3)
print(obj4)