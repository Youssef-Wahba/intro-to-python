##########################   DICTIONARIES   ##########################

# Dictionaries in Python are unordered collections of key-value pairs. They are similar to associative arrays or hash tables in other programming languages. Unlike sequences (such as lists or tuples) that are indexed by a range of numbers, dictionaries are indexed by keys, which can be of any immutable data type (such as strings, numbers, or tuples).

# In this dictionary, "name", "age", and "city" are keys, and "John", 30, and "New York" are their corresponding values.
my_dict = {"name": "John", "age": 30, "city": "New York"}

# You can access the values in a dictionary by referring to its key:
print(my_dict["name"])  # Output: John
print(my_dict["age"])  # Output: 30

# You can also modify the values of existing keys or add new key-value pairs:
# Modifying values
my_dict["age"] = 35
print(my_dict["age"])  # Output: 35

# Adding new key-value pairs
my_dict["gender"] = "Male"
print(
    my_dict
)  # Output: {'name': 'John', 'age': 35, 'city': 'New York', 'gender': 'Male'}

# You can iterate over the keys, values, or key-value pairs of a dictionary using a for loop:

# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)

##########################   FUNCTIONS   ##########################


# Functions in Python are reusable blocks of code that perform a specific task. They allow you to break down your program into smaller, modular pieces, making your code more organized, readable, and easier to maintain. Functions help avoid repetition of code and promote code reuse.


# Here's a basic example of defining and calling a function in Python:
def greet():
    print("Hello, world!")


# Calling the function
greet()


# Functions can also accept parameters (inputs) and return values (outputs). Here's an example:
def add(x, y):
    return x + y


# Calling the function
result = add(3, 5)
print(result)  # Output: 8


# Functions can have default parameter values:
def greet(name="World"):
    print("Hello, " + name + "!")


# Calling the function with and without arguments (positional arguments)
greet("Alice")  # Output: Hello, Alice!
greet()  # Output: Hello, World!


# Functions can also return multiple values using tuples:
def square_and_cube(x):
    return x**2, x**3


# Calling the function
square, cube = square_and_cube(2)
print("Square:", square)  # Output: 4
print("Cube:", cube)  # Output: 8


def greet2(name, age):
    print(f"Hello, {name}! You are {age} years old.")


# Calling the function with keyword arguments
greet(age=30, name="Alice")

##########################   EXCEPTION_HANDLING   ##########################


# In Python, exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions. When an error occurs, Python raises an exception, which can be caught and handled by the program.

# Attempting to divide by zero
result = 10 / 0
# When you run this code, Python will raise a ZeroDivisionError because division by zero is not allowed.

# To handle exceptions, you can use a try statement along with one or more except clauses. Here's how it works:
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Cannot divide by zero!")

# In this example, the code inside the try block is executed. If an exception occurs, Python looks for an except block with a matching exception type. If it finds one, it executes the code inside that block. If no matching except block is found, the exception is propagated up the call stack, potentially causing the program to terminate with an error message.

# You can also use the else block with a try statement to execute code if no exceptions occur:
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print("Result:", result)

# Additionally, you can use the finally block to execute cleanup code that should run regardless of whether an exception occurs:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    print("Cleanup code executed")
    
# Exceptions are a powerful mechanism in Python for handling errors and unexpected situations gracefully, allowing you to write robust and reliable code.
