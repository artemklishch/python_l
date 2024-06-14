set1 = {1, 2, 3}
set2 = {1, 2, 3}
print(set1 == set2)  # True
print(set1 is set2)  # False
print(1 in set1)  # True

# false values: None, False, "", 0, 0.0 0j, {}, [], (), set(), range(0)
print(not not {})
