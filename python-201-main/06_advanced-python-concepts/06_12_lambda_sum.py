# Write a lambda expression that takes in three numbers
# and returns the sum of the numbers.
list_ = input('Give me 3 numbers, separated by space: ').split()
print(list_)
sum_fxn = lambda x: sum(int(i) for i in x)

print(sum_fxn(list_))