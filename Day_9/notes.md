# Day 9: Dictionaries | Keys, Values, Methods, Nested Dicts

## What is Dictionary?
A dictionary is a data type that help us to store data in **key-value : Pair**
* Think of it like a real dictionary: a word (key) maps to its meaning (value).
* Keys must be unique and immutable (like strings, numbers, tuples).
* Values can be of any type (string, list, number, another dictionary, etc.).

```bash
# A simple dictionary
student = {
    "name": "Ali",
    "age": 21,
    "subjects": ["Math", "Physics", "Computer Science"]
}

print(student)
```
* **Key**: name
* **Value**: Ali
## Dictionary Methods:

```bash                   
 * **.get()**         Get value safely                
 * **.keys()**         Get all keys                    
 * **.values()**       Get all values                  
 * **.items()**        Get key-value pairs             
 * **.update()**       Merge dictionaries              
 * **.pop()**          Remove key and return its value 
 * **.popitem()**      Remove last inserted pair       
 * **.clear()**        Empty dictionary                
 * **.copy()**         Copy dictionary                 
 * **.fromkeys()**     Create dict with same value      
 * **.setdefault()**   Get or set default key
```