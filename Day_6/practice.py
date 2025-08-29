# Write a function that takes two numbers and returns their sum.
def sum_of_numbers(a, b):
    return a + b

final_value = sum_of_numbers(4, 5)
print(final_value)



# Write a function that checks if a number is prime.
def check_prime(number):
    if number <= 0:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
        return True

number = int(input("Enter a number you wanna check prime: "))
prime_number = check_prime(number)
print(prime_number)



# Write a function that returns the factorial of a number.
def return_factorial(fact):
    f = 1
    for n in range(1, fact + 1):
        f = f * n
    return f

fact = int(input("Enter factorial number: "))
x = return_factorial(fact)
print(f"Factorial of {fact} is: {x}")



# Create a function with a default parameter (e.g., greet(name="Guest")).
def greet(name = 'Guest'):
    print(f"Hello, {name}. Welcome in the world of python!")

greet("Hina")
greet()



# Write a function that takes any number of arguments (*args) and returns their sum.
def sum_of_args(*args):
    return sum(args)

print(sum_of_args(1, 3, 4 ,5, 7, 0))



# Write a function that accepts keyword arguments (**kwargs) and prints them.
def keyword_argument(**kwargs):
    print(kwargs)

keyword_argument(Name="Hina", Age=25, Profession="Web Developer")



# Write a function that reverses a string.
def reverse_string(string):
    return string[::-1]

string = input("Enter a string that you wanna reverse: ")
print(reverse_string(string))


# Write a function that takes a list and returns the largest element.
def largest_number(list_of_numbers):
    largest = list_of_numbers[0]
    for num in list_of_numbers:
        if num > largest:
            largest = num
    return largest

list_of_numbers = [1, 2, 3, 6, 87, 98, 45, 34]
number = largest_number(list_of_numbers)
print(f"Largest number in the {list_of_numbers} is {number}.")



# Write a function that takes a sentence and returns the number of vowels.
def return_vowels(words):
    vowels = 'aeiouAEIOU'
    list = []
    for word in words:
        if word in vowels:
            list.append(word)
    return list

words = input("Enter a word where you wanna check vowels: ")
print(return_vowels(words))



# Write a function to calculate the area of a rectangle (length × width).
def area_of_rectangle(length, width):
    return length * width

length = float(input("Enter length of the rectangle (in meters): "))
width = float(input("Enter width of the rectangle (in meters): "))

area = area_of_rectangle(length, width)
print(f"The area of the rectangle is: {area:.2f} square meters")



def total_bill(bill, tip_percent):
    tip_percentage = (tip_percent / 100) * bill
    total_bill = bill + tip_percentage
    return total_bill

tip_percent = int(input("Enter the tip percentage: "))

result = total_bill(1000, tip_percent)
print(f"The total bill with tip is: {result}")


def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

student_info(name="Hina", age=25, grade="A")
