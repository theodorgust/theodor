import math

print("Bråk ett")
num1 = int(input("skriv en täljare:"))
num2 = int(input("skriv en nämnare:"))
print(num1, "\n" "--" "\n", num2)
print("Bråk två")
num3 = int(input("skriv en täljare:"))
num4 = int(input("skriv en nämnare:"))
print(num3, "\n" "--" "\n", num4)
print("Bråk tre")
num5 = int(input("skriv en täljare:"))
num6 = int(input("skriv en nämnare:"))
print(num5, "\n" "--" "\n", num6)
taljare = (num1*num4*num6)+(num3*num2*num6)+(num5*num2*num4)
namnare = num2*num4*num6

print("\n resultat")
gcd = math.gcd(taljare, namnare)
print(taljare/gcd, "\n" "---" "\n", namnare/gcd)