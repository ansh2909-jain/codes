def get_user_data():
    return 'Anna', 23, 'anna123'


name, age, id = get_user_data()
print('Got the user data:', name, age, id)
# Got the user data: Anna 23 anna123

def get_user_data():
    return 'Anna', 23, 'anna123'

res = get_user_data()     # Store the returned value in a single variable
print(res)                # ('Anna', 23, 'anna123')
print(type(res))          # <class 'tuple'>

name, age, id = res       # Unpack the tuple
print('Got the user data:', name, age, id)
# Got the user data: Anna 23 anna123


res = 'Anna', 23, 'anna123'   # Which is an alternative of ('Anna', 23, 'anna123')
print(res)                    # ('Anna', 23, 'anna123')
print(type(res))              # <class 'tuple'>

# Unpack the tuple:
name, age, id = res
print('Got the user data:', name, age, id)
# Got the user data: Anna 23 anna123

# Which is exactly the same as:
name, age, id = 'Anna', 23, 'anna123'
print('Got the user data:', name, age, id)
# Got the user data: Anna 23 anna123


def get_numbers_list():
    return [3, 4]

[a, b] = get_numbers_list()
print(a) # 3
print(b) # 4

def get_numbers_dict():
    return {'a':3, 'b':4}

numbers = get_numbers_dict()
print(numbers['a']) # 3
print(numbers['b']) # 4


# Return a list
def get_numbers_list():
    return [3, 4]

[a, b] = get_numbers_list()
print(a) # 3
print(b) # 4


# Return multiple values
def get_numbers_list():
    return 3, 4

a, b = get_numbers_list()
print(a) # 3
print(b) # 4


# Return a tuple
def get_numbers_list():
    return (3, 4)

a, b = get_numbers_list()
print(a) # 3
print(b) # 4


# Wrap a and b in a tuple
def get_numbers_list():
    return 3, 4

(a, b) = get_numbers_list()
print(a) # 3
print(b) # 4