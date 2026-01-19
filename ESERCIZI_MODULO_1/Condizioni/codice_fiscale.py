"""Caso d'uso: Applicazioni burocratiche
Traccia: Genera le prime 6 lettere del codice fiscale (cognome + nome):
 Cognome: prime 3 consonanti. Se non bastano, aggiungi vocali.
 Nome: se ha 4+ consonanti prendi la 1a, 3a, 4a. Altrimenti come cognome.
Esempio:
Input: Nome="Mario", Cognome="Rossi"
Cognome: R, S, S -> "RSS"
Nome: M, R -> solo 2 consonanti, aggiungo vocali -> "MRA"
Output: "RSSMRA"
Concetti: manipolazione stringhe avanzata, cicli, condizioni"""

nome, cognome = input("Inserisci nome e cognome: ").split()
codice_fiscale = ""

cognome_cons = ""
cognome_voc  = ""

nome_voc  = ""
nome_cons = ""

for lettera in cognome:
    if lettera.lower() in "aeiou":
        cognome_voc += lettera
    else:
        cognome_cons += lettera

for lettera in nome:
    if lettera.lower() in "aeiou":
        nome_voc += lettera
    else:
        nome_cons += lettera

if len(cognome_cons) >= 3:
    codice_fiscale += cognome_cons[:3]
else:
    codice_fiscale += cognome_cons + cognome_voc
    codice_fiscale = codice_fiscale[:3]

if len(nome_cons) >= 3:
    codice_fiscale += nome_cons[:3]
else:
    codice_fiscale += nome_cons + nome_voc
    codice_fiscale = codice_fiscale[:6]

print(f"Il codice fiscale è ", codice_fiscale)