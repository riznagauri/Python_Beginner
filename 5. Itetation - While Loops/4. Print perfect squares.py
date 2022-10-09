"""
Q. Given a number A. Print all perfect squares less than or equal to A.
Notes - Perfect squares are integers whose square root is an integer.
"""

A = int(input('Enter the number: '))

num = 1
while num ** 2 <= A:
    print(num ** 2, end= ' ')

    num += 1