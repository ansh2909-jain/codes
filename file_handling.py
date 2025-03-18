file = open("requirements.txt", "r")

###############################################################################

file = open("requirements.txt", "w")
file.write("Hello, World!")  # Write a string to the file

# Write multiple lines
lines = ["First line\n", "Second line\n", "Third line\n"]
file.writelines(lines)

###############################################################################

file.close()

###############################################################################

with open("requirements.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed after the block.

###############################################################################

# Appending text to the file
with open("sample.txt", "a") as file:
    file.write("This is an appended line.\n")

# Reading the file again
with open("requirements.txt", "r") as file:
    print(file.read())

###############################################################################