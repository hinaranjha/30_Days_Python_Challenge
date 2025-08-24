# Day 3 - Strings
# Topics: Slicing, Methods, Formatting, f-string, Escape Sequences

### Definition:
A string is a series of characters. Anything inside the quotes is considered a string in pytho, and you can use single, or double quotes around your string like this.
"This is a string."
'This is also a string.'

This flexibility allows us to use double quotes or apostrophes within your strings like this.
"In this example, we'll understand the concept of double quote & apostropes within the string."


## String Indexing:
String indexing means **Picking a single character using it position**


                            ### Diagram
                          name = "python"
                          
                          p     y     t     h     o     n
                          0     1     2     3     4     5
                         -6    -5    -4    -3    -2    -1

1. Indexing start from 0 in python.
2. Positive indexing start from 0 while negative indexing starts from -1.
3. Positive indexes: left → right (0,1,2,...)
4. Negative indexes: right → left (-1,-2,-3,...)


## String Slicing:
Extracting a part of the string using indexes.

** string[start:end:step] **

#### Parts of slicing:
- start: index where the slice begins
- end: index where the slice stops
- step: interval between the characters (default = 1)

## String Methods:
### 1. Case Conversion:
- .upper() = convert all characters to uppercase
- .lower() = convert all character to lowercase
- .capitalize = make the first character to uppercase, rest lowercase
- .title() = capitalize first letter of every word
- .swapcase() = swap uppercase to lowercase & swap lowercase to uppercase

### 2. Searching
- .find(substring) = returns the index of the substring (-1, if not found)
- .rfind(substring) = work same as .fin(substring), but start searching from right side
- .index(substring) = like .find(substring), but throws an error if not found
- .count(substring) = count how many times substring appears

### 3. Checking String Content
- .startswith("sub")
- .endswith("sub")
- .isalpha()
- .isdigit()
- .isalnum()
- .isspace()
- .islower() / .isupper() / .istitle()

### 4. Modifying / Replacing:
- .replace(old, new, count)
- .strip() = remove white space from both ends (left side & right side)
- .lstrip() / .rstrip()

### 5. Splitting & Joining:
- .split(sep) = split string into list by separator
- ..rsplit(sep, mxsplit)
- .splitlines()
- .join(list) = join list into string with separator

### 6. Alignment / Formating:
- .center(width, fillchar)
- .ljust(width, fillchar) / .rjust(width fillchar)
- .zfill(width)
## String Formatting:
## f-string:
## Escape Sequence: