"""
Q. Write a program to input from user an integer(A) representing the rating of a person on a platform.

You have to print the category of that person.

If the rating is greater than or equal to 2100 then that person is "grand master".
If the rating is greater than or equal to 1900 then that person is "candidate master".
If the rating is greater than or equal to 1600 then that person is "expert".
If the rating is greater than or equal to 1400 then that person is "pupil".
If the rating is smaller than 1400 then that person is "newbie".

Note: Print all the chars of the category of the person in lowercase if rating is odd otherwise print in UPPERCASE
"""
odd_rating = bool()

user_rating = int(input("Enter rating of the user: "))


if user_rating % 2 != 0:
    odd_rating = True
else:
    odd_rating = False

if user_rating < 1400:
    user_category = 'newbie'

elif 1400 <= user_rating < 1600:
    user_category = 'pupil'

elif 1600 <= user_rating < 1900:
    user_category = 'expert'

elif 1900 <= user_rating < 2100:
    user_category = 'candidate master'

elif user_rating >= 2100:
    user_category = 'grand master'

print(user_category if odd_rating else user_category.upper())

