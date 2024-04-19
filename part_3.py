##########################   LISTS   ##########################

# Lists in Python are ordered collections of items, which can be of any data type.
# Lists are mutable, meaning their elements can be changed after the list is created.
# Lists are defined by enclosing a comma-separated sequence of elements within square brackets [ ]

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Lists with mixed data types
mixed_list = [1, "hello", 3.14, True, [5, 6, 7]]

# Accessing elements of a list
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3
print(my_list[-1])  # Output: 5 (last element)
print(my_list[-2])  # Output: 4 (second-to-last element)

# Slicing a list
print(my_list[1:3])  # Output: [2, 3] (elements at index 1 and 2)

# Lists are MUTUABLE, so you can modify their elements:
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

# append(): Adds an element to the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# extend(): Extends the list by appending elements from the iterable.
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# insert(): Inserts an element at the specified index.
my_list = [1, 2, 3]
my_list.insert(1, 10)
print(my_list)  # Output: [1, 10, 2, 3]

# remove(): Removes the first occurrence of the specified value from the list.
my_list = [1, 2, 3, 1]
my_list.remove(1)
print(my_list)  # Output: [2, 3, 1]

# pop(): Removes the element at the specified index (or the last element if index is not provided) and returns it.
my_list = [1, 2, 3]
popped_element = my_list.pop(1)
print(my_list)  # Output: [1, 3]
print(popped_element)  # Output: 2

# index(): Returns the index of the first occurrence of the specified value.
my_list = [1, 2, 3, 1]
print(my_list.index(1))  # Output: 0

# count(): Returns the number of occurrences of the specified value.
my_list = [1, 2, 3, 1]
print(my_list.count(1))  # Output: 2

# sort(): Sorts the list in ascending order (or descending order if reverse=True is specified).
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

# reverse(): Reverses the order of the elements in the list.
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]

# clear(): Removes all elements from the list.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []

# copy():  create a shallow copy of a list
# A shallow copy means that a new list object is created,
# and it contains references to the same elements as the original list. However,
# if the elements themselves are mutable objects (e.g., lists, dictionaries),
# changes to these mutable elements in the copied list will also affect the original list and vice versa
original_list = [1, 2, 3]
copied_list = original_list.copy()

# Modify the copied list
copied_list.append(4)

# Original list remains unchanged
print("Original list:", original_list)  # Output: [1, 2, 3]
print("Copied list:", copied_list)  # Output: [1, 2, 3, 4]

# unpacking list
a, b, c = [1, 2, 3]
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

##########################   TUPLES   ##########################

# Tuples in Python are ordered collections of items, similar to lists,
# but with one crucial difference: tuples are IMMUTABLE,
# meaning their elements cannot be changed after the tuple is created.
# Tuples are defined by enclosing a comma-separated sequence of elements within parentheses ().

# Creating a list
my_tuple = (1, 2, 3, 4, 5)

# Tuples with mixed data types
mixed_tuple = (1, "hello", 3.14, True)

# Accessing elements of a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3
print(my_tuple[-1])  # Output: 5 (last element)

# Slicing a list
print(my_tuple[1:4])  # Output: (2, 3, 4) (slicing)

# Unpacking a tuple
person = ("John", 30, "New York")
name, age, city = person
print(name)  # Output: John
print(age)  # Output: 30
print(city)  # Output: New York

##########################   FOR_LOOP   ##########################

# For loops in Python are used to iterate over a sequence (such as a list, tuple, string, or range)
# and execute a block of code for each item in the sequence. The basic syntax of a for loop in Python is as follows:

# for item in iterable:
#     # Code block to execute for each item

#  for loop iterating over a list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# iterate over a range of numbers using the range() function:
# This loop will print numbers from 0 to 4.
for i in range(5):
    print(i)

# The range() function can also be used with start, stop, and step arguments
# to generate a range of numbers with specific properties
# This loop will print odd numbers from 1 to 9.
for i in range(1, 10, 2):
    print(i)
