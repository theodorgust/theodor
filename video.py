is_male = input("skriv ditt kön man/kvinna/annat :")
is_tall = float((input("skriv din längd :")))

if is_male == "man":
    is_male = True
else:
    is_male = False
if is_tall >= 180:
    is_tall = True
elif is_tall:
    is_tall = is_tall
elif is_tall < 160:
    is_tall = False


if is_male and is_tall:
    print("you are a male and tall")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
elif is_male and is_tall == is_tall:
    print("you are male and averge height")
elif not(is_male) and is_tall == is_tall:
    print("you are not a male but averge height")
else:
    print("you are not a male or tall")