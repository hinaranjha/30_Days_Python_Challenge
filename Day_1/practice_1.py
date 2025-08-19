# Create variables for your name, age, and country and print them in a single line.
name = "Hina Sattar"
age = "24"
country = "Pakistan"
print(f"{name} is a {age} years old girl living in {country}.")




# # Store two integers and print their sum, difference, product, and quotient.
num_1 = 5
num_2 = 6

# sum of numbers
add = num_1 + num_2
print(f'Sum of {num_1} & {num_2} is {add}.')

# difference of num_1 &  num_2
difference = num_1 - num_2
print(f'Difference of {num_1} & {num_2} is {difference}.')

# product of num_1 & num_2
product = num_1 * num_2
print(f'The product of {num_1} & {num_2} is {product}.')

# quotient/power of num_1 & num_2
quotient_of_1 = num_1 ** 2
quotient_of_2 = num_2 ** 2
print(f'The Quotient of {num_1} is {quotient_of_1}.')
print(f'The Quotient of {num_2} is {quotient_of_2}.')




# Create a variable with your full name and print it in uppercase.
full_name = "hina sattar"
print(full_name.upper())




# Ask the user for two numbers and swap their values without using a third variable.
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the 2nd number: "))
number_1, number_2 = number_2, number_1
print(number_1, number_2)




# Print the data type of each of these: 5, "5", 5.0, [5], (5,), {5}.
datatype_1 = 5          # int
datatype_2 = "5"        # str
datatype_3 = 5.0        # float
datatype_4 = [5]        # list
datatype_5 = (5,)       # tuple
datatype_6 = {5}        # set
print(f"Data Type of {datatype_1} is {type(datatype_1)}.")
print(f"Data Type of {datatype_2} is {type(datatype_2)}.")
print(f"Data Type of {datatype_3} is {type(datatype_3)}.")
print(f"Data Type of {datatype_4} is {type(datatype_4)}.")
print(f"Data Type of {datatype_5} is {type(datatype_5)}.")
print(f"Data Type of {datatype_6} is {type(datatype_6)}.")




# Ask the user to input a float and print it rounded to 2 decimal places.
user_float = float(input("Enter a float number like 5.0, 3.14157: "))
print(f'{user_float} : {round(user_float, 2)}')




# Create three variables a=10, b=20, c=30 and print their average
a = 10
b = 20
c = 30
average = (a + b + c) / 3
print(f'Average of {a}, {b}, & {c} is {average}')




# Write a program that takes a user's name and prints "Hello, [Name]!".
user_name = input("Enter your full name: ")
print(f"Hello, {user_name.title()}!")




# Create a multiline string and print it without line breaks.
multi_string = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''
print(multi_string)


# Ask the user for their birth year and print their age.
current_year = 2025
birth_year = int(input("What is your birth year?: "))
age = current_year - birth_year
print(age)