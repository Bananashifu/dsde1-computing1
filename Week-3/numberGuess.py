print('Welcome to Number Guessing Game')

import random as r
num = r.randint(1,10)

print('Pick a number between 1 and 10. You have three tries.')

i = 1 
while i < 4:
    print('This is guess number ' + str(i) + ':')
    guess = int(input())
    if guess == num:
        print('Nice you got it right')
        break
    elif guess > 10:
        print("That's not even in the range fam")
    else:
        print('You failed lol')
    i += 1

print('Thanks for playing')