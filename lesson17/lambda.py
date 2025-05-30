squared = lambda num: num * num

print(squared(10))

numbers = [3,7,12,18,20,21]

squared_nums = map(lambda num: num * num,numbers)

print(list(squared_nums))

############################################
# High Order Functions
odd_nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_nums))

###########################################

from functools import reduce

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr,numbers,10)

print(total)

print(sum(numbers,10))

names = ['Dave Gray', 'sera lancaster', 'Ezuma Emmanuel']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(f"character length: {char_count}")