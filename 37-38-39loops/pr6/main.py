d1 = {
    'a': 'tom',
    'b': 'Alice',
    'c': 'Bob'
}
d2 = {k: v.upper() for k, v in d1.items()}
print(d2)

l1 = ['as', 'dfsgd', 'fg', 'fgfgfgfgfg']
l2 = [v for v in l1 if len(v) > 3]
print(l2)
