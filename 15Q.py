#Question - 1 (Equilibrium Index)

def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0  
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        
        if left_sum == right_sum:
            return i 
        left_sum += arr[i]
    return -1  
arr = [4, 2, 5, 1, 2, 3]
result = find_equilibrium_index(arr)
print(f"The equilibrium index is: {result}")

#Question - 2 (Group Anagrams)

from collections import defaultdict
def find_set(a):
    anagram_groups = defaultdict(list)
    
    for word in a:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)
    result = [set(group) for group in anagram_groups.values()]
    return result

words = ['cat', 'dog', 'god', 'cat', 'tac']
print(find_set(words))

#Question - 3 (Find First And Last Index)

def find_first_and_last(arr, X):
    
    def find_first(arr, X):
        left, right = 0, len(arr) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == X:
                first = mid
                right = mid - 1 
            elif arr[mid] < X:
                left = mid + 1
            else:
                right = mid - 1
        return first
    
    def find_last(arr, X):
        left, right = 0, len(arr) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == X:
                last = mid
                left = mid + 1 
            elif arr[mid] < X:
                left = mid + 1
            else:
                right = mid - 1
        return last
    first = find_first(arr, X)
    last = find_last(arr, X)
    return (first, last)

arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
X = 5
first, last = find_first_and_last(arr, X)
print(f"First occurrence of {X} is at index {first}")
print(f"Last occurrence of {X} is at index {last}")

#Question - 4 (Count Element Occurring Once Once (Eg :- aaabbbc))

from collections import Counter
string = "aaabbbc"
counter = Counter(string)
for char, count in counter.items():
    print(f"Character '{char}' occurs {count} times.")

#Question - 5 (Palindrome (String Recursive))

def is_palindrome(s):
    if len(s) <=1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
s = "racecar"
print(f"Is '{s}' a palindrome: {is_palindrome(s)}")

s = "hello"
print(f"Is '{s}' a palindrome: {is_palindrome(s)}")

#Question - 6 (Palindrome (String Recursive)(Using A Flag = 0))

def is_palindrome(s, flag=0):
    if len(s) <= 1:
        return flag == 0
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1], flag)

s = "anmolomna"
print(f"Is '{s}' a palindrome: {is_palindrome(s)}")

s = "jainanmol"
print(f"Is '{s}' a palindrome: {is_palindrome(s)}")

#Question - 7 (Sum Of Digits)

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

number =123456789
print(f"The sum of digits of {number} is {sum_of_digits(number)}")

#Question - 8 (Factorial Iterative)

def factorial_iterative(n):
    result = 1
    for i in range (1, n + 1):
        result *= i
    return result

number = 6
print(f"The factorial of {number} is {factorial_iterative(number)}")

#Question - 9 (Factorial Recursive)

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

number = 7
print(f"The factorial of {number} is {factorial_recursive(number)}")

#Question - 10 (Isograms)

def is_isogram(s):
    s = s.lower()
    return len(s) == len(set(s))

word ="abcdef"
print(f"Is '{word}' an isogram: {is_isogram(word)}")

word = "hello"
print(f"Is '{word}' an isogram: {is_isogram(word)}")

#Question - 11 (Anagrams)

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if are_anagrams(str1, str2):
    print(f'"{str1}" and "{str2}" are anagrams.')
else:
    print(f'"{str1}" and "{str2}" are not anagrams.')

#Question - 12 (Binary Search For Sorted List Array)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
target = 19
result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the list")

#Question - 13 (Binary Search Sorted (Bubble Sort))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2 
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1  
    return -1

arr = [64, 34, 25, 12, 22, 11, 90]
target = 34
bubble_sort(arr)
print("Sorted Array:", arr)
result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the list")

#Question - 14 (Binary Search Iterative)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2 
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  

arr = [1, 3, 5, 7, 9, 11, 13]  
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the list")

#Question -15