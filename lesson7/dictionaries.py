# Dictionaries
# band = {
#     "vocals": "Freddie Mercury",
#     "guitar": "Brian May",
# }

# band2 = dict(
#     vocals="Freddie Mercury",
#     guitar="Brian May",
# )

# print(band)
# print(type(band2))

# # Accessing values
# print(band["vocals"])
# print(band.get("guitar"))

# # list all keys
# print(band.keys())

# # list all values
# print(band.values())

# # list of keys and values
# print(band.items())

# # verifying if a key exists
# print("vocals" in band)
# print("drums" in band)

# # changing values
# band["vocals"] = "Roger Taylor"
# band.update({"drum": "John Deacon"})

# print(band)

# # removing items
# print(band.pop("vocals"))
# print(band)

# band["cello"] = "Sara Smith" # adding new item

# print(band)

# print(band.popitem()) # removes the last item
# print(band)

# # delete or clear item
# #del band["guitar"]
# #print(band)
# band2.clear() # clears all items
# print(band2)
# del band2 # deletes the entire dictionary

# # copying dictionaries
# # band3 = band # this creates a reference to the original dictionary
# # print("Bad Copy!")
# # print(band3)
# # print(band)
# # band3["trumpet"] = "John Doe" # this will also change the original dictionary
# # print(band)

# band3 = band.copy() # this creates a new copy of the dictionary
# print("Good Copy!")
# band3["trumpet"] = "John Doe" # this will also change the original dictionary
# print(band3)
# print(band) 

# # use a constructor function to copy a dictionary
# band2 = dict(band)
# print('Good copy with constructor')
# print (band2)
# print(band)

# Nested dictionaries
member1 = {
    "name": "Freddie Mercury",
    "instrument": "vocals",
    "age": 45,
}

member2 = {
    "name": "Brian May",
    "instrument": "guitar",
    "age": 50,
}

band = {
    "member1": member1,
    "member2": member2,
}

print(band["member1"]["age"])

# Sets
# A set is a collection of unique items
# A set is unordered, unindexed, and unchangeable
# A set can be created using curly braces or the set() constructor

num1 = {1, 2, 3, 3, 4, 5}
num2 = set([1, True, 2, False, 3, 4, 0])

print(num1)
print(num2) 
print(type(num1))

print(2 in num1) # check if 2 is in the set

# you cannot use indexing with sets
# print(num1[0]) # this will raise an error

# adding items to a set
num1.add(6)
print(num1)

# add elements from another set
morenum = {7, 8, 9}
num1.update(morenum)
print(num1)

# you can use update wit lists, tuples, and dictionaries

# merge two sets
one = {1, 2, 3}
two = {4, 5, 6}
three = one.union(two)
print(three)

# keep only the duplicates
one = {1, 2, 3}
two = {4, 1, 6}

one.intersection_update(two) # this will keep only the duplicates
print(one)

# all except the duplicates
one = {1, 2, 3}
two = {4, 1, 6} 

one.symmetric_difference_update(two) # this will keep all except the duplicates
print(one)