operand1= int(input('Enter the first number: '))
operand2= int(input('Enter the second number: '))

operator= input('Enter the operator(+,-,*,/): ')

if operator == '+':
    print('The sum of two number is ',operand1 + operand2)
elif operator == '-':
    print('The diffrerence of two number is ',operand1 - operand2)
elif operator == '*':
    print('The product of two number is ',operand1 * operand2)
elif operator == '/':
    print('The quotient of two number is ',operand1 / operand2)
else :
    print('none')
print("\nThank You!")