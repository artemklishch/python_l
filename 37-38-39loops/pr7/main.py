from sys import getsizeof

nums = (3, 5, 10)
squares = (num * num for num in nums)

print(squares)
print(type(squares))

squares1 = (num * num for num in range(6))
print(squares1)

# print(squares1[2]) # error, impossible to fetch element by index

for num in squares1:
    print(num)

squares3 = (num * num for num in range(100_000_000))
l = [num * num for num in range(100_000_000)]
print(getsizeof(squares3))
print(getsizeof(l))
