elements = ["some name", 25, True, 12.5, {'name': "Bob"}]
elements.pop(2)
print(len(elements))
elements.reverse()
other_elements = ["main", 256]
elements += other_elements
print(elements)

print("======")

el1 = [1, 2, 3, 4]
el2 = [5, 6, 7, 8]
all_els = el1 + el2
all_els2 = el1.__add__(el2)
print(all_els2)

print("===")
