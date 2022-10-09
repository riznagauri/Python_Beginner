"""
Q. Write a program that asks the user to input their age and 
tells them if they're old enough to ride a roller coaster.
The minimum age to ride the roller coaster in this question is 13.
"""

age = int(input('Enter your age: '))
age_limit = 13

if age >= age_limit:
    print('You can ride the roller coaster!')

else:
    print("You can't ride the roller coaster.")