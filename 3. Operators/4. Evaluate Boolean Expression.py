"""
Q. What is the value of result at the end of the following code?

x = 20
y = 5
result = (x + True) / (4 - y * False)

"""

x = 20
y = 5
result = (x + True)  / (4 - y * False) # x + True = 20 + 1 = 21 ; 4 - 5 * 0 = 4 ; 21 / 4 = 5.25

print(result)
