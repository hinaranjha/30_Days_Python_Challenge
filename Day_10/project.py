# Mini Project – Data Transformation Tool

from functools import reduce

while True:

    print("Data Transformation Tool", end="\n")
    print("Tasks you can perform: ")
    print("1. Square all numbers")
    print("2. Filter even numbers")
    print("3. Calculate product of numbers")
    print("4. Exit")


    ask_user = int(input("Choose the number between(1-4): "))

    if ask_user == 1:
        # user entered the number separated by spaces
        user_input = input("Enter list of number separated by spaces: ")

        # convert user_input into list
        numbers = list(map(int, user_input.split()))
        
        # square all the numbers
        square_numbers = list(map(lambda x : x * x, numbers))
        print(f"Square of Numbers: {square_numbers} \n\n\n")


    elif ask_user == 2:
        # user entered the number separated by spaces
        user_input = input("Enter list of number separated by spaces: ")

        # convert user_input into list
        numbers = list(map(int, user_input.split()))

        # filter even numbers
        even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
        print(f"Even Numbers: {even_numbers} \n\n\n")


    elif ask_user == 3:
        # user entered the number separated by spaces
        user_input = input("Enter list of number separated by spaces: ")

        # convert user_input into list
        numbers = list(map(int, user_input.split()))

        # calculate product of numbers
        sum_of_numbers = reduce(lambda x, y : x + y, numbers)
        print(f" Sum: {sum_of_numbers} \n\n\n")

    elif ask_user == 4:
        print("Exit the Data Transformation Tool! BYE", end='\n\n')
        break

    else:
        print("Invalid Input", end="\n\n\n")
        print(ask_user)

