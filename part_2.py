##########################  RECIEVE_INPUT   ##########################

# In Python, you can use the input() function to receive input from the user via the console. The input() function reads a line of text entered by the user and returns it as a string. Here's how you can use it

# Receive input from the user
name = input("Enter your name: ")
print("Hello,", name)

# You can also convert the input to other data types if needed
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Keep in mind that the input() function always returns a string. If you want to convert the input to another data type (like integer or float), you can wrap the input() function with the appropriate conversion function (int(), float(), etc.). However, you need to handle exceptions if the user enters invalid input that cannot be converted to the desired data type.

##########################  IF_CONDITIONS   ##########################

# Simple if statement:
x = 10

if x > 5:
    print("x is greater than 5")

# if-else statement:
x = 3

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

# if-elif-else statement:
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

# Nested if statement:
x = 10
y = 5

if x > 5:
    if y > 5:
        print("Both x and y are greater than 5")
    else:
        print("x is greater than 5, but y is not")
else:
    print("x is not greater than 5")

# if-elif ladder:
x = 0

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

##########################  MATCH_CASE   ##########################

# Starting from Python 3.10, you can use the match statement as an alternative to long chains of if, elif, and else statements, especially when dealing with pattern matching. The match statement provides a concise and expressive way to compare a value against multiple patterns and execute code based on the matching pattern.


def describe_fruit(fruit):
    match fruit:
        case "apple":
            print("It's an apple!")
        case "banana":
            print("It's a banana!")
        case "orange":
            print("It's an orange!")
        case _:
            print("Unknown fruit!")


# Example usage
describe_fruit("apple")  # Output: It's an apple!
describe_fruit("banana")  # Output: It's a banana!
describe_fruit("pear")  # Output: Unknown fruit!

##########################  WHILE_LOOP   ##########################

# while condition:
# Code block to execute as long as the condition is true
# This block can contain any number of statements
# Remember to update the condition inside the loop to avoid an infinite loop

# Here's an example of a simple while loop:

# Countdown from 5 to 1
count = 5
while count > 0:
    print(count)
    count -= 1

# Asking the user to enter 'quit' to exit the loop
command = ""
while command != "quit":
    command = input("Enter a command (type 'quit' to exit): ")
    print("You entered:", command)
