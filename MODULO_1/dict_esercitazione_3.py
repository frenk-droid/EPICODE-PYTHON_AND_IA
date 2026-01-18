d = {"a" : 1, "b" : 2, "c" : 3}
inverso = {v:k for k, v in d.items()}
print(inverso)


chiavi = ["nome", "eta", "citte"]
valori = ["Anna", 25, "Roma"]

dict = dict(zip(chiavi, valori))
print(dict)

parola = ["ciao", "come", "va", "oggi"]
gruppi = {}

for p in parola:
    gruppi.setdefault(len(p), []).append(p)
print(gruppi)


#metodo 1
testo = "programmazione"
frequenza = {}

for lettera in testo:
    frequenza.setdefault(testo.count(lettera), []).append(lettera)

print(frequenza)

#metodo 2
testo = "programmazione"
frequenza = {}

for lettera in testo:
    frequenza[lettera] = frequenza.get(lettera, 0) + 1
print(frequenza)