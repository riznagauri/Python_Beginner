"""
Q. Write a program to print all even numbers from 1 to N where
you have to take N as input from the user. 
Note: Use while-loop. 
"""

N = int(input('Enter the end number: '))

i = 1

while i <= N:
    if i % 2 == 0:
        print(i, end = ' ')
    
    i +=1