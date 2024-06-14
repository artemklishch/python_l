fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]

fruits_qtys_zip = zip(fruits, quantities)

fruits_qtys_dict = dict(fruits_qtys_zip)
print(fruits_qtys_dict)  # {'apple': 100, 'banana': 70, 'lime': 50}
