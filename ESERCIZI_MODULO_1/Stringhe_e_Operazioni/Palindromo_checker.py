""""
Caso d'uso: Giochi di parole
Traccia: Verifica se una frase e palindroma (si legge uguale al contrario). Ignora spazi, punteggiatura e differenze maiuscole/minuscole.
Esempio:
"I topi non avevano nipoti" -> Palindromo!
"anna" -> Palindromo!
"ciao" -> Non palindromo
"""

frase = input("Inserisci una frase per controllare se è palindroma: ")
frase_pulita = frase.lower().replace(",", "").replace(":","").replace(";","").replace(" ","")

if frase_pulita[::-1] == frase_pulita:
    print("Palindroma")
else:
    print("Non palindroma")