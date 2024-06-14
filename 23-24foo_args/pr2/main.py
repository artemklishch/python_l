def merge_lists_to_dict(list_one, list_two):
    merged_list = zip(list_one, list_two)
    return dict(merged_list)


res1 = merge_lists_to_dict(list_one=[1, 2, 3], list_two=['Bob', 'Alice', 'Rob'])
print(res1)
res2 = merge_lists_to_dict([1, 2, 3], list_two=['Bob', 'Alice', 'Rob'])
print(res2)


def update_car_info(**car):
    updatedCar = car.copy()
    updatedCar['is_available'] = True
    return updatedCar


print(update_car_info(name='Audi', year=2000))
