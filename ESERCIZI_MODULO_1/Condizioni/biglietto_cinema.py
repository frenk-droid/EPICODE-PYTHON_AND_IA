""""Caso d'uso: Sistema di biglietteria
Traccia: Calcola il prezzo del biglietto in base a:
1 Eta: bambini (<12): 5 EUR, adulti: 10 EUR, anziani (>65): 7 EUR
2 Giorno: se martedi, sconto 20% per tutti
3 Formato: se 3D, aggiungi 3 EUR
Esempio:
Input: eta=25, giorno="martedi", 3D=True
Calcolo: 10 EUR - 20% = 8 EUR + 3 EUR = 11 EUR
Output: "Totale: 11.00 EUR"""


eta = int(input("Inserisci la tua età: "))
giorno = input("Inserisci che giorno è oggi: ")
tre_d_str = input("Il film è in 3d (S/N)? ")
tre_d = False
prezzo = 0

if tre_d_str.lower() == "s":
    tre_d = True

if eta < 12:
    prezzo = 5
elif eta < 65:
    prezzo = 10
else:
    prezzo = 7

if giorno.lower() == "martedì":
    prezzo = prezzo - 0.2 * prezzo

if tre_d:
    prezzo += 3

print("Il costo del biglietto è di ", prezzo)



