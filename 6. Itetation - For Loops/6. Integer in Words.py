"""
Q. Problem Description

You are given an integer A. You have to print A in word form.

Following are the words which should be replaced in place of a digit:

For digit = 0, word = zero
For digit = 1, word = one
For digit = 2, word = two
For digit = 3, word = three
For digit = 4, word = four
For digit = 5, word = five
For digit = 6, word = six
For digit = 7, word = seven
For digit = 8, word = eight
For digit = 9, word = nine
For eg., If A = 2634, you should print two six three four.

Note: Words should be seperated by a single space. Also, the output is case sensitive.
There will be no zeros at the start of a number.
"""
num_word = { '0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four',
            '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine'}

A = input('Enter the number: ')

num = ''
for i in range(len(A)):
    print(num_word[A[i]], end= ' ')

