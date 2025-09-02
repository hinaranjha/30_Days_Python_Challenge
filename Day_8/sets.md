# Sets | Methods, Properties, Set Operations


## Set
### What is Set?
* When data should not be changed (e.g., coordinates, fixed settings).
* As keys in dictionaries (since tuples are hashable, but lists are not).
* When returning multiple values from a function.

### How to create Set?
* Using curly braces {}:
```bash
s = {1, 2, 3}
```

### Properties of Set:
* **Unordered**: no index, can’t access with [0].
* **Mutable**: you can add/remove items.
* **Unique**: no duplicates allowed.
* **Heterogeneous**: can hold different data types.

### Set of Operations:
* **Union**: | , .union()
* **Intersection**: & , .intersection()
* **Difference**: - , .difference()
* **Symmetric Difference**: ^ , .symmetric_difference()
* **Subset**: <= , .issubset()
* **Superset**: >= , .issuperset()
* **Disjoint**: .isdisjoint()
* **Modification**: add, remove, discard, pop, clear