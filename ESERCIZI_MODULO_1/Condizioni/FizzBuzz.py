""" Caso d'uso: Classico test dei colloqui di lavoro
Traccia: Chiedi un numero all'utente. Poi:
 Se divisibile per 3, stampa "Fizz"
 Se divisibile per 5, stampa "Buzz"
 Se divisibile per entrambi (3 e 5), stampa "FizzBuzz"
 Altrimenti stampa il numero """

numero = int(input("Inserisci un numero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
elif numero % 5 == 0:
    print("Buzz")
elif numero % 3 == 0:
    print("Fizz")
else:
    print("Il numero stampato è ", numero)
