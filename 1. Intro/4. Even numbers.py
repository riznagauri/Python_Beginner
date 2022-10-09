"""
Q. Print first 5 even numbers i.e. 0, 2, 4, 6, 8.
"""

num = 0
even_nums = []
i = 0

while i <= 4:
    if num % 2 == 0:
        even_nums.append(num)
        num += 1
        i += 1
    else:
        num += 1

print(*even_nums, sep= ' ')