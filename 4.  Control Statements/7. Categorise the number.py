"""
Q. Write a program to input a number(A) from user and print

1 if it is positive,
-1 if it is negative,
0 if it's neither positive nor negative.
"""

A = int(input('Enter the number: '))

if A == 0:
    print('Number is neither Positive nor Negative.')
elif A > 0:
    print('Number is Positive.')
else:
    print('Number is Negative.')