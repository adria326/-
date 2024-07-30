print("bank of codedex")

pin = int(input("enter your pin:"))

while pin != 1234:
    pin = int(input("incorrect pin. enter your pin again: "))
    
if pin ==1234:
    print("pin accepted!")