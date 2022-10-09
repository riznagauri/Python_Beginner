"""
Q.
In this exercise, you need to implement some rules from Pac-Man, the classic 1980s-era arcade-game.

You have to answer whether the Pac-Man loses or not.

Your are given the following boolean inputs (0 / 1) each in one line:

1. Does the Pac-Man have a power pellect active?

2. Is the Pac-Man touching a ghost?

The Pac-Man loses if it is touching a ghost and does not have a power pellet active.
"""
power = int(input('Enter Power (1) or no Power (0): '))
ghost = int(input('Enter Ghost (1) or no Ghost (0): '))

if not power and ghost:
    print('Sorry you Loose!')

elif power and (ghost or not ghost):
    print('Its a Win!')

elif not power and not ghost:
    print('Its a Win!')