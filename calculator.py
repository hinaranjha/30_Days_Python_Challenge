variable_1 = int(input("Enter your first number: "))
variable_2 = int(input("Enter your second number: "))

operand = input("Choose an operand from '/, +. -, *, **, //, %': ")

if operand == '+':
    print(variable_1 + variable_2)

elif operand == '-':
    print(variable_1 - variable_2)

elif operand == '*':
    print(variable_1 * variable_2)

elif operand == '/':
    print(variable_1 * variable_2)

elif operand == '**':
    print(variable_1 ** variable_2)

elif operand == '//':
    print(variable_1 // variable_2)

elif operand == '%':
    print(variable_1 % variable_2)

else:
    print("Choose the right operand")