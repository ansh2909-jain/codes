a = [1, 2, 3, 4 ]                                               # Add 5 to the end of the list
a.append(5)
print(a)

a = [1, 2, 3, 4]                                                   # Create a copy of the list
b = a.copy()
print(b)

a = [1, 2, 3, 4]                                                   # Remove all elements from the list
a.clear()
print(a)

a = [1, 2, 3, 4, 3]                                                # Count occurrences of 3 in the list
print(a.count(3))

a = [1, 2]                                                      # Extend list a by adding elements from list [3, 4, 5]
a.extend([3, 4, 5])
print(a)

a = [1, 2, 3, 4]                                                # Find the index of 4 in the list
print(a.index(4))

a = [1, 3, 4]                                                      # Insert 2 at index 1
a.insert(1, 2)
print(a)

a = [1, 2, 3, 4]                                                   # Remove and return the last element in the list
a.pop()
print(a)

a = [1, 2, 3, 4]                                                   # Remove the first occurrence of 3
a.remove(3)
print(a)

a = [1, 2, 3, 4]                                                   # Reverse the list order
a.reverse()
print(a)

a = [4, 3, 1, 2]                                                   # Sort the list in ascending order
a.sort()
print(a)