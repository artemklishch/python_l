import re
import string


def check_password(password):
    pattern_length = re.compile(r"\S{8,}")
    pattern_lowercase = re.compile(r"^.*[a-z]+.*$")
    pattern_uppercase = re.compile(r"^.*[A-Z]+.*$")
    pattern_numbers = re.compile(r"^.*[0-9]+.*$")
    pattern_special_characters = re.compile(fr"^.*[{string.punctuation}]+.*$")
    patter_no_whitespaces = re.compile(r"^\S*$")

    if not re.match(pattern_length, password):
        return False, "Password must have at least 8 symbols"

    if not re.match(pattern_lowercase, password):
        return False, "Password must have at least one lowercase letter"

    if not re.match(pattern_uppercase, password):
        return False, "Password must have at least one uppercase letter"

    if not re.match(pattern_numbers, password):
        return False, "Password must have at least one number"

    if not re.match(pattern_special_characters, password):
        return False, "Password must have at least one special symbol"

    if not re.match(patter_no_whitespaces, password):
        return False, "Password must have no spaces"

    return True, "Password is valid"


print(check_password("123"))
print(check_password("123456789"))
print(check_password("123456789a"))
print(check_password("123456789B"))
print(check_password("fgghGHFJFjfjgB"))
print(check_password("fgghGHFJFjfjgB3542345"))
print(check_password("fgghGHFJFjfjgB3  425**"))
print(check_password("fgghGHFJFjfjgB3425**"))
