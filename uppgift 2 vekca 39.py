import math
#uppgift 2 vecka 39
#1
num1 = int(input("skriv ett nummer"))
num2 = float(input("skriv ett till nummer"))
#2
print(float(num1))
print(int(num2))
#3
print(math.ceil(25.11))
print(math.floor(25.11))
#ceil avrundar upp och floor avrundar ner. Man kan tänkta att ceil är ceiling/taket och floor är golvet
#4
num1 = int(num1)
num2 = int(num2)
gcd1 = math.gcd(num1)
gcd2 = math.gcd(num2)
print(gcd1)
print(gcd2)
#5
print("cirkel omkrets")
r = 10
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
cirkel_omkrets = (r+r)*pi
print(cirkel_omkrets)