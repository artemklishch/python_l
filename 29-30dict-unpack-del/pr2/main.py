d = {'a': True, 'b': 10}
del d['a']

print(d)  # {'b': 10}

d.__delitem__('b')

print(d)  # {}

l = [1, 2]
del l[0]
print(l)  # [2]
