def sum_nums(*args):
    print(args)  # (2,3,7)
    print(type(args))  # tuple class
    # print(args[0])  # 2
    return sum(args)


print(sum_nums(2, 3, 7))


def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info


print(get_posts_info("Bob", 10))

print(get_posts_info(posts_qty=10, name="Bob"))  # порядок аргументів в такому випадку не важливий


def get_posts_info1(**person):
    print(person)  # { 'name': 'Bob'. 'posts_qty': 25 }
    print(type(person))
    info = (
        f"{person['name']} wrote "
        f"{person['posts_qty']} posts"
    )  # not tuple - hack to join string, to avoid long string in the code
    return info


print(get_posts_info1(name='Bob', posts_qty=25))
# print(get_posts_info1(name='Bob', 25)) # error - do not pass position args when using ** operator
