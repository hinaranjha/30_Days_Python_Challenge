# # Student Gradebook
# # Create a dictionary with student names as keys and grades as values.
student_grades = {
    "Ali": 90,
    "Sara": 86,
    "Hanan": 67,
    "Amal": 60
}

# Print all student names.
print(f"Students Name: {student_grades.keys()}")

# Find the grade of a specific student.
print(f"Ali's grade: {student_grades['Ali']}\n\n\n")




# E-Commerce Inventory
# Store products in a dictionary:
products = {
    "Laptop": 800,
    "Phone": 500,
    "Tablet": 300
    }

# Add a new product "Headphones": 100.
products['Headphones'] = 100
# Update the price of "Phone" to 450.
products['Phone'] = 450
print(products, end='\n\n\n')




# Word Counter
# Take a sentence input from the user.
words = input("Enter a sentence: ")
word_count = {}
# Count the frequency of each word using a dictionary.
for word in words.split():
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    
    else:
        word_count[word] = 1

print(word_count, end='\n\n\n')




# Employee Records
# Store an employee record as:
employee_record = {
    "id": 101,
    "name": "Alice",
    "department": "HR"
    }

# Add "salary": 50000 to the dictionary.
employee_record["salary"] = 50000

print(employee_record, end='\n\n\n')




# Nested Dictionary – University
# Store multiple students in a nested dict:
grade = {
  "Alice": {"age": 20, "grade": "A"},
  "Bob": {"age": 22, "grade": "B"}
}

# print Bob's grade
print(f"Bob's Grade: {grade['Bob']} \n\n\n")




# Dictionary Comprehension
# Create a dictionary of squares {1: 1, 2: 4, 3: 9, ...} up to 10.

squares = {n : n ** 2 for n in range(1, 11)}
print(f"Squares: {squares} \n\n\n")




# Menu Ordering System
menu = {
    "Burger": 5,
    "Pizza": 8,
    "Pasta": 6
    }

print("Menu:", menu, end="\n")

# ask the user to order an item and print the price
order = input("Enter the item you want to order: ").capitalize()

if order in menu:
    print(f"The Price of {order}: ${menu.get(order)} \n\n\n")
else:
    print(f"Sorry, {order} is not on the menu. \n\n\n")




# Country Capitals
country = {
    "USA": "Washington",
    "France": "Paris",
    "Japan": "Tokyo"
}
print("Country: ", country, end=" \n")

# ask user for a country and print it's capital
country_name = input("Enter the country name: ").capitalize()

if country_name in country:
    print(f"The Capital of {country_name} is {country[country_name]}.  \n\n\n")

else:
    print(f"{country_name} does not exit in the collection.  \n\n\n")




# Shopping Cart (with Quantity)
cart = {
    "Apple": 3,
    "Banana": 5,
    "Orange": 2
}

# print total items in the cart
print(f"Total items in a cart: {len(cart)} \n")

# increase banana count by 2
cart['Banana'] += 2
print(cart, end='\n\n\n')