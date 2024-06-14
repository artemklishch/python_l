hello = "Hello"
world = "world"

greeting = f"{hello} {world}"

print(greeting)  # Hello world
print(hello + " " + world + str(8))  # Hello world8
print(f"{hello} {world}{8}")  # Hello world8
print((f"{hello} {world}{8}".title()))
