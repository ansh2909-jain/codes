################################################### Enumerate #############################################

fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(i, fruit)

# Will print:
# 0 apple
# 1 banana
# 2 cherry


fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits, 1):
    print(i, fruit)

# Will print:
# 1 apple
# 2 banana
# 3 cherry


################################################### ZIP ####################################################

fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'red']
for fruit, color in zip(fruits, colors):
    print(fruit, color)

# Will print:
# apple red
# banana yellow
# cherry red


fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow']
for fruit, color in zip(fruits, colors):
    print(fruit, color)

# Output:
# apple red
# banana yellow
