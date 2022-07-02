import random

# loop for guessing the computer generated number until correct.
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    
    # on correct guess, break loop and display the following:
    print(f"That is correct! You have guessed the number {random_number} correctly. Great job!")

guess(10)
