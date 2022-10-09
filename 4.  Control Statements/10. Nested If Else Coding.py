"""
Q. Write a program that asks the user to input a number N.
If N is between 10 and 20, your program should ask the user to enter another number M and then:-

Print the sum of the two numbers.
If the sum is greater than equal to 100, your program should also print "That is a large sum!" on a new line.
If N is not between 10 and 20, your program should print -1.

"""

num1 = int(input('Enter the number: '))

if 10 <= num1 <= 20:
    num2 = int(input('Enter 2nd number: '))
    total = num1 + num2
    print('Sum of both numbers is: {}'.format(total))

    if total >= 100:
        print('That is a large sum!')

else:
    print(-1)