def mult_by_factor(value, mult=1):
    """Multiplies number by multiplication"""  # description of the function
    return value * mult


mult_by_factor(5)


def print_number_info(num):
    """
    function description
    :param num: int number value
    :return: num
    """
    if (num % 2) == 0:
        print("Even")
    else:
        print("Odd")
    return num


print_number_info(3)

a = 10


def fn():
    # print(a) # error
    a = 2
    print(a)


fn()


def fn2():
    global b
    b = 1


fn2()
print(b)  # 1
