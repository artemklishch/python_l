from pathlib import Path

test_file = open('test.txt', 'w')

# print(test_file)
# print(type(test_file))

test_file.write("First string\n")
test_file.write("Second string\n")

# print(test_file.read()) # error, impossible to read when writable mode

test_file.close()

test_file = open('test.txt')
print(test_file.read())
test_file.close()

with open('test.txt') as test_file:
    for line in test_file.readlines():
        print(line)

with open('test.txt') as test_file:
    while True:
        line = test_file.readline()
        print(line)
        if not line:
            break

# test_file = Path('test.txt')
# if test_file.exists():
#     test_file.unlink()