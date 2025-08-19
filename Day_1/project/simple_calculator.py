number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

operand = input("Choose an operand '+, -, *, /': ")

if operand == "+":
    print(number_1 + number_2)
elif operand == '-':
    print(number_1 - number_2)
elif operand == '*':
    print(number_1 * number_2)
elif operand == '/':
    print(number_1 / number_2)
else:
    print("Choose right operand.")