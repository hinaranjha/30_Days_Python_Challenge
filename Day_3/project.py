# Project: "Username & Password Masker"
# Username & Password Masker

# Input: username & password
user_name = input("Enter your User Name: ")
password = input("Enter your password: ")
password_len = len(password)

# Show username normally
print(f"User Name: {user_name}")

# Mask password with * (e.g., mypassword123 → ***********)
print(f"Password: {'*' * password_len}")