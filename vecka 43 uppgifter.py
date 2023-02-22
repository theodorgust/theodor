
#uppgift 1
n = 2
while n <= 20:
    print(n)
    n += 2
#uppgift 2
summa = 0
while summa < 100:
    n = int(input("skriv ett nummer: "))
    summa += n
    print("summan är " + str(summa))
#uppgift 3
guess = (" ")
n = "nej"
while guess != n:
    print("vill du spela?")
    guess = input("svar: ")
print("Jag vill inte spela med dig heller")
#uppgift 4

import random
secret_num = random.randint(1,1000000)
guess_count = 0
guess_limit = 20
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
        print("HIGHER")
    elif secret_num < guess:
        print("LOWER")
if out_of_guesses:
    print("\nYOU LOSE!" )
    print("THE NUMBER WAS" + secret_num)
else:
    print("\nYOU WIN!")
print("YOU GUESSED " + str(guess_count) + " TIMES")
