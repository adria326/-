Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("q1) do you like dawn or dusk?")
print("1) dawn")
answer = int(input(""))

if answer == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif answer == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    PRINT("wrong input")
    
print("q2) when i\'m dead i want people to rremenber me as:")
print(q"1) the good")
print("2) the great")
print("3) the wise")
print("4) the bold")
answer = int(input(""))

if answer ==1:
    Hufflepuff +=2
elif answer == 2:
    Slytherin +=2
elif answer == 3:
    Ravenclaw +=2
elif answer == 4:
    Gryffindor +=2
else:
    print("wrong input")
    
print("q3) wich kind of instrument most pleases your ear?")
print("1) the violin")
print("2) the trumpet")
print("3) the piano")
print("4) the drum")
answer = int(input(""))

if answer == 1:
    Slytherin += 4
elif answer == 2:
    Hufflepuff += 4
elif answer == 3:
    Ravenclaw += 4
elif answer == 4:
    Gryffindor +=4
else:
    print("wrong input")
    
houses = [Gryffindor, Ravenclaw, Slytherin, Hufflepuff]
if max(house) == Gryffindor:
    print("your house is Gryffindor")
elif max(houses) == Ravenclaw:
    print("your house is Ravenclaw")
elif max(houses) == Slytherin:
    print("your house is slytherin")
elif max(houses) == Hufflepuff:
    print("your house is Hufflepuff")