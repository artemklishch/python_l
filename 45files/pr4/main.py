from pathlib import Path

with open('test.txt') as test_file:
    print(test_file.read())

with open('test.txt') as test_file:
    print(test_file.readlines())

with open('new.txt', 'w') as new_file:
    print(new_file.write("This is what we write here...\n"))

with open('new.txt') as new_file:
    print(new_file.read())  # This is what we write here...

with open('new.txt', 'a') as new_file:
    print(new_file.write("Second line...\n"))

with open('new.txt') as new_file:
    print(new_file.read())  # This is what we write here...
# Second line...

# Path('new.txt').unlink() # this expression deletes the file
