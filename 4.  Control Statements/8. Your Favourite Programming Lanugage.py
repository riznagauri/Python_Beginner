"""
Q. Write a program that asks the user to input their favorite 
programming language and output a specific string based on their answer.
Based on the user inputs these are the outputs to be shown to the user.

Programming Language    --> Output
Python or Java          --> Nice choice!
Golang                  --> You're a cool person I see...
JavaScript              --> Okay so you are our web developer!
C++                     --> Too old school...
Anything else           --> I don't know that language.

Note: The input will be case sensitive and exact as mentioned in the above list
"""

fav_lang = input('Enter you favorite programming language: ')

if fav_lang == 'Python' or fav_lang == 'Java':
    print('Nice choice!')
elif fav_lang == 'Golang':
    print("You're a cool person I see...")
elif fav_lang == 'JavaScript':
    print('Okay so you are a web developer')
elif fav_lang == 'C++':
    print('Too old school...')
else:
    print("I don't know that language.")