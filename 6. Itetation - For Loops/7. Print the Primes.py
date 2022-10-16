"""
Q. Problem Description

You are given an integer N you need to print all the Prime Numbers between 1 and N.

Prime numbers are numbers that have only 2 factors: 1 and themselves. 
For example, the first 5 prime numbers are 2, 3, 5, 7, and 11.
"""

N = int(input('Enter the number till which you want all the Prime numbers: '))

print('All Prime numbers till {} are: '.format(N))


for i in range(2,N):

    is_prime = 'Yes'
    
    
    for j in range(2, (i // 2) + 1):
        
        
        if i % j == 0:
            
            is_prime = 'No'
            break
    
    if is_prime == 'Yes':
        print(i)

    

