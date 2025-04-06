#### Control Modules & Functions

# Function to greet a user
def greet(name):
    print(f"Hello, {name}!")

# Main control
def main():
    user_name = input("Enter your name: ")
    greet(user_name)

if __name__ == '__main__':
    main()



##### Exception Handling

# Try-except block to handle division by zero
def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# Example usage
divide(10, 2)
divide(10, 0)


##### File Handling

# Write to a file and then read it
file_name = "example.txt"

# Writing
with open(file_name, 'w') as file:
    file.write("This is a sample file.\nPython is awesome!")

# Reading
with open(file_name, 'r') as file:
    content = file.read()
    print("File Content:\n", content)



##### Math, DateTime, and Calendar

import math
from datetime import datetime
import calendar

# Math Example
print("Square root of 16 is:", math.sqrt(16))

# DateTime Example
now = datetime.now()
print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Calendar Example
print("\nCalendar for April 2025:")
print(calendar.month(2025, 4))

