intro = 'Welcome to Number Guessing Game'
print(intro)

print('Pick a number between 1 and 10')
guess = input()
guess = int(guess)

import random as r
num = r.randint(1,10)

if guess == num:
    print('Nice you got it right')
else:
    print('You failed lol')