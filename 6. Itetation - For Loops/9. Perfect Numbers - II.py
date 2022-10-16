"""
Q. Problem Description
You are given an integer A as input.

You have to print all the perfect numbers which lie in the range [1, A] in ascending order.
A perfect number is a positive integer which is equal to the sum of its
proper positive divisors (excluding the number itself). 
A positive proper divisor divides a number without leaving any remainder.
"""

A = int(input('Enter the number till which you want all Perfect numbers: '))

for i in range(A):

    total = 1

    is_perfect = 'No'

    
    for j in range(2, (i //2) + 1):

        
        if i % j == 0:
            total += j
            
            if total != i:
                is_perfect = 'No'
                
            else:
                is_perfect = 'Yes'

    if is_perfect == 'Yes':
        print('{} is a Perfect number!'.format(i))
    
