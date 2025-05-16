def add_one(num):
    if (num >= 9):
        return num + 1
    
    total = num + 1
    print(total)

    # Recursive call
    return add_one(total)

# Test the function
#add_one(0)
# result = add_one(0)
# print(result)

# use a loop to get the same result

def add_one_loop(num):
    while (num < 9):
        num += 1
        print(num)
    else:
        num += 1
        print(num)


# Test the function
add_one_loop(0)