def hello_world():
    print("Hello, World!")
    return "Hello, World!"

hello_world()

# functions with parameters
def sum_numbers(num1, num2):
    print(num1 + num2)

def sum_numbers(num1=0, num2 = 0):
    if(type(num1) is not int or type(num2) is not int):
       return 0
    return num1 + num2

total = sum_numbers(7,3)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))


def multiple_items2(**kwargs):
    print(kwargs)
    print(type(kwargs))

multiple_items2(first="John", last="Doe", age=30)