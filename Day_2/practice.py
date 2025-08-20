# Arithematic Operators
# Write a program that takes two numbers and prints their sum, difference, product, and quotient.

num_1 = 5
num_2 = 4

print("Arithematic Operators:")

# +, Addition
sum = num_1 + num_2
print(f"Sum of {num_1} & {num_2} is {sum}")     # 9, "\n" is used to add a new line

# -, Subtraction
difference = num_1 - num_2
print(f"Difference of {num_1} & {num_2} is {difference}")       # 1

# *, Multiplicaton
product = num_1 * num_2
print(f" of {num_1} & {num_2} is {product}")      # 20

# /, Division
quotient = num_1 / num_2
print(f"Quotient of {num_1} & {num_2} is {quotient}")       # 1.25



# Use the modulus operator (%) to check if a number is even or odd.
number = 21

if number % 2 == 0:
    print("Even")
else:
    print("Odd")        # Odd


# Write a program that raises a number to the power of another number.
a = 5
b = 3
result = a ** b     # 125
print(result)



# Demonstrate compound assignment operators (+=, -=, *=, /=) with an example.
num_3 = 6

num_3 += 1      # add 1 in num_3, then num_3 will be 7
print(num_3)

num_3 -= 1      # subtract 1 from num_3, then it will be again 6
print(num_3)

num_3 *= 3      # multiply num_3 with 3, then it will be 18
print(num_3)

num_3 /= 9      # divide by 9, then answer will be 2.0
print(num_3)


# Take two numbers and check which one is greater (comparison operators).
number_1 = 8
number_2 = 89

if number_1 > number_2:
    print(f"{number_1} is Greater")
elif number_1 < number_2:
    print(f"{number_2} is Greater")
else:
    print("Both numbers are Equal")



# Write a program that checks if a number lies between 10 and 50 (logical operators).
number_3 = 1
number_4 = 60
user_number = int(input("Enter a number in between 1 and 60: "))
if user_number >= 10 and user_number <= 50:
    print("True")
else:
    print("Flase")

# Demonstrate identity operators: check if two variables point to the same object using is and is not.
first_object = [2, 3, 4]
second_object = [2, 3, 4]
third_object = first_object

print(first_object is third_object)         # True
print(first_object is not second_object)    # True

# Demonstrate membership operators: check if "a" exists in "apple" and "z" in "apple".
fruit_name = "apple"

print("a" in fruit_name and "z" in fruit_name)