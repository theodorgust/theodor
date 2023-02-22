matejLängd= 180
matejÅlder= 20
matejSkola= True
gkLängd=178
gkÅlder= 16
gkSkola = True
kenLängd = 130
kenÅlder = 22
kenSkola = False
print(matejÅlder, gkÅlder, kenÅlder)
print(matejLängd, gkLängd, kenLängd)
print(matejSkola, gkSkola, kenSkola)


def funktion1(x, y):  # den tar in två värden
  a = x * y + y  # den sparar en variabel som är då x*y+y
  return a  # den returnar variabeln som är sparad


def funktion2(x, y):  # den tar in två värden
  print(x + y)  # den räknar ut summan av de två värdena


import numpy as np


def funktion3(a, b):  # den tar in två värden
  c = np.sqrt(
    a * a + b * b)  # den tar värde ett gånger sig själv + värde två gånger sig själv. Sedan tar han roten ur på produkten
  return c


def funktion(x, y, z):  # tar in tre värden
  n = x * y  # multiplicerar de två första värden
  a = n * z  # tar produkten gånger det sista värdet
  return a  # returnar produkten


x = input("skriv ett ord: ")#tar in en stringfrån användaren
n = len(x) # räknar ut längden på ordet/stringen
print("ditt ord är " + str(n) + " bokstäver långt")#printar ut hur lång den är



def miniräknare(num1, operator, num2):
  if operator == +:
    return num1+num2
  elif operator == -:
    return num1-num2
  elif operator == /:
    return num1/num2
  elif operator == *:
    return num1*num2
print(miniräknare(4, /, 5))
