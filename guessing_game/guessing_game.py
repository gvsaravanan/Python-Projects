from itertools import count
import random

print('''

Let's play a game! 🫡
Try to guess the number I am thinking of. 🤔
The number will be between 1 and 100. 🔢
I will be giving you hints to help you narrow down the number. 🙌
I will also be keeping track of your guesses, so guess wisely. 👀
Good luck! 😈

''')

randomNum = random.randint(1, 100)
count = 0

while True:

    try:
        print('What is your guess? ')
        guess = int(input())

        if guess < 1 or guess > 100:
            raise ValueError

        count += 1

        if guess > randomNum:
            print('\nGuess lower ⬇️\n')
        elif guess < randomNum:
            print('\nGuess higher ⬆️\n')
        else:
            print(
                f'\nYou got it! The number was {randomNum} and it took you {count} guesses! 👏\n')
            break
    except ValueError:
        print('\nPlease enter a integer between 1 and 100 😡\n')