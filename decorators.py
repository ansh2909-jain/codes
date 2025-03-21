# Simple Decorators

def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

# Apply decorator
@decorator_function
def display():
    print("Display function executed.")

display()

# Decorator with Arguments

def decorator_with_args(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Function {original_function.__name__} is being called with arguments: {args} and kwargs: {kwargs}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_with_args
def greet(name, age):
    print(f"Hello {name}, You are {age} years old.")
greet("Anmol", 23)

# Chaining Decorators

def decorator_one(func):
    def wrapper():
        print("Decorator One")
        return func()
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator Two")
        return func()
    return wrapper

@decorator_one
@decorator_two
def say_Hi():
    print("Hi!")
say_Hi()