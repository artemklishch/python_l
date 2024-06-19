import random

print(random.random())  # by default from 0 to 1(not included)
print(random.randint(1, 10))  # by default from 1 to 10 included both numbers

print(random.choice('abcd'))  # random letter
print(random.choice([1, 10, 14]))

print(random.choices([1, 10, 12, 4], k=2))

l1 = [1, 10, 12, 4]
random.shuffle(l1)
print(l1)

print(''.join(random.choices('ABCDEF0123456789', k=8)))
