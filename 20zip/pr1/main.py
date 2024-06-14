# fruits = ['apple', 'banana', 'lime']
# quantities = [100, 70, 50]
#
# fruits_qtys_zip = zip(fruits, quantities)
# print(fruits_qtys_zip) # <zip object at 0x767962d83d40>
#
# fruits_qtys_list = list(fruits_qtys_zip)
# print(fruits_qtys_list) # [('apple', 100), ('banana', 70), ('lime', 50)]

fruits = ['apple', 'banana', 'lime', 'orange']
quantities = [100, 70, 50, 14]
availability = [True, False, False, True]

fruits_qtys_zip = zip(fruits, quantities, availability)

fruits_qtys_list = list(fruits_qtys_zip)
print(fruits_qtys_list)  # [('apple', 100, True), ('banana', 70, False), ('lime', 50, False), ('orange', 14, True)]
