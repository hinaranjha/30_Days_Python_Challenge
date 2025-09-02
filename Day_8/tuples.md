# Day 8: Tuples & Sets | Properties, Methods, Set Operations

## Tuples
### What is Tuple?
A tuple is:
* An ordered collection of items.
* Immutable → once created, you cannot change (add/remove/modify) elements.
* Similar to lists, but safer when you don’t want data to change.

### Creating a Tuple:
With Paranthesis
```bash
t1 = (1, 2, 3)
```

### Tuple Operations:
1. Concatenation
2. Repetition
3. Membership

### Tuple Methods:
* **.count(n)**: Returns how many times a value appears in the tuple.
* **.index(i)**: Returns the index of the first occurrence of a value. Raises an error if the value is not found.

### Tuple Built-in-Functions:
* len()
* max()
* min()
* sum()
* sorted()


### When to use Tuple?
* When data should not be changed (e.g., coordinates, fixed settings).
* As keys in dictionaries (since tuples are hashable, but lists are not).
* When returning multiple values from a function.




