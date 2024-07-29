height = int(input("what is your height (cm)? "))
credits = int(input("how many credits do you have? "))
if height >= 137 and credits >= 10:
    print("¡disfruta el viaje!")
elif credits >= 10:
    print("no eres lo suficiente alto para viajar")
elif height >=137:
    print("no tienes suficientes creditos")
else:
    print("no cumples ninguno de los requisitos")
    