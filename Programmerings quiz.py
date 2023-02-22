num1 = float(input("skriv ett nummer: "))
num2 = float(input("skriv ett nummer till: "))
num3 = float(input("skriv ett nummer till: "))

list1 = [num1, num2, num3]
list2 = []

while list1:
    n = list1[0]
    for x in list1:
        if x < n:
                n = x
    list2.append(n)
    list1.remove(n)

print(list2)

print([num1, num2, num3] + list2)