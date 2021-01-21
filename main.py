# Author: Ileana Hernandez
# Date: 01/20/2021
# Description: Guess the integer

import random

secretNumber = random.randint(-12, 12)
print('Enter the integer for the player to guess.')
print(secretNumber)
for guessesTaken in range(1, 99):
    print('Enter your guess')
    guess = int(input(15))

if guess < secretNumber:
    print('Too low - try again:')
elif guess > secretNumber:
    print('Too high - guess again:')

if guess == secretNumber:
    print('You guessed it in ' + str(guessesTaken) + ' tries')
