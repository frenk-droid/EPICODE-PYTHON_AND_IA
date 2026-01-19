"""
Caso d'uso: Form di registrazione
Traccia: Scrivi un programma che chiede all'utente il suo anno di nascita e:
1 . Calcola quanti anni ha attualmente
2 . Calcola in che anno compira 100 anni
Esempio:
Input: 1995
Output: "Hai 30 anni. Compirai 100 anni nel 2095!"
Concetti: input(), int(), operazioni aritmetiche, f-string
"""

anno_nascita = int(input("In che anno sei nato? "))
print(f"Attualmente hai {2026 - anno_nascita}")
print(f"Compirai 100 anni l'anno {anno_nascita + 100}")