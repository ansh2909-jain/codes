def area(length, width = 1):
    return length * width

print(area(5))     # 5
print(area(5, 10)) # 50

"""
def sum_numbers(a=1, b):
    return a + b
"""

def sum_numbers(b, a=1):
    return a + b


def greeting(name, title='Mr.'):
    return f'Hello, {title} {name}'

print(greeting('John'))         # Hello, Mr. John
print(greeting('Jack', 'Dr.'))  # Hello, Dr. Jack


def sum_numbers(a, b):
    return a + b

print(sum_numbers(1, 2)) # 3
print(sum_numbers(2, 1)) # 3


def greeting(name, title='Mr.'):
    return f"Hello, {title} {name}"

print(greeting(name='John'))               # Hello, Mr. John
print(greeting(name='John', title='Dr.'))  # Hello, Dr. John


def create_person(first_name, last_name, age=18, city='London', country='UK'):
    return {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'city': city,
        'country': country
    }

person = create_person('John', 'Doe', city='New York', country='USA')
print(person)
# {'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'city': 'New York', 'country': 'USA'}

print(create_person(first_name='Anna', last_name='Brown'))
# {'first_name': 'Anna', 'last_name': 'Brown', 'age': 18, 'city': 'London', 'country': 'UK'}

"""
def function_name(*args):
    # function body
"""

def add(*args):
    res = 0
    for number in args:
        res += number
    return res
print(add(1, 2, 3, 4, 5)) # 15

"""
def function_name(**kwargs):
    # function body
"""

def product(**kwargs):
    result = 1
    for key, value in kwargs.items():
        result *= value
    return result
print(product(a = 2, b = 3, c = 4))   # 24


def add_number(number, numbers=[]):
    numbers.append(number)
    return numbers

print(add_number(1)) # [1]
print(add_number(2)) # [1, 2]


def add_number(number, numbers=None):
    if numbers is None:
        numbers = []
    numbers.append(number)
    return numbers

print(add_number(1)) # [1]
print(add_number(2)) # [2]


"""def greeting(name, title='Mr.'):
    return f'Hello, {title} {name}'
print(greeting('John', title='Dr.'))   # Hello, Dr. John
print(greeting(title='Dr.','John'))   # SyntaxError: positional argument follows keyword argument"""