import time

start_time = time.time()
range1 = range(100000)
print(range1[1000])
# l1 = list(range(100000))
# print(l1[1000])
end_time = time.time()

print(end_time - start_time)
