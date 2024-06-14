# button = {
#     'width': 200,
#     'text': 'Buy'
# }
#
# red_button = {
#     **button,
#     'color': 'red'
# }
#
# print(button)
# print(red_button)


button = {
    'width': 200,
    'text': 'Buy',
    'color': 'gray'
}

red_button = {
    **button,
    'color': 'red'
}

print(button)
print(red_button)

b1 = {
    'text': 'Buy',
    'nested': {
        'name': 'Bob'
    },
}
b2 = {
    'color': 'red'
}
b3 = {
    **b1,
    **b2
}
print(b3)  # {'text': 'Buy', 'nested': {'name': 'Bob'}, 'color': 'red'}
print(b1 | b2)  # {'text': 'Buy', 'color': 'red'}

b3['nested']['name'] = 'Alice'  # no deep copy made and be name will be changed for b3 and for b1
print(b3)
print(b1)
