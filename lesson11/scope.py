name = "Vibe"
count = 1

def greet():
    color = "blue"
    global count
    count += 2
    print(count)
    def inner_greet(name):
        # change the color vaiarable to red
        nonlocal color
        color = "red"
        print(f"Hello {name}, my favorite color is {color}\n")

    inner_greet(name)
    print(color)
greet()