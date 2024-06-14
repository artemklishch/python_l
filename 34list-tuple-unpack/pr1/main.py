l1 = ['apple', 'banana', 'lime']
t1 = ('apple', 'banana', 'lime')

apple, banana, lime = l1
# apple1, banana1, lime1, something = l1 # error
print(apple, banana, lime)  # apple banana lime

apple2, banana2, lime2 = t1
print(apple2, banana2, lime2)  # apple banana lime

l2 = ['apple', 'banana', 'lime']
apple3, *test_l1 = l2
print(apple3, test_l1)  # apple ['banana', 'lime']
