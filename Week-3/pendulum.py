import math

def period(L, g):
    try:
        return 2 * math.pi * math.sqrt(L/g)
    except ZeroDivisionError or ValueError or TypeError:
        print('Error: You are trying to divide by zero.')

print('Input a value for L')
L = int(input())

print('Input a value for g')
g = int(input())

print('Your time period T is: ' + str(period(L, g)))