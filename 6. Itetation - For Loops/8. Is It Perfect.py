"""
Q. Problem Description

You are given N positive integers.

For each given integer A, you have to tell whether it is a perfect number or not.

A perfect number is a positive integer which is equal to the sum of its
proper positive divisors (excluding the number itself). 
A positive proper divisor divides a number without leaving any remainder.
"""

N = int(input('How many numbers to check: '))

for i in range(N):
    A = int(input('Enter number {}: '.format(i + 1)))

    total = 1

    is_perfect = 'No'

    for j in range(2, A):
        
        if A % j == 0:
            
            total += j
           
            if total != A:            
                is_perfect = 'No'
            
            else:
                is_perfect = 'Yes'
                
            
    if is_perfect == 'Yes':
        print('{} is a Perfect number!'.format(A))

    else:
        print('{} is not a Perfect number!'.format(A))
    