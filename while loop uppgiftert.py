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

print("\n Tack!")
#uppgift 3
guess_count = 0
guess_limit = 3
out_of_guesses = False
secret num
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("you lose!")
else:
    print("you win!")