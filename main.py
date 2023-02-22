import random
# random
#1
for i in range(10):
    print(str(random.randint(30, 50)))
#2
for i in range(5):
    print(str(random.uniform(1, 10)))
#3
for i in range(7):
    print(str(random.gauss(50, 25)))
#4
list1 = []
for i in range(5):
   list1.append(random.randint(1, 10))
for i in range(5):
   print(random.sample(list1, 2))
print(list1)
#break
#1
n = 1
while n < 100:
    print(n)
    n += 1
    if n > 50:
        break
#try/except
#1
string = input("skriv ett ord: ")
integer = int(input("skriv ett nummer: "))
try:
    print(string + integer)
except:
    print("cannot print int and string")
#2
try:
    print(4/0)
except ZeroDivisionError:
    print("error")

#files

#1
try:
    file = open("kdp.txt", "x")
except:
    print("filen finns redan")


#2
file = open("kdp.txt", "r")
fileread = file.read()
print(fileread)

#3
try:
    file2 = open("ftp.txt", "x")
except:
    print("")

#4

file2 = open("psycho", "w")#man öppnar filen för write
file2.write(input("skriv en mening: "))#usern skriver in en mening
file2 = open("psycho", "r")#man öppnare filen för read
print(file2.read())#programmet läser filen
