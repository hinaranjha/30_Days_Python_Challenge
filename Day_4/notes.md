# Day 4: Conditionals

It’s a way to make decisions in programming.
It checks conditions in order, and only one block of code will run.
Conditionals are the statements in programming that let you make decision
They check whether the condition is **True** or **False** then execute the code.

<!-- If it's raining today. Then i'll take umberalla. Otherwise i won't -->


### The structure of conditionals in python
```bash
if condition1: 
    # runs if condition1 is True
elif condition2:
    # runs if condition1 is False AND condition2 is True
elif condition3:
    # runs if above are False AND condition3 is True
else:
    # runs if none of the above conditions are True
```

### Why are conditionals important?
* They let your code make decisions instead of always running the same way.
* Used in games, apps, data analysis, and almost everything in programming.




## Match-Case Statement
### What is match-case?
* A pattern matching feature in Python (like switch-case in other languages).
* Makes code cleaner and more readable than multiple if-elif-else.
* Introduced in Python 3.10.

### Basic Syntax:
```bash
match variable:
    case pattern1:
        # code block
    case pattern2:
        # code block
    case _:
        # default case (like "else")
```

### Key Notes:
* match-case is like a switch statement, but more powerful.
* _ works as a wildcard (default case).
* Can match values, types, or even patterns inside data structures.
* Available only in Python 3.10+.