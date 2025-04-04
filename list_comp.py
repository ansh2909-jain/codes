# Squares of even numbers from 0 to 9
squares = [x**2 for x in range(12) if x % 2 == 0]
print(squares)  

#Even Numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Stripping Whitespace from a List of Strings

raw = ['  apple ', ' banana', 'cherry  ']
clean = [s.strip() for s in raw]
print(clean)

#Repeat Characters

letters = ['a', 'b', 'c']
repeated = [char * 3 for char in letters]
print(repeated)

#Convert to Uppercase

words = ['hello', 'world']
upper = [w.upper() for w in words]
print(upper)

#Advanced & Creative Examples
#Flatten a 2D List (Matrix)

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)

# Conditional Transformation

nums = [1, 2, 3, 4, 5]
new = [x if x % 2 == 0 else x*10 for x in nums]
print(new)

#Extract Digits from a String

text = "a1b2c3d4"
digits = [int(ch) for ch in text if ch.isdigit()]
print(digits)

#Get Words Longer Than 3 Letters

sentence = "The fox jumps over the lazy dog"
long_words = [word for word in sentence.split() if len(word) > 3]
print(long_words)

#Reverse Each Word in a List

words = ['hello', 'world', 'python']
reversed_words = [word[::-1] for word in words]
print(reversed_words)
