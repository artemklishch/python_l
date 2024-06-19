# import re
#
# str1 = "My name is Bob."
# str2 = "My name is Bob!"
#
# # res1 = re.search(r'My.*\.$', str1)
#
# pat1 = re.compile(r'My.*\.$')
#
# print(pat1)
#
# print(pat1.match(str1))
# print(pat1.match(str2))

import re

str1 = "My name is Bob. Bib is instructor"

pat1 = re.compile(r'B.b')

print(pat1)

print(pat1.findall(str1))
