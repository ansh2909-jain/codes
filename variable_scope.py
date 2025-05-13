x = 10 # global scope

def add_numbers():
    y = 20 # local scope
    result = x + y
    print(result)

add_numbers() # 30


x = 10        # global scope

def add_numbers():
    global x
    x += 7    # access the global variable x
    print(x)

add_numbers() # 17


x = 10             # global scope

def outer_function():
    x = 20         # outer local scope
    def inner_function():
        x = 30     # inner local scope
        print(x)
    inner_function()

outer_function()   # prints 30


def outer_function():
    x = 10            # outer local scope
    def inner_function():
        nonlocal x    # access the x in outer local scope
        x = x + 10    # modify the x in outer local scope
        print(x)
    inner_function()

outer_function()      # prints 20


count = 0          # global scope

def increment_count():
    global count   # access the global variable count
    count += 1     # increment the value of count
    print(count)

# Button click event handler
def on_click():
    increment_count()


# Avoid naming collisions by using descriptive names
count = 0                 # global counter
def increment_count():    # A function that should increment the counter
    count = count + 1     # local variable with the same name
    print(count)

increment_count()         # UnboundLocalError: local variable 'count' referenced before assignment