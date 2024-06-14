l1 = [-3, 1, 0, 10, -20, 5]

abs1 = []
for num in l1:
    abs1.append(abs(num))
print(abs1)

abs2 = [abs(num) for num in l1]  # [3, 1, 0, 10, 20, 5]
print(abs2)
print(l1)  # [-3, 1, 0, 10, -20, 5]

abs3 = [num for num in l1 if num > 0]  # [1, 10, 5]
print(abs3)

set = {1, 10, 15}
s1 = {val * val for val in set}
print(s1)  # {1, 100, 225}

d1 = {
    'a': 10,
    'b': 7,
    'c': 14,
}
sc = {k: v * 10 for k, v in d1.items()}
print(sc)  # {'a': 100, 'b': 70, 'c': 140}

print({v * 10 for k, v in d1.items()})  # {140, 100, 70}
print([v * 10 for k, v in d1.items()])  # [140, 100, 70]
print({index: value for index, value in enumerate([140, 100, 70])})  # {0: 140, 1: 100, 2: 70}
#  enumerate returns index-value


