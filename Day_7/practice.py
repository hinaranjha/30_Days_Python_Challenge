# Create a list of 5 numbers and print the first and last elements.
numbers = [1, 2, 3, 4, 5]
print(f"Fist number of the list {numbers} is: {numbers[0]}")
print(f"Fist number of the list {numbers} is: {numbers[-1]}\n\n\n")



# Replace the 2nd element of a list with a new value.
name = ['Python', 'Javascript', 'Ruby', 'R', 'Next.js']
name[1] = 'Django'
print(f"Replace 2nd element of the list with 'Djando': {name}\n\n\n")



# Append an item to a list and then remove it.
list = [1, 2, 3, 4, 5]
list.append(6)
print(list, end='\n\n\n')



x = [23, 45, 12, 0, 10]
print("Smallest:", min(x))
print("Largest:", max(x))
print("\n\n\n")

# Sort a list of numbers in ascending and descending order.
random_list = [3, 8, 6, 9, 1, 7, 0, 11]
random_list.sort()        # smalles to the largest
print(f"Ascending Order: {random_list}\n")

random_list.sort(reverse=True)       # largest to smalest
print(f"Descending Order: {random_list}\n\n\n")



# Write a program to remove duplicates from a list.
items = [1, 1, 2, 2, 3, 4, 4]
unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)

print(unique_items, end='\n\n\n')



# Reverse a list without using slicing ([::-1]).
list = [1, 2, 3, 4]
list.reverse()
print(list, end='\n\n\n')



# Square all numbers in a list using list comprehension.
list_of_number = [2, 3, 4, 5 ,6, 7]
square_numbers = [i ** 2 for i in list_of_number]
print(f"Square: {square_numbers}\n\n\n")



# Filter out even numbers from a list using list comprehension.
a = [1, 2, 3, 4, 5, 7, 8, 9, 11, 14, 20, 17]
even_numbers = []
for num in a:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even Numbers: {even_numbers}\n\n\n")      # [2, 4, 8, 14, 20]



# Combine two lists into one (e.g., [1,2,3] and [4,5,6] → [1,2,3,4,5,6]).
list_1 = [1, 2, 3]
list_2 = [4, 5 ,6]
list_3 = list_1 + list_2
print(list_3)