def merge_lists_to_dict(list_one, list_two):
    merged_list = zip(list_one, list_two)
    return dict(merged_list)


res = merge_lists_to_dict([1, 2, 3], ['Bob', 'Alice', 'Rob'])
print(res)
