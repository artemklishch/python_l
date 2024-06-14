# try:
#     print('10' / 0)
# except ZeroDivisionError as e:
#     print("Error: ", e)
# except TypeError as e:
#     print("Error: ", e)
# finally:
#     print("Final")
#
# print("Continue...")

try:
    print('10' / 0)
except ZeroDivisionError as e:
    print("Error: ", e)
except TypeError as e:
    print("Error: ", e)
else:
    print("There was no error")  # executed only when no errors happend
finally:
    print("Final")

print("Continue...")
