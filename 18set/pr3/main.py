# my_set = {'abc', 'd', 'f'}
# copied_set = my_set.copy()
#
# my_set.add('t')
# copied_set.add('l')

# print(my_set & copied_set)  # пересечение
# print(my_set.symmetric_difference(copied_set)) # extracting exceptional elements

a = {'abc', 'd', 'f', 'y'}
b = {'abc', 'd', 'f', 'l'}
print((a | b) - (a & b))
print(a.symmetric_difference(b))
