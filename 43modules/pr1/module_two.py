# import module_one
#
# print(type(module_one))
# print(dir(module_one))
#
# module_one.print_name("Bob")

# import module_one as m_one
#
# m_one.print_name("Bob")

from module_one import print_name

print_name("Bob")
