# Basic Try-Except Block

try:
    # Code that might raise an exception
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")

# Try-Except-Else-Finally

try:
    x = 20 / 2
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
else:
    print("No errors! The division was successful.")
finally:
    print("This block will always execute.")

# Custom Exceptions

class NegativeValueError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_value(value):
    if value < 0:
        raise NegativeValueError("Value cannot be negative!")

try:
    check_value(-10)
except NegativeValueError as e:
    print(f"Custom Error: {e}")