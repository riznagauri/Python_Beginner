"""
Q. Problem Description

Given an integer A as input, you have to tell whether it is a prime number or not.

A prime number is a natural number greater than 1 which is divisible only by 1 and itself.

"""

A = int(input('Enter the number to be checked for Prime: '))

is_prime = 'Prime Number'

max_divisor = A // 2

for i in range(2,max_divisor + 1):
    if A % i == 0:
        is_prime = 'not a Prime Number'
        break

print('{} is a {}'.format(A, is_prime))
