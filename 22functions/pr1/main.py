def my_fn(a, b):
    print(id(a))  # 10781704
    a = a + 1
    c = a + b
    print(id(a))  # 10781736
    return c


av = 2
print(id(av))  # 10781704
bv = 3
print(my_fn(av, bv))
print(id(av))  # 10781704


def my_fn1():
    pass


print(my_fn1())


def increase_person_age(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy


person_one = {
    'name': 'Bob',
    'age': 21
}
print(increase_person_age(person_one)['age'])  # 22
print(person_one['age'])  # 21
