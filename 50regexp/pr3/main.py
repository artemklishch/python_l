import re


# email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
#
# email_check_pattern = re.compile(email_regexp)
#
# print(email_check_pattern.fullmatch('bs@gmail.com'))
# print(email_check_pattern.fullmatch('bsgmail.com'))
# print(email_check_pattern.fullmatch('bs@.com'))
# print(email_check_pattern.fullmatch('gmail.com'))


def check_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)
    validation_result = "valid" if email_check_pattern.fullmatch(email) else "not valid"
    return (email, validation_result)


print(check_email('bs@gmail.com'))
print(check_email('bsgmail.com'))
print(check_email('bs@.com'))
print(check_email('gmail.com'))
