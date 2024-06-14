import random

i = 1

while i < 10:
    print(i)
    i += 1

random_num = random.randint(1, 5)
while True:
    num = int(input("Guess the number from 1 to 5: "))
    if num != random_num:
        print('Try again')
        continue
    print("Congrats!")
    break


