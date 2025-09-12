from functools import reduce
# Square Numbers (map + lambda)
# Given [1, 2, 3, 4], return [1, 4, 9, 16]
number = [1, 2, 3, 4]
square = list(map(lambda x : x * x, number))
print("Square: ", square)



# Filter Even Numbers (filter + lambda)
# From [1, 2, 3, 4, 5, 6], return [2, 4, 6]
num_list  = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x : x % 2 == 0, num_list))
print("Even Numbers: ", even_numbers)



# Convert List of Strings to Integers (map)
# Input: ["1", "2", "3"] → Output: [1, 2, 3]
string = ["1", "2", "3"]
integer = list(map(lambda x : int(x), string))
print("Integers: ", integer)



# Find the Largest Number (reduce)
# From [10, 25, 7, 50, 32], return 50
b = [10, 25, 7, 50, 32]
greatest_number = reduce(lambda x , y : x if x > y else y, b)
print("Greatest Number: ", greatest_number)



# Multiply All Numbers (reduce)
# From [2, 3, 4], return 24
a = [2, 3, 4]
result = reduce(lambda x,y : x * y, a)
print("Total: ", result)



# Name Formatting (map + lambda)
# Input: ["alice", "bob", "charlie"] → Output: ["Alice", "Bob", "Charlie"]
name =  ["alice", "bob", "charlie"]
format_name = list(map(lambda n : n.capitalize(), name))
print("Capitalize Format: ", format_name)



# Filter Out Empty Strings (filter)
# Input: ["hello", "", "world", "", "python"] → Output: ["hello", "world", "python"]
list_1 = ["hello", "", "world", "", "python"]
filter_list = list(filter(lambda x : x!= "", list_1))
print("List without Empty Strings: ", filter_list)



# Sum of Odd Numbers (reduce + filter)
# From [1, 2, 3, 4, 5], return 9
n = [1, 2, 3, 4, 5]
odd_numbers = list(filter(lambda x : x % 2 != 0, n))
odd_numbers_sum = reduce(lambda x, y : x + y, odd_numbers)
print("Sum: ", odd_numbers_sum) 



# Transform Prices (map)
# Input: [100, 200, 300], add 10% tax → [110, 220, 330]
prices = [100, 200, 300]
add_tax = list(map(lambda x : x + x * 0.1, prices))
print("Prices after Tax: ", add_tax)



# Check Palindromes (filter + lambda)
# Input: ["madam", "python", "level", "world"] → Output: ["madam", "level"]
points = ["madam", "python", "level", "world"]
final_result = list(filter(lambda x : x if x == x[::-1] else None, points))
print("Palindromes: ", final_result)