try:
    x = int(input("Please enter a number: "))
except ValueError:
    print("Oops!  That was not a valid number.  Try again...")
    input("try again: ")
else:
    print("nothing went wrong")
finally:
    print("done")
#om du skriver in en int kommer den printa nummret. Men om du skriver något annat kommer den printa det som står under except
