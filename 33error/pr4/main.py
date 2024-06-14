def divide_nums(a, b):
    if b == 0:
        raise TypeError("Second argument acn not be 0")
    return a / b


def divide_nums1(a, b):
    if b == 0:
        raise ValueError("Second argument acn not be 0")
    return a / b


print(divide_nums(4, 2))

try:
    divide_nums(4, 0)
except TypeError as e:
    print(e)

try:
    divide_nums1(4, 0)
# except Exception as e:
#     print(e)
except ValueError as e:
    print(e)
