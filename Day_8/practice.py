# Create a tuple with 5 numbers and print the 2nd element.
tuple = (1, 3, 4, 5, 6)
print(tuple[1])

# Try to change a value in a tuple — what happens?
#  if we try to change a value in a tuple, it will raise an error
tuple[3] = 9
print(tuple)



# Find the length of a tuple.
z = (2, 3, 4, 5, 6, 7, 8)
print(f"Length of a: {len(z)}")



# Write a program to unpack a tuple into variables.
name = ('hina', 'sattar')
first, last = name
print(f"First Name: {first}")
print(f"Last Name: {last}")

# Create a set of numbers and add a new element.
x = {1, 3, 4, 5}
x.add(9)
print(f"Add 9 to the set x: {x}")



# Remove an element from a set (using remove and discard).
y = {2, 3, 4, 5, 6, 7}
y.remove(4)   # remove 4 from the set
y.discard(10)  # it'll remove even number doesn't exist
print(y)



# Find the union and intersection of {1,2,3} and {2,3,4}.
a = {1, 2, 3}
b = {2, 3, 4}
print(f"Union of a and b: {a | b}")
print(f"Intersection of a and b: {a & b}")



# Check if {1,2} is a subset of {1,2,3,4}.
m = {1, 2, 3, 4}
n = {1, 2}
print(f"n is a subset of m: {n.issubset(m)}")



# Convert a list with duplicates into a set (to remove duplicates).
c = [1, 1, 2, 3, 3, 4, 4]
c = set(c)
print(c)
print(type(c))



# Use set comprehension to create a set of squares from 1 to 10.
square = {i ** 2 for i in range(1, 11)}
print(square)           # {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}