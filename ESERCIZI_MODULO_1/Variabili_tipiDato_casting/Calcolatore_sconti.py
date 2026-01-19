"""""
Caso d'uso: E-commerce
Traccia: Scrivi un programma che:
1 Chiede il prezzo di un prodotto
2 Chiede la percentuale di sconto
3 Calcola e mostra il prezzo finale e il risparmio
4 Gestisce l'errore se l'utente inserisce testo invece di numeri (try/except)
Esempio:
Input: Prezzo 80, Sconto 25%
Output: "Prezzo finale: 60.00 EUR (Risparmi: 20.00 EUR)"
Concetti: casting, try/except, calcoli percentuali, formattazione decimali
"""

try:
    prezzo_prodotto = int(input("Quanto costa questo prodotto? "))
    sconto_prodotto = int(input("Di quanto è lo sconto? ").replace("%", ""))
    print(f"Prezzo finale: {prezzo_prodotto - prezzo_prodotto*sconto_prodotto/100} (Risparmi: {prezzo_prodotto*sconto_prodotto/100} EUR)")
except ValueError:
    print("Inserisci solo caratteri numerici!")





