my_range = range(7)

print(type(my_range))
print(list(my_range))

my_range2 = range(10, 20, 3)  # range(10, 20, 3)
print(my_range2)
# print(my_range[1])  # 1

# for n in my_range:
#     print(n)

for n in range(2, 7):
    print(n)

print(list(range(12, 25, 5)))
print(tuple(range(12, 25, 5)))
print(set(range(12, 25, 5)))

print(dir(my_range))
print(my_range.start)  # 0
print(my_range.stop)  # 7
print(my_range.step)  # 1
print(my_range.count(2))
