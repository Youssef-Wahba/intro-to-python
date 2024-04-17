##########################  INTRODUCTION   ##########################

# Python is a 'high level language' that is more easier for developers to
# deal with rather than 'low level languages' that are more complex

# Complier vs Interpreter
# 'Compiler' take the whole code and compile it to an executable to deal with
# machine code (0s and 1s) e.g. Java and C++
# 'Interpreter' interprets the code line by line and convert it to
# machine code e.g. python and Javascript

# strictly (strongly) typed languages put restrictions on variables to be
# on specific types rather than loosly typed languages which put no restrictions

# installation:
# Vs code: https://code.visualstudio.com/docs/languages/python
# Pycharm: https://www.jetbrains.com/guide/python/tutorials/getting-started-pycharm/installation-and-setup/

##########################  VARIABLES   ##########################

# It's a storage location in memmory with an associated symbolic name (an identifier)

# declaration vs assignment vs initialization
# Declaration: In Python, you don't explicitly declare variables before using them
# **Declaration doesn't happen explicitly, it's done implicitly by assignment
# Assignment: Assigning a value to a variable means giving it a specific data or object to hold
# Initialization: Initialization refers to the act of giving an initial value to a variable at the time of its creation. It's the process of assigning the first value to a variable.

# Assignment and Initialization
x = 10  # Assigning the value 10 to the variable x, initializing it

# Reassignment
x = 20  # Reassigning the value of x to 20

# Variables can be reassigned to different types
x = "Hello"  # Now x is a string

# Multiple assignment / Multi-initialization
x, y = 10, 20

# Swapping the values of x and y
x, y = y, x

# Camel case vs Pascal case vs Snake case
# Camel case is a convention where multiple words are joined together, and each word (except the first one) begins with a capital letter.
# Example: camelCaseExample, numberOfStudents, totalSalesAmount

# Pascal case is similar to camel case, but it starts with a capital letter, including the first word.
# Example: PascalCaseExample, NumberOfStudents, TotalSalesAmount

# Snake Case:
# Snake case is a convention where words are separated by underscores (_), and all letters are usually lowercase.
# Example: snake_case_example, number_of_students, total_sales_amount

# It's essential to follow the conventions of the language or project you're working with for consistency and readability.

# Python commonly uses snake case for variable and function names, while languages like Java and C# often use camel case or pascal case.

# variables in python are case-sensitive
# Variables with different cases
myVariable = 10
MyVariable = 20
myvariable = 30

# Output each variable
print(myVariable)  # Outputs: 10
print(MyVariable)  # Outputs: 20
print(myvariable)  # Outputs: 30

# They are all different variables

##########################  DATA_TYPES   ##########################

# Integer (int): Whole numbers without decimal points.
x = 10

# Float (float): Numbers that have decimal points.
pi = 3.14

# String (str): Sequence of characters, enclosed in single, double, or triple quotes.
name = 'Alice'
name = "Alice"
name = '''Alice'''
name = """Alice"""

# Boolean (bool): Represents truth values, either True or False.
is_student = True

# NoneType (None): Represents the absence of a value.
empty_variable = None


# In Python, the type() function is used to get the type of an object. It returns the type object of the argument passed to it. Here's how you can use it:
print(type(5))  # Output: <class 'int'>
print(type(3.14))  # Output: <class 'float'>
print(type("Hello"))  # Output: <class 'str'>
print(type(True))  # Output: <class 'bool'>
print(type(None))  # Output: <class 'NoneType'>

# type casting / conversion
# Integer Conversion: Converts a value to an integer.
x = int(3.14)  # x will be 3

# Float Conversion: Converts a value to a float.
y = float("5.7")  # y will be 5.7
# String Conversion: Converts a value to a string.
z = str(10)  # z will be "10"

# Boolean Conversion: Converts a value to a boolean.
a = bool(0)  # a will be False
b = bool(10)  # b will be True

# Explicit Conversion: Converting between incompatible types may result in errors or loss of data. You can explicitly convert a value to another type if the conversion is valid.
x = "10"
y = int(x)  # y will be 10

##########################  DEALING_WITH_STRINGS   ##########################

# String slicing in Python allows you to extract substrings from a string by specifying a start and end index. It's done using square brackets [] with the syntax [start_index:end_index:step]. Here's how it works:

# Example string
text = "Hello, World!"

print(text[0:5])  # Output: Hello
print(text[7:12])  # Output: World
print(text[:5])  # Output: Hello (start_index defaults to 0)
print(text[7:])  # Output: World! (end_index defaults to the end of the string)
print(text[-5:-1])  # Output: orld (from fifth character from the end to second-to-last)
print(text[::2])  # Output: Hlo ol! (step by 2)
print(text[::-1])  # Output: !dlroW ,olleH (reverse the string)

# function vs method
# Function: It is not associated with any particular object or class.
# Method is a function that is associated with an object or a class. It defines the behavior of objects in a class.

# Some string methods

# str.upper(): Converts all characters in a string to uppercase.
text = "hello"
print(text.upper())  # Output: HELLO

# str.lower(): Converts all characters in a string to lowercase.
text = "WORLD"
print(text.lower())  # Output: world

# str.capitalize(): Converts the first character of a string to uppercase and the rest to lowercase.
text = "hello world"
print(text.capitalize())  # Output: Hello world

# str.title(): Converts the first character of each word to uppercase.
text = "hello world"
print(text.title())  # Output: Hello World

# str.strip(): Removes leading and trailing whitespace characters from a string.
text = "   hello   "
print(text.strip())  # Output: hello

# str.replace(old, new): Replaces occurrences of a substring with another substring.
text = "hello world"
print(text.replace("world", "Python"))  # Output: hello Python

# str.split(sep): Splits a string into a list of substrings based on a delimiter.
text = "hello,world"
print(text.split(","))  # Output: ['hello', 'world']

# str.join(iterable): Joins elements of an iterable (e.g., list) into a single string using the specified separator.
words = ["hello", "world"]
print(",".join(words))  # Output: hello,world

# str.startswith(prefix): Checks if a string starts with the specified prefix.
text = "hello world"
print(text.startswith("hello"))  # Output: True

# str.endswith(suffix): Checks if a string ends with the specified suffix.
text = "hello world"
print(text.endswith("world"))  # Output: True

##########################  OPERATORS   ##########################

# Arithmetic Operators:
# Used to perform mathematical operations.
a = 10
b = 3

print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335
print(a % b)  # Output: 1
print(a**b)  # Output: 1000
print(a // b)  # Output: 3

# Comparison Operators:
# Used to compare values and return a Boolean result.
x = 5
y = 10

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x < y)  # Output: True
print(x > y)  # Output: False
print(x <= y)  # Output: True
print(x >= y)  # Output: False

# Assignment Operators:
# Used to assign values to variables.
x = 5
x += 3
print(x)  # Output: 8

y = 10
y -= 2
print(y)  # Output: 8

z = 5
z *= 2
print(z)  # Output: 10

# Logical Operators:
# Used to combine conditional statements.
x = True
y = False

print(x and y)  # Output: False
print(x or y)  # Output: True
print(not x)  # Output: False

# Membership Operators:
# Used to test if a sequence (e.g., list, tuple, string) contains a specific value.
my_list = [1, 2, 3, 4, 5]

print(1 in my_list)  # Output: True
print(6 not in my_list)  # Output: True

# Identity Operators:
# Used to compare the memory location of two objects.
x = 10
y = 10
z = 5

print(x is y)  # Output: True
print(x is z)  # Output: False
print(x is not z)  # Output: True
