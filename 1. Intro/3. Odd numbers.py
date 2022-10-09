"""
Q. Print first 5 odd numbers i.e. 1, 3, 5, 7, 9.
Output format: Print first five odd numbers separated by space.
"""

num = 0
odd_nums = []

i = 0

while i <= 4:
    if num % 2 != 0:
        odd_nums.append(num)
        num += 1
        i += 1

    else:
        num += 1

print(*odd_nums, sep=' ')
    
