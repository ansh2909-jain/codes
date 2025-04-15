#Mapping Numbers to Their Squares

squares = {x: x**2 for x in range(6)}
print(squares)

# Use for loop

squares = {}
for x in range(6):
    squares[x] = x ** 2
print(squares)

# Filtering Items

prices = {'apple': 100, 'banana': 50, 'cherry': 75}
expensive = {k: v for k, v in prices.items() if v > 60}
print(expensive)

# Use for loop 

prices = {'apple': 100, 'banana': 50, 'cherry': 75}
expensive = {}
for k, v in prices.items():
    if v > 60:
        expensive[k] = v
print(expensive)

# Swapping Keys and Values

original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)

# Use for loop

original = {'a': 1, 'b': 2, 'c': 3}
swapped = {}
for k, v in original.items():
    swapped[v] = k
print(swapped)

# Using a List of Tuples

pairs = [('x', 1), ('y', 2), ('z', 3)]
d = {key: value for key, value in pairs}
print(d)

# Use for loop

pairs = [('x', 1), ('y', 2), ('z', 3)]
d = {}
for key, value in pairs:
    d[key] = value
print(d)

# Nested Dictionary Comprehension
# Creating a multiplication table (up to 3x3)
table = {i: {j: i*j for j in range(1, 4)} for i in range(1, 4)}
print(table)

# Use for loop
table = {}
for i in range(1, 4):
    table[i] = {}
    for j in range(1, 4):
        table[i][j] = i * j
print(table)

#
text = "hello world"
freq = {char: text.count(char) for char in text if char != ' '}
print(freq)

# Use for loop

text = "hello world"
freq = {}
for char in text:
    if char != ' ':
        freq[char] = text.count(char)
print(freq)

#
celsius = {'day1': 20, 'day2': 25, 'day3': 30}
fahrenheit = {day: (temp * 9/5) + 32 for day, temp in celsius.items()}
print(fahrenheit)

# Use for loop

celsius = {'day1': 20, 'day2': 25, 'day3': 35}
fahrenheit = {}
for day, temp in celsius.items():
    fahrenheit[day] = (temp * 9/5) + 32
print(fahrenheit)

#
items = [('a', 1), ('b', 2), ('a', 3), ('c', 4)]
cleaned = {k: v for k, v in items}
print(cleaned)

# Use for loop

items = [('a', 1), ('b', 2), ('a', 3), ('c', 4)]
cleaned = {}
for k, v in items:
    cleaned[k] = v
print(cleaned)

#
labels = {x: ('even' if x % 2 == 0 else 'odd') for x in range(1, 6)}
print(labels)

# Use for loop

labels = {}
for x in range(1, 6):
    labels[x] = 'even' if x % 2 == 0 else 'odd'
print(labels)

#
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
person = {k: v for k, v in zip(keys, values)}
print(person)

# Use for loop

keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
person = {}
for k, v in zip(keys, values):
    person[k] = v
print(person)