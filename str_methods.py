a="Hello Anmol"                                                 
print(a)                                                        #Sample string

print("Uppercase:", a.upper())                                  #Uppercase                             

print("Lowercase:", a.lower())                                  #Lowercase

print("Title Case:", a.title())                                 #Title

print("Capitalize:", a.capitalize())                            #Capitalize

print("Replace 'Hello' with 'Hi':", a.replace("Hello", "Hi"))   #Replace Hello with Hi

print("Count 'o':", a.count('o'))                               #Count

print("Find 'Anmol':", a.find('Anmol'))                         #Find the index of a substring

print("Starts with 'Hello':", a.startswith('Hello'))            #Check if the string starts with a specific substring

print("Ends with 'Anmol':", a.endswith('Anmol'))                #Check if the string ends with a specific substring

print("Split by space:", a.split())                             #Split the string into a list

words = ['Hello', 'Anmol', 'Jain']
print("Join words:", ' '.join(words))                           #Join list elements into a string

str_with_spaces = "   Hello, Anmol   "
print("Strip spaces:", str_with_spaces.strip())                 #Strip leading/trailing whitespace

alphanumeric = "Anmol14"
print("Is alphanumeric:", alphanumeric.isalnum())               #Check if all characters are alphanumeric

alphabetic = "Anmol"
print("Is alphabetic:", alphabetic.isalpha())                   #Check if all characters are alphabetic

digit_string = "142002"
print("Is digit:", digit_string.isdigit())                      #Check if all characters are digits

whitespace_string = "   "
print("Is whitespace:", whitespace_string.isspace())            #Check if the string contains only whitespace

reversed_text = a[::-1]
print("Reversed:", reversed_text)                               #Reverse a string (by slicing)