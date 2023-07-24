# User Input
operand_1 = float(input('Enter first operand: '))
operand_2 = float(input('Enter second operand: '))

# Calculator Menu
print('Calculator Menu')
print('---------------')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division\n')
# The \n creates a blank line in the output

selection = int(input('Which operation do you want to perform? '))

# This code is meant to use the student's selection to give a final output!
if selection == 1:
    result = operand_1 + operand_2
    print(f"The result of the operation is {result}. Goodbye!")
elif selection == 2:
    result = operand_1 - operand_2
    print(f"The result of the operation is {result}. Goodbye!")
elif selection == 3:
    result = operand_1 * operand_2
    print(f"The result of the operation is {result}. Goodbye!")
elif selection == 4:
    result = operand_1 / operand_2
    print(f"The result of the operation is {result}. Goodbye!")
else:
    print("Error: Invalid selection! Terminating program.")

