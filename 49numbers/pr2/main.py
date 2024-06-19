import secrets
import string

# print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)  # 0123456789
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#
# print(string.ascii_letters + string.digits + string.punctuation)

symbols = string.ascii_letters + string.digits + string.punctuation
print(''.join(secrets.choice(symbols) for i in range(20)))
