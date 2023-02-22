#uppgift 1

#1
list1 = ["jack", "erik", "leo", "abdi", "tony"]

#2
list2 = list1.copy()

#3
list2.reverse()

#4
element1 = list2[0]

#5
list1.insert(2, element1)

#6
list1.count(element1)

#uppgift 2

#1
list3 = [1, 2, 3, 4, 5]
print(list3)

#2
list3.append(6)
print(list3)
#append lägger till ett element till slutet av listan
list4 = [7, 8, 9]
list3.extend(list4)
print(list3)
#extend lägger till en till lista in i list3

#3
#pop() tar bort ett element i en specifik position
print(list3)
list3.pop(1)
print(list3)
#remove tar bort första instansen av elementet man har skrivit
print(list3)
list3.remove(5)
print(list3)

#4
print(len(list3))

print(list3.count(1) + list3.count(3) + list3.count(4) + list3.count(6) + list3.count(7) + list3.count(8) + list3.count(9))
