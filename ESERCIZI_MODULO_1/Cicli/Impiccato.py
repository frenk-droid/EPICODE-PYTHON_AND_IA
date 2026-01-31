"""Caso d'uso: Gioco classico
Traccia: Implementa il gioco dell'impiccato:
 Scegli una parola casuale da una lista
 Mostra la parola nascosta con underscore: _ _ _ _
 L'utente indovina una lettera alla volta
 Mostra le lettere gia provate
 Massimo 6 errori prima di perdere
Concetti: liste, stringhe, set (per lettere provate), while, for"""

import random
parole = ["velociraptor", "programmazione", "impiccato", "python", "dinosauro"]
parola = random.choice(parole)

parola_tracciamento = parola
lettere_provate = set({})
errori = 0
vittoria = False
parola_attuale = ""
parola_bck = parola
#inizializza parola attuale
for i in parola:
    parola_attuale += "_ "    

while True:
    
    print(parola_attuale)
    print("Lettere Provate" , ','.join(c for c in lettere_provate))
    lettera = input("Inserisci la parola per indovinare oppure la lettera: ")
    if len(lettera) > 1:
        # caso parola
        if lettera == parola:
            vittoria = True
            break
        else:
            if errori == 5:
                vittoria = False
                break
            else:
                print("Hai sbagliato parola")
                errori +=1
    else:
        

        if lettera in parola:
           
            if lettera in lettere_provate:
                print("Errore, hai già provato la lettera!")
                errori += 1
            else:
               
                indici = set({})
                while parola_bck.find(lettera) >= 0:
                    indice = parola_bck.find(lettera)
                    indici.add(indice)
                    parola_bck= parola_bck[:indice]+"_"+ parola_bck[indice+1:]

                for i in indici:
                    parola_attuale = parola_attuale[:i*2] + lettera + " " + parola_attuale[i*2+2:]
                
                vittoria = all(c == "_" for c in parola_bck)
                if vittoria: break
        else:
            print("Errore, la lettera non è presente")
            errori += 1
        
        lettere_provate.add(lettera)
        if errori == 5:
            vittoria = False
            break   


if vittoria:
    print("Hai vinto")
else:
    print("Hai perso")