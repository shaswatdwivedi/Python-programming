"""
Python Complete Course for Beginners
This file contains practical implementations of all core Python concepts.
Each section is separated by comments for clarity.
"""

# ==========================================
# 1. BASIC SYNTAX & VARIABLES
# ==========================================
print("--- Section 1: Variables & Data Types ---")

# Printing to the console
print("Hello, Python Learners!")

# Variables and basic types
name = "Alice"          # String (str)
age = 25                # Integer (int)
height = 5.7            # Float (float)
is_student = True       # Boolean (bool)

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# Type Casting (Converting types)
age_str = str(age)       # int to str
height_int = int(height)  # float to int (truncates decimals)
print(f"Casted Age: {age_str}, Casted Height: {height_int}")
print("\n")


# ==========================================
# 2. OPERATORS
# ==========================================
print("--- Section 2: Operators ---")

a = 10
b = 3

# Arithmetic
print(f"Addition: {a + b}")         # 13
print(f"Division: {a / b}")         # 3.333...
print(f"Floor Division: {a // b}")   # 3 (removes decimal)
print(f"Modulo: {a % b}")            # 1 (remainder)
print(f"Exponent: {a ** b}")         # 10^3 = 1000

# Comparison & Logical
print(f"Is a greater than b? {a > b}") # True
print(f"Logical AND: {a > 5 and b < 5}") # True (both must be true)
print("\n")


# ==========================================
# 3. CONTROL FLOW (Conditionals & Loops)
# ==========================================
print("--- Section 3: Control Flow ---")

# If-Elif-Else
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# For Loop (Iterating through a range)
print("Counting 0 to 4:")
for i in range(5):
    if i == 2:
        print("Skipping 2...")
        continue  # Skip the rest of this iteration
    print(i)

# While Loop
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Blast off!")
print("\n")


# ==========================================
# 4. DATA STRUCTURES
# ==========================================
print("--- Section 4: Data Structures ---")

# Lists (Mutable, Ordered)
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Date")       # Adding item
fruits[1] = "Blueberry"     # Modifying item
print(f"List: {fruits}")

# Tuples (Immutable, Ordered)
coordinates = (10, 20)
print(f"Tuple: {coordinates}") # coordinates[0] = 15 would cause an Error

# Dictionaries (Key-Value Pairs)
user = {"name": "Bob", "age": 30, "city": "New York"}
print(f"User Name: {user['name']}")
user["email"] = "bob@example.com" # Adding new key-value pair
print(f"Updated Dict: {user}")

# Sets (Unique elements)
numbers = {1, 2, 2, 3, 4, 4}
print(f"Set (Unique): {numbers}") # Result: {1, 2, 3, 4}
print("\n")


# ==========================================
# 5. FUNCTIONS & MODULES
# ==========================================
print("--- Section 5: Functions ---")

# Defining a function with parameters and a return value
def greet(person, greeting="Hello"):
    """This function greets a person with a custom message."""
    return f"{greeting}, {person}!"

print(greet("Charlie"))              # Uses default "Hello"
print(greet("Diana", "Welcome"))     # Uses custom "Welcome"

# Lambda Function (Short, one-line function)
square = lambda x: x * x
print(f"Square of 5: {square(5)}")
print("\n")


# ==========================================
# 6. FILE HANDLING & EXCEPTIONS
# ==========================================
print("--- Section 6: Files & Exceptions ---")

# Exception Handling
try:
    result = 10 / 0 # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    print("Execution of try-except block finished.")

# File Handling (Writing and Reading)
filename = "test_file.txt"
try:
    with open(filename, "w") as f:
        f.write("Hello! This is a test file.\nWelcome to Python.")

    with open(filename, "r") as f:
        content = f.read()
        print(f"File Content:\n{content}")
except IOError as e:
    print(f"File Error: {e}")
print("\n")


# ==========================================
# 7. OBJECT-ORIENTED PROGRAMMING (OOP)
# ==========================================
print("--- Section 7: OOP ---")

class Animal:
    # Constructor
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

# Inheritance: Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Use super() to call the parent constructor
        super().__init__(name, species="Dog")
        self.breed = breed

    # Method Overriding
    def make_sound(self):
        print(f"{self.name} says: Woof! Woof!")

# Creating objects
my_dog = Dog("Buddy", "Golden Retriever")
print(f"My dog's name is {my_dog.name} and it is a {my_dog.breed}.")
my_dog.make_sound()

# --- Advanced OOP: Encapsulation ---
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (starts with __)

    def deposit(self, amount):
        self.__balance += amount
        print(f"Added {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
# print(account.__balance) # This would cause an ERROR because it's private
print(f"Account Balance: {account.get_balance()}")

print("\n")


# ==========================================
# 8. ADVANCED STRING & LIST MANIPULATION
# ==========================================
print("--- Section 8: Advanced Strings & Lists ---")

# String Slicing
text = "Python Programming"
print(f"Slice [0:6]: {text[0:6]}")    # Python
print(f"Reverse string: {text[::-1]}") # gnimmargorP nohtyP

# List Comprehensions (Powerful one-line loops)
numbers_list = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers_list if x % 2 == 0] # Square of even numbers only
print(f"Even squares: {squares}") # [4, 16]
print("\n")


# ==========================================
# 9. ITERATORS, GENERATORS & DECORATORS
# ==========================================
print("--- Section 9: Iterators, Generators & Decorators ---")

# Generator (Using yield instead of return)
def countdown_gen(n):
    while n > 0:
        yield n
        n -= 1

for val in countdown_gen(3):
    print(f"Generator value: {val}")

# Decorator (A function that wraps another function)
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
print("\n")


# ==========================================
# 10. STANDARD LIBRARY & SYSTEM
# ==========================================
print("--- Section 10: Standard Library ---")
import os
import datetime
import random

# Current Date and Time
print(f"Current Time: {datetime.datetime.now()}")

# Random number
print(f"Random number 1-100: {random.randint(1, 100)}")

# Getting current working directory
print(f"Current Directory: {os.getcwd()}")

print("\n--- Full Comprehensive Course Code Complete! ---")

