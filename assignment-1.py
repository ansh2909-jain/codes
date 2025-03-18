# Question - 2

def factorial_and_count_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

num = int(input("Enter a number: "))
print(f"No of zeros in {num} is {factorial_and_count_zeros(num)}")

# Question - 6

def count_the_no_of_vowels_consonants(input_string):
    vowels = "aeiouAEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    
    vowel_count = 0
    consonant_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    
    return vowel_count, consonant_count
input_user = input("Enter a string: ")
vowels, consonants = count_the_no_of_vowels_consonants(input_user)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")


#Question -1

def calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")
result = calculator(num1, num2, operation)
print(f"The result of {operation} between {num1} and {num2} is: {result}")