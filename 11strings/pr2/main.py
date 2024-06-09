print(type("Artem"))  # returns the data type

info_msg = """
You are learning the 

easiest
programming language - 
Python!
"""
# """ - output the string as it is in the editor
print(info_msg)
print(type(info_msg))
print(type(str))
print(type(int))

my_name = "Artem"
print(len(my_name))  # returns the string length
print(my_name[0])  # returns the symbol by index

# returns the sequence of symbols in range, including first index and excluding last index in square brackets
print(my_name[2:4])
print(my_name[3:])  # returns all string after 3 index, including 3

print(my_name.upper())  # returns string in uppercase
print(my_name.lower())  # returns string in lowercase

print(my_name.index("r"))  # returns the index of "r" symbol
