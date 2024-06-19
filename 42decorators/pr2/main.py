def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Function name is {fn.__name__}")
        print(f"Function arguments are: {args}, {kwargs}")
        result = fn(*args, **kwargs)
        print(f"Function result is: {result}")
        return result

    return wrapper


@log_function_call
def mult(a, b):
    return a * b


print(mult(5, 2))
print(mult(a=5, b=2))


@log_function_call
def sum_foo(a, b):
    return a + b


print(sum_foo(2, 2))
