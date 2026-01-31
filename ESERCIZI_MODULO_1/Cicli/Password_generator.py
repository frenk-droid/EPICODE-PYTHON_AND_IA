"""Caso d'uso: Sicurezza informatica
Traccia: Genera una password casuale che contenga:
 Lunghezza specificata dall'utente (minimo 8)
 Lettere maiuscole e minuscole
 Numeri
 Simboli speciali (!@#$%&*)
Suggerimento: Usa il modulo string (string.ascii_letters, string.digits, etc.)
Concetti: random.choice(), string module, cicli, concatenazione"""
import string
import random 

lunghezza_utente = int(input("Inserisci la lunghezza della password: "))
password=""
caratteri_speciali= string.punctuation
caratteri_maiuscoli= string.ascii_uppercase
caratteri_minuscoli= string.ascii_lowercase
numeri = string.digits

caratteri = string.ascii_letters + string.digits + caratteri_speciali

while True:
    password = ''.join(random.choice(caratteri) for c in range(lunghezza_utente))

    car_m = any(c.islower() for c in password)
    car_M = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    speci = any(c in caratteri_speciali for c in password)

    if car_m and car_M and digit and speci:
        break

print("La password scelta è ", password)

