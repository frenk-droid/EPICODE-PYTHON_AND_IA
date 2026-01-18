testo = "Python è utilizzato per analisi di dati e sviluppo web; studiare python è divertente e questo è un palese testo fornito dall'esercitatore"

def pulisci_testo(testo):
    simboli = ",.;:!?"
    for s in simboli:
        testo= testo.replace(s, "")
    return testo.lower()

def conta_parole(testo):
    parole = testo.split()
    return len(parole)

def frequenza_parole(testo):
    parole = testo.split()
    frequenza = {}

    for parola in parole:
        frequenza[parola] = frequenza.get(parola, 0) +1

    return frequenza

def parole_uniche(freq):
    return set(freq.keys())

def top_n_parole(freq, n=5):
    return sorted(freq.items(),  key= lambda x : x[1], reverse=True)[:n]

def lunghezza_media(freq):
    tot_caratteri= sum(len(p) * occ for p, occ in freq.items())
    tot_parole = sum(freq.values())
    return tot_caratteri / tot_parole


pulito = pulisci_testo(testo)
print("numero di parole: ", conta_parole(pulito))

freq = frequenza_parole(pulito)
print("Frequenza parole: ", freq)
print("Parole uniche :", parole_uniche(freq))
print("top 5 parole: ", top_n_parole(freq))
print("Lunghezza media: ", round(lunghezza_media(freq)))