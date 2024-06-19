import csv

# with open('test.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['user_id', 'user_name', 'comments_qty'])  # we can pass string, but usually we pass lists
#     writer.writerow([52, 'bob', 12121])
#     writer.writerow([51, 'mike', 121])
#     writer.writerow([50, 'alice', 21])

# with open('test.csv') as csv_file:
#     reader = csv.reader(csv_file)
#     print(reader)
#     print(type(reader))
#     # csv_list = list(reader)
#     # print(
#     #     csv_list)  # [['user_id', 'user_name', 'comments_qty'], ['52', 'bob', '12121'], ['51', 'mike', '121'], ['50', 'alice', '21']]
#     for line in reader:  # loop is possible only one time
#         print(line)
#     print(reader.line_num) # loop is possible only one time


with open('test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(['user_id', 'user_name', 'comments_qty'])  # we can pass string, but usually we pass lists
    writer.writerow([52, 'bob', 12121])
    writer.writerow([51, 'mike', 121])
    writer.writerow([50, 'alice', 21])

with open('test.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for line in reader:
        print(line)
    print(reader.line_num)  # 4
