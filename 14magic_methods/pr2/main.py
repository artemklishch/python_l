int_num = 50
float_num = 7.5

print(int_num.__mul__(float_num))  # NotImplemented
print(float_num.__rmul__(int_num))  # 375.0
print("abc" * 50)  # abcabcabc...
print(50 * "abc")  # abcabcabc...

print(dir(bool))
print(dir(bool).__doc__)
print(str.__doc__)
print(help([].__eq__))
