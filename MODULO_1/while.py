#esercizio uno
numero= -1

while numero  <= 0:
   numero=int(input("Inserisci un numero positivo"))

print(f"Hai inserito il numero positivo {numero}")

#esercizio due
numero = 123456789
somma=0

while numero != 0:
    print(numero%10,numero // 10)
    somma += numero % 10
    numero= numero // 10

print(somma)