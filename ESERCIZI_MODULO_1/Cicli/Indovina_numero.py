"""Caso d'uso: Mini-gioco
Traccia:
 Il computer genera un numero casuale da 1 a 100
 L'utente prova a indovinarlo
 Ad ogni tentativo, rispondi "Troppo alto!" o "Troppo basso!"
 Quando indovina, mostra il numero di tentativi
Concetti: while, random.randint(), contatore, break"""

import random

numero_casuale = random.randint(1,100)

while True:
    try:
        numero_utente = int(input("Indovina il numero: "))
        break
    except ValueError:
        print("Inserisci un numero intero!")

while numero_casuale != numero_utente:
    if numero_utente > numero_casuale:
        print("Troppo alto!")
    else:
        print("Troppo basso")
    numero_utente = int(input("Indovina il numero: "))

print("Numero Indovinato!")
    