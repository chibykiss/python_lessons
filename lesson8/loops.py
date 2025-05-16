# while loops

value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         continue
#     value += 1   
# The above code will result in an infinite loop because the value is not being incremented before the continue statement.
# To fix this, we need to increment the value before the continue statement.

while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)    

# for loops
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(name)
   
for x in names:
    if x == 'Bob':
        break
    print(x)

for x in names:
    if x == 'Bob':
        continue
    print(x)

# for loop with range
for x in range(4):
    print(x)

for x in range(2,4):
    print(x)

for x in range(5,101,5):
    print(x)
else:
    print("Loop completed")

names = ['Alice', 'Bob', 'Charlie']
actions = ['eat', 'sleep', 'code']

for name in names:
    for action in actions:
        print(f"{name} will {action}")

for action in actions:
    for name in names:
        print(f"{name} will {action}")
   

    