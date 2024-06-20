from array import array

arr = array('i', [4, 19, 5, 7])
print(arr)
print(type(arr))

arr.append(15)
print(arr)
# arr.append('fgf') # error

print(arr.count(5))
arr.pop()
print(arr)
print(len(arr))

for e in arr:
    print(e)

print(arr[0])

with open('my_arr.bin', 'wb') as my_file:
    arr.tofile(my_file)

arr1 = array('i')
with open('my_arr.bin', 'rb') as my_file:
    arr1.fromfile(my_file, 3)
    print(arr1)

arr1.reverse()
print(arr1)
