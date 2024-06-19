import time

print(time)

print(time.time())

start_time = time.time()
print(time.ctime(1718783223))

time.sleep(2.5)  # delay code on 2.5 seconds

# print(time.time())
end_time = time.time()
print(end_time - start_time)
