import math

def period(L, g):
    try:
        return 2 * math.pi * math.sqrt(L/g)
    except ValueError or TypeError or ZeroDivisionError:
        print('Error: Invalid input.')

print('Input a value for L')
L = int(input())

print('Input a value for g')
g = int(input())

print('Your time period T is: ' + str(period(L, g)))