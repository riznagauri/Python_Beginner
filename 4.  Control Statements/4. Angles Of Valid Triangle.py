"""
Q. You are given 3 integer angles(in degrees) A, B and C of a triangle.
You have to tell whether the triangle is valid or not.
A triangle is valid if sum of its angles equals to 180.

"""
A = int(input('Enter the degree of angle A: '))
B = int(input('Enter the degree of angle B: '))
C = int(input('Enter the degree of angle C: '))

print('Valid angles of a triangle' if A + B + C == 180 else 'Not valid angles')