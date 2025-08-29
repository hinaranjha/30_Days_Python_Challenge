# Day 6: Functions | Parameters, Return, Default, (*args, **kwargs)

## Function:
A function is a **block of resueable code** that perform a specific task.
Instead of writing code again and again, you write code once inside the function and call it whenever you need.

```bash
A function is like cooking a recipe, instead of writing everytime when you start cooking a dish.
You write it once, and then use it whenever you need.
```

### Basic Structure of a function
```bash
def function_name(parameters):
    # code block
    return result
```
* **def**: a keyword to define a function
* **function_name**: a name you give your function
* **parameter**: input your function can take(optional but important)
* **return**: sends the output back(optional, but useful)

### Why Do We Need Functions?
Without functions:
* You’ll repeat the same code everywhere.
* Your program will look messy and hard to understand.
* Changing one part means fixing it in many places.

With functions:
* Write once → use many times.
* Code becomes organized.
* Easier to test, debug, and reuse.

### How Functions Work in Python?
Steps:
1. **Define**: Write the function (like storing a recipe).
2. **Call**: Use the function (like cooking using the recipe).




### Inputs & Outputs
Functions can take inputs (like ingredients) and give outputs (like the final dish).

```bash
Think of a function like a **magic box**.
* You put something in → function processes it → gives you something out.
```




## Parameters:
Parameters are **inputs** we pass inside the function. They are optional but useful & change the whole function.

```bash
def greet(name):
    return f'Hello, {name}'

message = great('hina')
print(message)
```

* name is the parameter that we pass inside the function.
* **Parameters** also known as **arguments**




## Return Value
### What is a return value?
* A return value is the output that a function gives back after it finishes running.
* You use the **return** keyword to send this output back to the caller.

### If you don’t use return
* If a function has **no return statement**, Python automatically returns **None**.




## Default:
### What are default parameters?
* When defining a function, you can assign default values to parameters.
* If the caller doesn’t pass a value, the default is used automatically.

```bash
def greet(name='hina'):
    return f'Hello, {name}'

message = greet()
print(message)
```

* If no value is provided → Python uses "Hina".
* If you pass a value → that value overrides the default.




## *args:
In Python, ***args** is used in a function definition to allow the function to accept a variable number of arguments.
Think of it like:
* **Without *args**: your function takes a fixed number of inputs.
* **With *args**: your function can take any number of inputs (0, 1, 10, 100...).
The ** * ** collects all extra positional arguments into a tuple.

```bash
def add_all(*args):
    return sum(args)

print(add_all(2, 3))        # 5
print(add_all(2, 3, 4))     # 9
print(add_all(1, 2, 3, 4))  # 10
```

### Why Use *args?
* Makes functions flexible.
* Useful when you don’t know how many arguments will be passed.
* Helps avoid writing multiple versions of the same function.

1. *args = many positional arguments, stored as a tuple.
2. You can loop over them or pass them to other functions.




## **kwargs:
### What is **kwargs?
* In Python, ****kwargs** lets a function accept a **variable number of keyword arguments**.
* All those keyword arguments are collected into a dictionary (key-value pairs).

```bash
def student_info(**kwargs):
    print(kwargs)

student_info(name="Hina", age=25, grade="A")
```

### Why Use **kwargs?
* Makes functions very flexible.
* Useful when you don’t know in advance what options a user may pass.
* Often used in libraries (like Django, Flask, Pandas) to pass extra settings.