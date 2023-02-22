import random
n = input("SLUMPMÄSSIGT NUMMER MELLAN 1 TILL: " )


secret_num = random.randint(1, int(n))
guess = " "
guess_count = 0
guess_limit = int(input("ANGE ANTAL GISSNINGAR DU VILL HA: "))
out_of_guesses = False
print("\nHIGHER OR LOWER GAME")
print("\n" + "DU HAR "+ str(guess_limit) + " FÖRSÖK!")
int(guess_limit)
while guess != secret_num and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = int(input("\n ANSWER: "))
        guess_count += 1
    else:
        out_of_guesses = True
    if secret_num > guess:
        print("HIGHER \n" + str(guess_count) + " GUESSES")
    elif secret_num < guess:
        print("LOWER \n" + str(guess_count) + " GUESSES")
if out_of_guesses:
    print("\nYOU LOSE!" )
    print("THE NUMBER WAS " + str(secret_num))
else:
    print("\nYOU WIN!")
print("YOU GUESSED " + str(guess_count) + " TIMES")
