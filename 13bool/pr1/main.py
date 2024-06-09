is_authorized = True
print(is_authorized)
print(type(is_authorized))

print(100 > 24)
print(-5 > 0)
print("Long string" > "Long")  # посимвольне порівняння строк, True
print([1, 2, 3] == [1, 2, 3])  # посимвольне порівняння, True
print([1, 2, 3] == [1, 2, 3, 4])  # False
print(bool("asddas"))  # True
print(bool(""))  # False

print(bool(0))  # False
print(bool([]))  # False
print(bool(None))  # False
print({"a": 3} == {"a": 3})  # True
