# Squares of even numbers from 0 to 9
squares = [x**2 for x in range(12) if x % 2 == 0]
print(squares)  

# Use for loop

squares = []
for x in range(12):
    if x % 2 == 0:
        squares.append(x**2)
print(squares)

#Even Numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Use for loop

evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)
print(evens)

# Stripping Whitespace from a List of Strings

raw = ['  apple ', ' banana', 'cherry  ']
clean = [s.strip() for s in raw]
print(clean)

# Use for loop

raw = ['  apple ', ' banana', 'cherry  ']
clean = []
for s in raw:
    clean.append(s.strip())
print(clean)

#Repeat Characters

letters = ['a', 'b', 'c']
repeated = [char * 3 for char in letters]
print(repeated)

# Use for loop

letters = ['a', 'b', 'c']
repeated = []
for char in letters:
    repeated.append(char * 3)
print(repeated)

#Convert to Uppercase

words = ['hello', 'world']
upper = [w.upper() for w in words]
print(upper)

# Use for loop

words = ['hello', 'world']
upper = []
for w in words:
    upper.append(w.upper())
print(upper)

#Advanced & Creative Examples
#Flatten a 2D List (Matrix)

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)

# Use for loop

matrix = [[1, 2], [3, 4], [5, 6]]
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
print(flat)

# Conditional Transformation

nums = [1, 2, 3, 4, 5]
new = [x if x % 2 == 0 else x*10 for x in nums]
print(new)

# Use for loop

nums = [1, 2, 3, 4, 5]
new = []
for x in nums:
    if x % 2 == 0:
        new.append(x)
    else:
        new.append(x * 10)
print(new)

#Extract Digits from a String

text = "a1b2c3d4"
digits = [int(ch) for ch in text if ch.isdigit()]
print(digits)

# Use for loop

text = "a1b2c3d4"
digits = []
for ch in text:
    if ch.isdigit():
        digits.append(int(ch))
print(digits)

#Get Words Longer Than 3 Letters

sentence = "The fox jumps over the lazy dog"
long_words = [word for word in sentence.split() if len(word) > 3]
print(long_words)

# Use for loop

sentence = "The fox jumps over the lazy dog"
long_words = []
for word in sentence.split():
    if len(word) > 3:
        long_words.append(word)
print(long_words)

#Reverse Each Word in a List

words = ['hello', 'world', 'python']
reversed_words = [word[::-1] for word in words]
print(reversed_words)

# Use for loop

words = ['hello', 'world', 'python']
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])
print(reversed_words)