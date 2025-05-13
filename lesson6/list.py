#list holds multiple data values of differnent types
users = ['Emmauel', 'John', 'Mary', 'Paul', 'Peter']

data = ['frank', 23, 45.6, True, 'John', 'Mary', 'Paul', 'Peter']

empty_list = []

print("John" in data)

# print(users[0])
# print(users[-2])
# print(users.index('Mary'))
# print(users[0:2])
# print(users[1:])

data.append('40')

#data += ['2023-10-01', '2023-10-02', '2023-10-03']

#data.extend(['2023-10-01', '2023-10-02', '2023-10-03'])

#data.extend(users)

users.insert(0, 'Fresh')

users[2:2] = ['Frank', 'alex']

users[1:3] = ['linda', 'Mathew']

# users.remove('Fresh')

# users.pop()
users.sort(key=str.lower)
# del users[0]

print(users)

#delete data
#del data

#empty the list
#data.clear()

#print(data)

print(len(users))

nums = [4, 2, 5, 1, 3]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

# print(sorted(nums, reverse=True))

# print(nums)

# numscopy = nums.copy()
# mynums = list(nums)
# mycopy = nums[:]

# print(numscopy)
# print(mynums)
# print(nums)

# print(type(users))

# myList = list(['Hello'])                                                                                                                                                                                                    
# print(myList)

#Tuples
mytuple = ('dave', 22, 'mike', False)

newlist = list(mytuple)
newlist.append('Nail')
newtuple = tuple(newlist)
print(newtuple)

print(type(mytuple))

(one, *two, three) = mytuple
print(one, two, three)