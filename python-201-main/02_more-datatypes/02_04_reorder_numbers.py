# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1
n = 0
even_list = []
odd_list = []

new_list = input(f'Please enter 10 numbers, separated by space between each number: ').split()

for item in new_list:
    if new_list.index(item) % 2 != 0:
        even_list.append(item)
    else:
        odd_list.append(item)

odd_list.reverse()

print(even_list + odd_list)