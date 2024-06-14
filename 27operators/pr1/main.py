v1 = 10  # присваивание

# + - / * ; > < == != >= <= ;
# not, and, or, is, is not, in, not in

v2 = 10
v3 = v1
print(v2 is v3)  # comparing by id

v4 = 10
print(+v4)  # явно показываем, что это число

print(+False)  # 0

print(not False)  # True

my_car = {
    'brand': 'Toyota',
    'price': 10_000
}
print('brand' in my_car)  # True
print('brand' not in my_car)  # False
