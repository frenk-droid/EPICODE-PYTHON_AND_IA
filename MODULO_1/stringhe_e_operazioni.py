frase = input("Inserisci una frase ")
frase_invertita = frase[::-1]
print( f"La tua frase invertita è {frase_invertita}" )

if frase.strip() == frase_invertita.strip():
    print("La frase è palindroma")
else:
    print("La frase non è palindroma")