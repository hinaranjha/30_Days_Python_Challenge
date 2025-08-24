# 1. string indexing
# Get the first character of "Python".
f_char = 'Python'
f_char = f_char[0]
print(f"First Character of the string: {f_char}")

# Access the last character of "Developer".
last_char = 'Developer'
print(f"Last character of the string: {last_char[-1]}")

# Extract the character at index 3 in "Computer".
extract_index_3 = 'Computer'
print(f"Extract character from {extract_index_3} at index 3: {extract_index_3[3]}")

# Use negative indexing to get the 2nd last character of "AI".
second_last = 'AI'
print(f"Second Last character: {second_last[-2]}")

# Print the middle character of "Learning".
middle_char = 'Learning'
mid = len(middle_char) // 2
print(f'Middle character of {middle_char}: {middle_char[mid]}\n\n\n')






# 2. STRING SLICING
# Slice "Programming" to get "Program".
name = 'Programming'
print(f'Program from {name}: {name[0:7]}')

# Extract "thon" from "Python".
name_1 = 'Python'
print(f"thon from {name_1}: {name_1[2:]}")

# Get every second character from "abcdefg".
second_character = 'abcdefg'
print(f"Every second character from {second_character}: {second_character[::2]}")

# Reverse "OpenAI".
reverse_string = 'OpenAI'
print(f"Reverse {reverse_string}: {reverse_string[::-1]}")

# Slice "Hello World" to get "World".
slice_world = "Hello World"
print(f"Slice {slice_world} to get 'World: {slice_world[6:]}\n\n\n")




# 3. CASE CONVERSION
# Convert "python" to uppercase.
upper_case = 'python'
print(f'{upper_case} to uppercase: {upper_case.upper()}')

# Convert "DJANGO" to lowercase.
lower_case = 'Django'
print(f'{lower_case} to lowercase: {lower_case.lower()}')

# Capitalize "machine learning".
capitalize_word = 'machine learning'
print(f'{capitalize_word} to Capitalize: {capitalize_word.capitalize()}')

# Swap case of "PyThOn RuLeS".
swap_case = 'PyThOn RuLeS'
print(f'SwapCase {swap_case}: {swap_case.swapcase()}')

# Convert "artificial intelligence" into title case.
title_case = 'artificial intelligence'
print(f"{title_case} in title case: {title_case.title()}\n\n\n")



# 4. SEARCHING
# Find the index of "o" in "Python".
find_index = 'Python'
print(f'"o" in {find_index} is at {find_index.find("o")}')

# Search for "cat" in "The dog chased the cat".
search_cat = 'The dog chased the cat.'
print(f"'Cat' in {search_cat}: {search_cat.find('cat')}")

# Count how many "a" appear in "banana".
count_a = 'banana'
print(f"The count of 'a' in {count_a}: {count_a.count('a')}")

# Find last occurrence of "l" in "Hello World".
last_occurance = "Hello World"
print(f"Last Occurance of L in {last_occurance}: {last_occurance.rfind('l')}")

# Check if "python" contains "java".
check_existence = 'python'
print(f"Java in {check_existence}: {check_existence.find('java')}\n\n\n")





# 5. CHECKING STRING CONTENT
# Check if "Hello123" is alphanumeric.
alphanumeric = 'Hello123'
print(f"Is {alphanumeric} a alphanumeric?: {alphanumeric.isalnum()}")

# Verify if "2025" is digits only.
digit = '2025'
print(f"Is {digit} a contains digit only?: {digit.isdigit()}")

# Check if "OnlyText" is alphabet only.
str = "OnlyText"
print(f"Is {str} contains only alphabets?: {str.isalpha()}")

# Test if " " contains only whitespace.
white_spaces = "  "
print(f"Is {white_spaces} only contains white spaces?: {white_spaces.isspace()}")

# Check if "HELLO" is uppercase.
check_uppercase = "HELLO"
print(f"Is {check_uppercase} contains only uppercase: {check_uppercase.isupper()}\n\n\n")




# 6. MODIFYING & REPLACING
# Replace "blue" with "red" in "The sky is blue".
string = 'The sky is blue.'
print(f"Change 'blue' with 'red' in {string}: {string.replace('blue', 'red')}")

# Remove spaces from both ends of " hello world ".
remove_space = " hello world "
print(f"Remove white space from '{remove_space}': {remove_space.strip()}")

# Replace only the first "a" in "banana" with "o".
word_replacement = 'banana'
print(f"Replace 'a' in '{word_replacement}' with 'o': {word_replacement.replace('a', 'o', 1)}")

# Remove spaces only from left side of " Python".
remove_space = " Python"
print(f"Remove left space from '{remove_space}': {remove_space.lstrip()}")

# Replace "dog" with "cat" in "dog dog dog", but only twice.
dog_cat = "dog dog dog"
print(f"Replace 2 dogs from '{dog_cat}' with 'cat': {dog_cat.replace('dog', 'cat', 2)}\n\n\n")





# 7. SPLITTING & JOINING
# Split "apple,banana,mango" into a list.
split_into_list = "apple, banana, mango"
print(f"Split {split_into_list} into list: {split_into_list.split(',')}")

# Split "line1\nline2\nline3" into separate lines.
split_lines = "line1\nline2\nline3"
print(split_lines)

# Join ["2025", "Python", "Learning"] with "-".
word_join = ['2025', 'Python', 'Learning']
print("_".join(word_join))

# Split "one two three four" into max 2 parts.
parts_of_string = 'one two three four'
mid = len(parts_of_string) // 2
first_string = parts_of_string[:mid]
second_string = parts_of_string[mid:]
print(first_string)
print(second_string)

# Rebuild the string "a-b-c" into "abc".
string = "a-b-c"
print("".join(string.split("-")))




# 8. ALIGNMENT & FORMATTING
# Center "Hi" inside 10 spaces with "*" padding.
message = "Hi"
print(message.center(10, "*"))

# Left-align "Python" inside 12 characters.
left_align = "Python"
print(f"Left-align '{left_align}' inside 12 characters: {left_align.ljust(12, '0')}")

# Right-align "Data" with "." padding.
right_align = "Data"
print(f"Right Align '{right_align}' with '.' padding: {right_align.rjust(6, '.')}")

# Pad "42" with zeros to make it 6 characters long.
pad = "42"
print(f"Make 6 character long '{pad}' with zero: {pad.zfill(6)}")

# Format 3.14159 to 2 decimal places.
number = 3.14159
print(f"Format {number} to 2 decimal paces: {round(number, 2)} \n\n\n")





# 9. F-STRING
# Print "My name is Ali and I am 20 years old" using f-string.
name = "Ali"
age = 20
print(f"My name is {name} and I am {age} years old.")

# Show "Next year I will be 21" (age calculation inside f-string).
age += 1
print(f"Next years I will be {age}")