# Lambda function to add two numbers
add = lambda x, y: x + y
print(add(4, 7))

# Using lambda with map

numbers = [1, 5, 9, 13, 17]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Using lambda with filter
numbers_1 = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_1))
print(even_numbers) 