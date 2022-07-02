import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c': # While feedback is not equal to the answer
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        # asks user if the computed guess it too high, too low, or correct.
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C) ').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1

    # when conditions of loop are satisfied, break and print a message confirming correct answer.    
    print(f'Yay! The computer guessed your number {guess}, correctly!')


computer_guess(1000)