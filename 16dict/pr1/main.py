my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2,
}
other_motorbike = {
    'engine_vol': 1.2,
    'brand': 'Ducati',
    'price': 25000,
}
print(my_motorbike)
print(
    my_motorbike == other_motorbike)  # True, об'єкти різні, але дорівнює True, оскільки містять однакові дані, незалежно відпорядку ключів
print(id(my_motorbike) == id(other_motorbike))  # False
