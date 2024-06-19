# def decorator_foo(fn):
#     def wrapper():
#         print("executed before function")
#         result = fn()
#         print("executed after function")
#         return result
#
#     return wrapper
#
#
# @decorator_foo
# def foo1():
#     print("This is my function")
#
#
# foo1()


# def decorator_foo(fn):
#     def wrapper(a, b):
#         print("executed before function")
#         result = fn(a, b)
#         print("executed after function")
#         return result
#
#     return wrapper
def decorator_foo(fn):
    def wrapper(*args, **kwargs):
        print("executed before function")
        result = fn(*args, **kwargs)
        print("executed after function")
        return result

    return wrapper

@decorator_foo
def foo1(a, b):
    print("This is my function")
    return (a, b)


res1 = foo1(100, 50)
print(res1)
