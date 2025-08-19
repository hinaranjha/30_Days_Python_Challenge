# Day 1

# Topics: Variables, Data Types, I/O(input/output), Comments


# 1. Variables
Variable is like a container where you can store values.
Start variable with the name 'message' and assign a value 'Hello, Ahmad'.

### Variable Naming Rules:
* Start with the letter & underscore ( cannot start with the number )
* Can contain letters, digit, numbers, & underscore (_) (special characters are not allowed)
* Cannot use reserved words ( pythn uses for itself)
    * You can't use if, else, True, None, while, etc
* No spaces allowed ( only use underscore )
    * student_name

### Best Practices
1. Use descriptive name
    * age = 25
    * city_name = "Gujrat"
2. Use snake-case (highly recommended)

### Naming Rules: 
1. Snake Case
    * student_name
    * student_age
    * total_price
2. Camel Case
    * studentName
    * studentAge
    * totalPrice
3. Pascal Case
    * StudentName
    * StudentAge
    * TotalPrice

## CONSTANT
A constant is a variable whose value doesn't change throughout the program. It remains the same.
Python itself doesn't have a concept to declare constant like any other language like java or C.
But by naming convention, we can write constant with all UPPERCASE with underscore.


## Comment
Comments are notes you add in your code.
Pythn ignores them when running the program.
They are used to Explain your code (for yourself and others)

### Types of comments in python:
1. Single-line comment
    * Start with #
    * Everything after #, after ignored by python
2. Multi-line comment
    * Start with """ or '''
    * """ this is an example of multiline comments
     you can write multi-line comment using single quotation mark or double quotation mark three time
    """


# 2. Data Types
Data Types can define what kind of data a variable can store.
Python is a dynamically stored language. We don't need to declare the type of the data. Python detect it automatically

### Types:
1. Numeric Data Type
    * Integer
    * Floats
    * Complex
2. String Data Type
3. Boolean Data Type
4. Sequence Types
    * List
    * Tuple
    * Range
5. Mapping Types
    * Dictionary
6. Set Types
    * Set
    * Frozenset
7. Binary Types
    * Bytes
    * Bytearray
    * Memoryview


# Input/Output(I/O):

## Output:
Output means showing message/result to the user.
Use print() function for output.

### Formating Output:
1. ### Use f-string:
    * f-string is a most effective and recommended way to format output.
    * print(f"Hello, {name}") # curly braces contains variables name
2. ### .foramt() mathod:
    * print("My name is {} and I am {} years old.".format(name, age))

## Input:
Input is a most effective way to ask user for input in python.
Input is a best way taking data from the user.
BY default, input() always returns a string.

But we can convert input to other datatypes.
Like:
    * input("enter your height: ") returns string but
    * convert it into integer value
        * int(input("enter your height: "))

** Typecasting is most effective way to convert data types into other.**

# Strings:
A string is a sequence of characters(numbers, letters, symbols) enclosed in quotes.

name = "Hina"

## Creating Sring:
1. Single Quotes ' '
2. Double Quotes " "
3. Triple Quotes """ or ''' for multi-line string

## String Functions
### 1. Concatination:
Join the two or more string with +
print(message + " " + name)

### 2. Repetition:
We can repeat string:
word = 'Hi'
print(word * 3) # HiHiHi

### 3. Indexing:
Access String Characters by their position

text = "Python World"
print(text[0]) # P
print(text[-1]) # d

** Remember** 
Python indexing start from 0.
We can use positive indexing and negative indexing both.

P       y       t       h       o       n       -       w       o       r       l       d
0       1       2       3       4       5       6       7       8       9       10      11  = POSITIVE INDEXING
-12    -11     -10     -9      -8      -7      -6      -5      -4      -3       -2      -1  = NEGATIVE INDEXING


### 4. Slicing:
substring

print(text[0:4]) # Pyth

** String slicing start from the first number and end at the second last 
like: 
you want to slice text[0:4]
it start from 0 [P] and end at number 3 [h] not at 4 [0]