d = {
    'x': 10,
    'y': True,
}

print(d.items())

for item1 in d.items():
    key, value = item1
    print(key, value)

for k1, v1 in d.items():
    print(k1, v1)

s1 = {1435, 4317, 2761, 5721}
for el1 in s1:
    print(el1)

st1 = "Bob"
for el2 in st1:
    print(el2)

for el3 in range(5):
    print(el3)


def dict_to_list(data):
    list_of_pair_items = data.items()
    result_list = []
    for k, v in list_of_pair_items:
        result_list.append((k, v * 2 if type(v) == int else v))
    return result_list


print(dict_to_list({'name': 'bob', 'age': 10}))


def filter_list(data_list, datatype):
    res_list = []
    for v in data_list:
        if type(v) == datatype:
            res_list.append(v)
    return res_list


print(filter_list([1, 2, 'sdfsdf', True], int))
