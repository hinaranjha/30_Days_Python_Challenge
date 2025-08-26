# Project: "Simple ATM Menu"

# Display options
print("Choose an option (1-4):")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdrawal")
print("4. Exit")

# User input
choice = int(input("Choose an option (1-4): "))

# Match-case menu
match choice:
    case 1:
        print("You can check your account balance now. Enter your account number.")
    case 2:
        print("Enter the amount you want to deposit.")
    case 3:
        print("Enter the amount you want to withdraw.")
    case 4:
        print("Thanks for using our services. Come again!")
    case _:
        print("Invalid choice. Please choose from 1 to 4.")

