import re

str1 = "My name is Bob"

res1 = re.search('Bob', str1)
print(res1)  # <re.Match object; span=(11, 14), match='Bob'>

res2 = re.search('B.b', str1)
print(res2)  # <re.Match object; span=(11, 14), match='Bob'>

res3 = re.search('B.....b', str1)
print(res3)  # None

str2 = "My name is Bob!"
res4 = re.search('B.b$', str2)  # end
print(res4)  # None

print(re.search('^M.*name', str2))  # <re.Match object; span=(0, 7), match='My name'>

str3 = "My name is Bob."
print(re.search('B.b\.$', str3))
print(r'B.n\n.$')  # r - means disabling '\n' symbol

print(res2.span())  # (11, 14)
print(res2.start())
print(res2.end())
