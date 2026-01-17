colori = ("Viola" , "Giallo", "Viola")
trovato = False

print(f"Il primo e l'ultimo colore della tupla sono rispettivamente il {colori[0]} e {colori[-1]}")

for colore in set(colori):
    print(f"Il colore {colore} è comparso {colori.count(colore)} volte")
                
