#ruotare a destra di k posizioni

lista_normale = [1, 2, 3, 4, 5, 6]
lista_ruotata = []
k = 3

lista_ruotata = lista_normale[k:] + lista_normale[:k]


print(lista_ruotata)


a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

print([n for n in a if n in b])


tuples = [(1, 2), (3, 4), (5, 6)]
print(f"La somma dei valori è {sum([sum(t) for t in tuples])}")