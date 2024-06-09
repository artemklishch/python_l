my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2,
    'price_info': {
        'total': 250000,
        'is_avalable': True
    }
}
print(my_motorbike['brand'])  # Ducati
# print(dir(my_motorbike))
my_motorbike['price'] = 7000;
print(my_motorbike)
my_motorbike['color'] = 'red'
print(my_motorbike)
del my_motorbike['engine_vol']
print(my_motorbike)

key_name = 'brand'
print(my_motorbike[key_name])
print(my_motorbike['price_info']['total'])
print(len(my_motorbike))
# print(my_motorbike['ffff']) # error
print(my_motorbike.get('fff'))  # None
print(my_motorbike.get('fff', 56))  # 56

# print(my_motorbike.__doc__)
# dict() -> new empty dictionary
# dict(mapping) -> new dictionary initialized from a mapping object's
#     (key, value) pairs
# dict(iterable) -> new dictionary initialized as if via:
#     d = {}
#     for k, v in iterable:
#         d[k] = v
# dict(**kwargs) -> new dictionary initialized with the name=value pairs
#     in the keyword argument list.  For example:  dict(one=1, two=2)
