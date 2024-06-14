def filter_list(data_list, datatype):
    # def check_element_type(elem):
    #     return type(elem) is datatype
    # return list(filter(check_element_type, data_list))
    return list(filter(lambda elem: type(elem) is datatype, data_list))


print(filter_list([1, 2, 'sdfsdf', True], int))
print(list(filter(lambda elem: type(elem) is int, [1, 2, 'sdfsdf', True])))

print(isinstance(True, int))
print(isinstance(True, bool))
print(isinstance(True, object))