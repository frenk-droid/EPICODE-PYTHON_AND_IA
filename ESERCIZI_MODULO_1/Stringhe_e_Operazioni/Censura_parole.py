""""
Caso d'uso: Chat, forum, commenti
Traccia: Data una frase e una lista di parole "vietate", sostituisci ogni parola vietata con asterischi
della stessa lunghezza.
Esempio:
Frase: "Questo film fa schifo, che cavolo di finale"
Vietate: ["schifo", "cavolo"]
Output: "Questo film fa ******, che ****** di finale"
"""

vietate = ["schifo", "cavolo"]
frase = input("Inserisci la frase da censurare: ")

for parola in frase.split():
    print(parola.lower())
    if parola.lower() in vietate:
        print("ok")
        frase = frase.replace(parola, "*" * len(parola))

print("La frase censurata è: ", frase)