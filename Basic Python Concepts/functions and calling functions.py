# Part 1: Using Dictionaries
def dictionary_demo():
    # Creating a dictionary with some key-value pairs
    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    
    # Accessing values using keys
    print("Name:", person["name"])
    print("Age:", person["age"])
    print("City:", person["city"])

# Part 2: Using Error Handling (try, except)
def error_handling_demo():
    try:
        # Trying to divide by zero
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: You can't divide by zero!")
    else:
        print(f"Result: {result}")
    finally:
        print("Error handling finished.")

# Part 3: Using Imports
import math  # Importing the math module to use mathematical functions

def import_demo():
    # Using the math module to calculate the square root of a number
    number = 16
    sqrt_value = math.sqrt(number)
    print(f"The square root of {number} is {sqrt_value}")

# Calling all functions
dictionary_demo()
error_handling_demo()
import_demo()