# Ask the user for a number and print if it’s positive, negative, or zero.
number = int(input("Enter any number e.g 1, 2, 3: "))

if number > 0:
    print(f"{number} is Positive.")
elif number < 0:
    print(f"{number} is Negative")
else:
    print("Zero")
    

# Take a user’s age and print whether they’re a child, teenager, adult, or senior.
user_age = int(input("Enter your age: "))

if user_age <= 12:
    print(f"User age is {user_age}. So, he/she is child.")
elif user_age >= 13 and user_age <= 20:
    print(f"User age is {user_age}. So, he/she is in their teenage.")
elif user_age >= 21 and user_age < 35:
    print(f"User age is {user_age}. So, he/she is Adult.")
else:
    print(f"User age is {user_age}. So, he is senior.")


# Ask for a grade (A–F) and print remarks (A → Excellent, B → Good, etc.).
user_grade = int(input("Enter your grade in %: "))

if user_grade > 90:
    print("Excellent.")
elif user_grade < 90 and user_grade > 80:
    print("Good")
elif user_grade < 80 and user_grade > 60:
    print("Pass")
else:
    print("Fail")


# Write a program that checks if a year is a leap year.
year = int(input("Enter a year: "))  # [1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096] """

if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is NOT a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")

    
# Input a number and check if it’s divisible by both 3 and 5.
input_number = int(input("Enter a number: "))

if input_number % 3 == 0 and input_number % 5 == 0:
    print(f"{input_number} is divisible by 3 and 5.")
else:
    print(f"{input_number} is not divible by 3 and 5.")


# Write a program that takes two numbers and prints the larger one.
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter Second number: "))

if number_1 > number_2:
    print(f"{number_1} is greater than {number_2}")
elif number_2 > number_1:
    print(f"{number_2} is greater than {number_1}")
else:
    print("Try again!")


# Ask the user for a number and print "Even" if even, "Odd" if odd (use ternary operator).
user_number = int(input("Enter a number: "))
result = "Even" if user_number % 2 == 0 else "Odd"
print(result)


# Write a program using nested if to check if a number is > 100, between 50–100, or < 50.
point_number = int(input("Enter a number: "))

if point_number > 100:
    print(f"{point_number} is greater than 100.")
else:
    if point_number >= 50:   # nested inside else
        print(f"{point_number} is between 50 and 100.")
    else:
        print(f"{point_number} is less than 50.")


# Use match-case: take a day number (1–7) and print the day of the week.
week_day_number = int(input("Enter a number between 1-7: "))

match week_day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input! Please enter a number between 1 and 7.")


# Use match-case: build a simple calculator (+, -, *, /) with two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operand = input("Enter an operand(+, -, *, /): ")

match operand:
    case '+':
        print(f"{a} + {b}: {a + b}")
    case '-':
        print(f"{a} - {b}: {a -b}")
    case '*':
        print(f"{a} * {b}: {a * b}")
    case '/':
        if b != 0:
            print(f"{a} / {b}: {a / b}")
        else:
            print("Error: Division by Zero")
    case _:
        print("Invalid Operation!")
