# Day 5: Loops (for, while, break, continue, else)

## Loops
A loop is a programming  structure that let's you to repeat a code multiple times untill the condition met.
Instead of writing the code again and again you can use loops to automate repetition.

## Why do we use loops?
* To reduce repetition in code
* To process data one by one (e.g: going through list of names)
* To perform tasks untill the condition changes
* To make program perform, shorter, & cleaner

## Types of loops:
1. for loop (Repeat a block a specific number of times or through a collection):
    ```bash
    <!-- print number 1 to 5 -->
    for i in range(1, 6):
        print(i)
    ```
2. while loop (Repeat until a condition becomes False)
    ```bash
        <!-- Print numbers 1 to 5 -->
        i = 1
        while i <= 5:
            print(i)
            i += 1
    ```
3. Nested Loop (Loop inside another loop)
    ```bash
    <!-- # Print a 3x3 grid -->
        for row in range(3):
            for col in range(3):
                print("(", row, ",", col, ")", end=" ")
            print()
    ```

### Breaking / Skipping in loop:
* break: Stop the loop completely
* continue: skip the current iteration and move to the next


**Use for when you know how many times to loop.**
**Use while when you don’t know the number of repetitions but have a condition.**
