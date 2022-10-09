"""
Q. Perform the following operations on 6 and 3 and print their respective outputs in different lines.
1. Addition
2. Subtraction
3. Multiplication
4. Division
"""

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

print('Addition of number {} & {} is: {}'.format(num1, num2, num1 + num2))

if num1 > num2: # Checking which number is greater
    print('Subtraction of number {} from {} is: {}'.format(num2, num1, num1 - num2))
else:
    print('Subtraction of number {} from {} is: {}'.format(num1, num2, num2 - num1))

print('Multiplication of number {} & {} is: {}'.format(num1, num2, num1 * num2))

if num1 != 0 and num2 != 0:
    print('Division of number {} by {} is: {}'.format(num1, num2, num1 / num2))
else:
    print('Cannot divide when number is zero!')