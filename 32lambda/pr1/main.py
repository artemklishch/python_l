def mult(a, b): return a * b


print(mult(10, 5))

mult1 = lambda a, b: a * b  # not recommended to assign lambda to variable
print(mult1(2, 10))


def greeting(greet):
    return lambda name: f"{greet}, {name}"


def greeting1(greet):
    def info(name):
        return f"{greet}, {name}"

    return info


morning_greet = greeting("Good morning")
morning_greet1 = greeting("Good morning")
print(morning_greet("Bob"))  # Good morning, Bob
print(morning_greet1("Bob"))  # Good morning, Bob
