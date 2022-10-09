"""
Q. Write a program to input two numbers(A & B) from user and 
print the maximum element among A & B in each line.

"""

A = int(input('Enter 1st number: '))
B = int(input('Enter 2nd number: '))

if A > B:
    print('{} is greater than {}'.format(A,B))

else:
    print('{} is greater than {}'.format(B,A))