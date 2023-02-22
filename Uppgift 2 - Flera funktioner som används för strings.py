sentance = input("skriv en mening: ")

length = len(sentance.split())
print(length)

sista_a = sentance.rfind("a")
print(sista_a)

punkt = sentance.count(".")
if punkt == 1:
    print("meningen har punkt")
elif punkt == 0:
    print("meningen har ingen punkt")