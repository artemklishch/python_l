# print("10" + 5) # error no obvious converting data types
# print(5 + "10") # error

int_num = 5
float_num = 4.5
print(int_num + float_num)  # no error, no obvious converting data types works
print(float_num + int_num)  # no error
#  it works firstly as print(int_num.__add__(float_num)) # magic method under the hood
print(int_num.__add__(float_num)) # NotImplemented
print(float_num.__radd__(int_num)) # this is the next operations, following after previous

bool_val = True
int_val = 7
print(bool_val + int_val)  # no error, 8
print(int_val + bool_val)  # no error, 8

#  magic method always begins and ends with two underscores - "__add__"


