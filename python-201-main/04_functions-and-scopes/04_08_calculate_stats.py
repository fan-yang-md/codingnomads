# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list):
  # define the function here
  sum = 0
  maximum = list[0]
  minimum = list[0]
  for number in list:
    sum += number
    if number > maximum:
      maximum = number
    elif number < minimum:
      minimum = number
    average = sum / len(list)
  return(sum,maximum,minimum,average)
# call the function below here
# 
results = stats(example_list)
print(f'Sum: {results[0]} \nMaximum: {results[1]} \nMinimum: {results[2]} \nAverage: {results[3]}')
