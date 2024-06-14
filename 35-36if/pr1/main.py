n1 = 25

if n1 > 0:
    print("yes")

p1 = {
    'age': 20
}

if not p1.get('name'):
    print("no name")

n2 = 10
n3 = 5
if (n2 > 0 and
        n3 > 0 and
        isinstance(n2, int) and
        isinstance(n3, int)):
    print("Both numbers are ints and positive")

n4 = 21
if type(n4) is int:
    print("is integer")
elif type(n4) is float:
    print("is float")
else:
    print("is not a number")


def num_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = "One of args is not integer"
    elif a >= b:
        info = f"{a} greater or equal {b}"
    else:
        info = f"{a} less {b}"
    return info  # it works because there is not block visibility in Python
