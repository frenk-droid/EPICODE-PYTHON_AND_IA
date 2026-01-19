""" Caso d'uso: Validazione form
Traccia: Scrivi un programma che controlla se una stringa "sembra" un'email valida. Deve contenere:
1 Il carattere @
2 Il carattere . (punto)
3 La @ deve venire PRIMA del punto
Esempio:
"mario@gmail.com" -> Valida
"mario.gmail@com" -> Non valida (@ dopo il punto)
"mariogmail.com" -> Non valida (manca @)
"""

def valida_mail(email):
    return "@" in email and "." in email and email.find("@") < email.find(".")

email = input("Inserisci la mail da validare: ")
if valida_mail(email):
    print("Email valida")
else:
    print("Email non valida")