
#import the necessary modules
import random

# set the starting number
num = 5
# set the range of numbers
min_num = 1
max_num = 10

# set the number of attempts to guess the number
attempts = 3

# welcome the user
print("Welcome to the Higher or Lower game!")

# loop the game the number of times specified in attempts
for i in range(attempts):
    # prompt the user to make a guess
    guess = int(input("Guess a number between {} and {}: ".format(min_num, max_num)))
    # check if the number is higher or lower than the random number
    if guess > num:
        print("Your guess is too high!")
    elif guess < num:
        print("Your guess is too low!")
    else:
        print("You guessed it correctly!")
        break

# notify the user if they failed to guess correctly
if guess != num:
    print("Sorry, you didn't guess the number correctly!")