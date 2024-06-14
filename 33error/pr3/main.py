try:
    print('10' / 0)
except Exception as e:
    print("Error: ", e)

try:
    print(10 / 0)
except:
    print("Error occured")  # not reccomended

print("Continue...")
