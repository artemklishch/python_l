l1 = [True, 10, 'abc', {}]
t1 = (True, 10, 'abc', {})

for elem1 in l1:
    print(elem1)

for elem2 in t1:
    print(elem2)

d1 = {
    'x': 10,
    'y': True,
    'z': 'abc',
}
for elem3 in d1:
    print(elem3, d1[elem3])

print(elem1)  # global visibility
print(dir())
