my_fruits = ["apple", "banana", "lime"]

posts_ids = [151, 245, 762, 167]

user_inputs = [True, "hi!", 10.5, '⚜️']

happy_smiles = []
happy_smiles.append('⚜️')  # adds the element to the end
print(happy_smiles)

user_inputs.pop()  # removes the last element and returns the deleting element
print(user_inputs)

my_fruits.pop(1)  # removes the element with index 1
print(my_fruits)

posts_ids.sort()
print(posts_ids)
posts_ids.sort(reverse=True)
print(posts_ids)

greeting = "Hello from Python"
greeeting_letters = list(greeting)
print(greeeting_letters)

my_dict = {"a": 10, 'b': True}
my_dict_keys = list(my_dict)  # list of keys
print(my_dict_keys)

ratings = [2.5, 5.0, 4.3, 3.7]
print(min(ratings))
print(max(ratings))
print(sum(ratings))

mt_ratings = [2.5, 5.0]
other_ratings = [3.7, 4.5, 4.9]
all_ratings = mt_ratings + other_ratings  # creates the single merged list including two lists
print(all_ratings)

ratings2 = [2.5, 5.0, 4.3, 3.7, 4.5]
first_two_ratings = ratings2[:2]  # sublist [2.5,5.0]
print(first_two_ratings)
print(ratings2[1:-1])  # [5.0, 4.3, 3.7]
print(ratings2[-2:])  # [3.7,4.5]
