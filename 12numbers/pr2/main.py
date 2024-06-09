average_price = 17.25
print(average_price)
print(type(average_price))

str_temperature = "17.5"
print(float(str_temperature))
# print(int(str_temperature)) # it will be error

print(average_price.hex())
print(type(average_price.hex()))
print(average_price.is_integer())
print(average_price.__floor__())  # rounding
print(average_price.__round__())  # rounding
print(0.78.__round__())  # rounding

# complex numbers
complex_a = 3 + 5j  # real part is 3, no real part is 5j
complex_b = 4 + 7j
sum = complex_a + complex_b
#  7 + 12j ((3 + 4) + (5 + 7)j)

print(sum)
print(type(sum))

complex_aa = 10 + 7j
complex_bb = 3 + 3j
print(complex_aa + complex_bb)
print(complex_aa * complex_bb)  # (10 + 7j)(3 + 3j) = 30 + 30j + 21j + 21j^2
# (10 + 7j)(3 + 3j) = 30 + 30j + 21j - 21 = 9 + 51j
