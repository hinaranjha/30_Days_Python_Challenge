# Day 7: Lists | Indexing, Slicing, Methods, List Comprehensions

## Lists
### What is list?
A list in Python is a built-in data structure that lets you store multiple items (like numbers, strings, objects) in a single variable.
It is:
* **Ordered**: items have a fixed position (index starts at 0).
* **Mutable**: you can change items after creating the list.
* **Allows duplicates**: same value can appear more than once.
* **Can store mixed data types** e.g. numbers, strings, even other lists.

### Creating a list:
```bash
numbers = [1, 2, 3, 4]
words = ["Python", "AI", "Math"]
mixed = [1, "Hello", 3.14, True]
nested = [[1, 2], [3, 4]]   # list inside list
```

## Useful List Methods
```bash
list.append(x) → Add an item to the end of the list.
list.extend(iterable) → Extend list by appending elements from an iterable.
list.insert(i, x) → Insert an item at a given position.
list.remove(x) → Remove first occurrence of a value.
list.pop([i]) → Remove and return item at index i (default: last).
list.clear() → Remove all items from the list.
list.index(x[, start[, end]]) → Return index of first occurrence of a value.
list.count(x) → Return number of occurrences of a value.
list.sort(*, key=None, reverse=False) → Sort the list in place.
list.reverse() → Reverse elements of the list in place.
list.copy() → Return a shallow copy of the list.
```


## List Comprehension:
List comprehension is just a compact way to build a new list by looping through an iterable, possibly applying a condition.

### General Formula
```bash
[expression for item in iterable if condition]
```

### Parts Explained:
* **expression**: what you want to put in the list (can be the item itself or a transformation).
* **item**: a variable representing each element from the iterable.
* **iterable**: a sequence (list, string, range, etc.) you’re looping over.
* **condition (optional)**: filter to include only items that satisfy the condition.