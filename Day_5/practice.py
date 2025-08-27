# Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)

print("\n\n\n")


# Print numbers from 10 down to 1 using a while loop.
number = 10
while number > 0:
    print(number)
    number -= 1
print("\n\n\n")


# Find the sum of numbers from 1 to 100.
for x in range(1, 101):
    sum_ = x * (x + 1) // 2
print(f"The sum(1 to 100): {sum_}")

print("\n\n\n")

# Print all even numbers between 1 and 50.
even_number = 1
while even_number < 50:
    if even_number % 2 == 0:
        print(f"{even_number} is Even")
    even_number += 1

print("\n\n\n")


# Ask the user for a number n and print its multiplication table.
user_number = int(input("Enter a number: "))
for j in range(1, 11):
    print(f"{user_number} x {j} = {user_number * j}")

print("\n\n\n")


# Write a program to calculate the factorial of a number using a loop.
k = int(input("Enter a number: "))
fact = 1
for g in range(1, k + 1):
    fact *= g
print(f"The factorial of {k} is {fact}")

print("\n\n\n")


# Use break to stop a loop when a number equals 5.
for n in range(1, 6):
    if n == 5:
        break
    print(n)

print("\n\n\n")


# Use continue to skip printing multiples of 3 between 1 and 20.
for a in range(1, 21):
    if a % 3 == 0:
        print(a)
        continue

print("\n\n\n")


# Write a loop with an else clause (e.g., search for an element in a list).
countries = ["Pakistan", "India", "China", "United States", "United Kingdom", "Canada",
             "Australia", "Germany", "France", "Japan", "Brazil", "South Africa",
             "Saudi Arabia", "Turkey", "Italy", "Spain", "Russia", "Mexico", "Indonesia", "Nigeria"]
search = input("Enter country name & check if country name exits: ").title()
for country in countries:
    if country == search:
        print(f"{search} exist in the list") 
        break
else:
    print(f"{search} does not exist in the list. Try again!")

print("\n\n\n")


# Create a nested loop to print a simple star pattern:
# *
# **
# ***
# ****
# ***** 
rows = 5
for s in range(1, rows + 1):
    for m in range(1, s + 1):
        print("*", end=" ")
    print()
    

