# Print out every prime number between 1 and 1000.

list = []

for num in range(1,1001):
    count = 0
    for divisor in range(2,num):
        if num%divisor == 0:
            count += 1
    if count == 0:
        list.append(num)

print(list)