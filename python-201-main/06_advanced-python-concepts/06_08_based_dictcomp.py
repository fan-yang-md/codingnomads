# Write a dictionary comprehension that maps each integer
# between `0` and `999` to a list of the digits that represents
# that integer in base 10. That is, your output should be:
#
# {0: [0], 1: [1], 2: [2], 3: [3], ...,
# 10: [1, 0], 11: [1, 1], 12: [1, 2], ...,
# 999: [9, 9, 9]}
#
# CHALLENGE: Write another dictionary comprehension that works the same
# but for base 2 (binary)! The output values should be:
#
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 1, 0], 3: [0, 1, 1], ...,
# 7: [1, 1, 1], 8: [1, 0, 0, 0], 9: [1, 0, 0, 1], ...,
# 999: [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]}

list_ = list(range(0,1000))
#print(list_)
complete_dict = {}

# for x in list_:
#     map = [x//100, int(x/10)%10, x%10]
#     complete_dict[x] = map

# print(complete_dict)

for x in list_:
    map_binary = [x//2**9,int(x/2)//2**8,int(x/4)//2**7,int(x/8)//2**6,int(x/16)//2**5,int(x/32)//2**4,int(x/64)//2**3,int(x/128)//2**2,int(x/256)//2,int(x/512)//2]
    complete_dict[x] = map_binary

print(complete_dict)