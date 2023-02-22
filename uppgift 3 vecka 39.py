def max_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return "Det minsta numert är " + num1
    elif num2 <= num1 and num2 <= num3:
        return "Det minsta numert är " + num2
    elif num3 <= num1 and num3 <= num2:
        return "Det minsta numert är " + num3

print(max_num(input("Skriv ett nummer: "), input("Skriv ett till nummer: "), input("Skriv ett sista nummer: ")))
