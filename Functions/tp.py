import random
count = 0
while True:
    i1 = random.uniform(1.00000000000,1.00000000001)
    i2 = random.uniform(1.00000000000,1.00000000001)
    if i1 == i2:
        False
    count += 1
    print(i1,i2)
print(count)
