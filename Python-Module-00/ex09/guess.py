from random import randint

print("This is an interactive guessing game! \n\
You have to enter a number between 1 and 99 to find out the secret number. \n\
Type 'exit' to end the game.\n\
Good luck!")

n = randint(1, 100)

i = 0
while(1):
    try:
        guess = int(input('Whats your guess between 1 and 99?\n'))
    except ValueError:
        print('Thats not a number')
        continue
    if guess == 'exit':
        print('Goodbye')
        exit(0)
        continue
    elif int(guess) > 99 or int(guess) < 0:
        print('Invalid guess')
    else:
        if guess < n:
            print('Too low!')
        elif guess > n:
            print('Too high')
        else:
            if n == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            else:
                print("Congratulations, you've got it!")
            print("You won in {} attempts!".format(i))
            exit(0)
    i += 1