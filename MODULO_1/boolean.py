#Esercizio 1
anni = int(input("Quanti anni hai? "))
patente = input("Hai la patente? ") == "si"
guida = anni >= 18 and patente
print(guida)


#Esercizio 2
ritardo = True
premium = False

print(not ritardo or premium)