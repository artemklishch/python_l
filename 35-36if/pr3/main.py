n1 = 21.5

print("is_int") if type(n1) is int else print("is not int")

my_img = ('1920', '1080')
print(f"{my_img[0]}x{my_img[1]}"
      if len(my_img) == 2
      else print("Incorrect image formatting")
      )

s = "123456"
print("Nice string" if len(s) < 255 else "Too long string")
