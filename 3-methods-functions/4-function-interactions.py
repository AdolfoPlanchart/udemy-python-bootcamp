from random import shuffle

# This file means to mimic the 'Three Cup Monte' Carnival game.

cups = ['O',' ',' ']

def player_guess():
    guess = ''
    
    while guess not in ['1','2','3']:
        guess = input('Pick one of the following numbers: 1, 2, 3\n')
        
    return int(guess)

def check_guess(cups,guess):
    if(cups[guess-1] == 'O'):
        print('You win!')
    else:
        print('You lose...')

guess = player_guess()

check_guess(cups,guess)
print(cups)