# Unit Converter (Celsius ↔ Fahrenheit, Km ↔ Miles, etc.)mm


print("Unit Converter:")
print("1. KM to Miles")
print("2. Miles to KM")
print("3. Fahrenheit to Celsius")
print("4. Celsius to Fahrenheit")

user_choice = int(input("Choose an option (1-4): "))

if user_choice == 1:
    km = float(input("Enter Kilometers: "))
    km_to_miles = km / 1.60934
    print("Kilometers to Miles:", km_to_miles)

elif user_choice == 2:
    miles = float(input("Enter Miles: "))
    miles_to_km = miles * 1.60934
    print("Miles to Kilometers:", miles_to_km)

elif user_choice == 3:
    f = float(input("Enter Fahrenheit: "))
    fahrenheit_to_celsius = (f - 32) * 5/9
    print("Fahrenheit to Celsius:", fahrenheit_to_celsius)

elif user_choice == 4:
    c = float(input("Enter Celsius: "))
    celsius_to_fahrenheit = (c * 9/5) + 32
    print("Celsius to Fahrenheit:", celsius_to_fahrenheit)

else:
    print("Invalid choice! Please choose between 1-4.")
