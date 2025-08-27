# Project: "Number Guessing Game"
import random

player_1 = random.randint(1, 100)   # Computer's secret number
user_choice = input("Choose level (easy, intermediate, hard): ").lower()

if user_choice == "easy":
    attempt = 10
elif user_choice == "intermediate":
    attempt = 7
elif user_choice == "hard":
    attempt = 3
else:
    print("Invalid choice. Defaulting to easy mode.")
    attempt = 10

while attempt > 0:
    player_2 = int(input(f"Enter a number (1 to 100). Attempts left {attempt}: "))
    attempt -= 1  # reduce attempt after each guess

    if 1 <= player_2 <= 100:  # valid range check
        if player_2 > player_1:
            print("Your guess is greater than the actual number.")
        elif player_2 < player_1:
            print("Your guess is smaller than the actual number.")
        else:
            print("🎉 Correct! You guessed the number. You win!")
            print("The number was:", player_1)
            break
    else:
        print("❌ Invalid input. Choose a number between 1 and 100.")

else:
    print("😢 You've run out of attempts! You lost.")
    print("The number was:", player_1)
