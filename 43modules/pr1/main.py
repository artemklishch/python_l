# import other
#
# print(other)
# print(
#     dir(other))  # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'my_name', 'print_sum']
#
# other.print_sum(2, 2)

from other import my_name, print_sum

print(my_name)
print_sum(2, 5)
