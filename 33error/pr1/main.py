try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error occured...")

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Error: ", e)  # Error:  division by zero

print("Continue")
