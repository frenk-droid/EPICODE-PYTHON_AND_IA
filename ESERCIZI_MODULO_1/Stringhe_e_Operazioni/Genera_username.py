""""
Caso d'uso: Registrazione social network
Traccia: Scrivi un programma che chiede nome e anno di nascita, poi genera uno username formato
da:
1 Prime 3 lettere del nome (minuscole)
2 Ultime 2 cifre dell'anno di nascita
Esempio:
Input: "Alessandro", 1998
Output: "Il tuo username e': ale98"
"""

nome  = input("Come ti chiami? ")
anno_nascita = input(f"Quando sei nato {nome}? ")

print(f"Il tuo username è {nome[:3] + anno_nascita[2:]}")