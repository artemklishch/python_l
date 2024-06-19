class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


class MyExtendedList(ExtendedList):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


l1 = ExtendedList([3, 5, 2])
l1.print_list_info()  # List has 3 elements

l1.append(4)
l1.print_list_info()  # List has 4 elements
print(list.__subclasses__())  # [<class 'functools._HashedSeq'>, <class '__main__.ExtendedList'>]
print(ExtendedList.__subclasses__())  # [<class '__main__.MyExtendedList'>]


