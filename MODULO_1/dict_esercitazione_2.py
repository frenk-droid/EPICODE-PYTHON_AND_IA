t = (1, 2, 3, 4, 5, 6)
pari = tuple([ x for x in t if x % 2 == 0])
print(pari)


t = (1, 2, 3, 4, 5, 6)
invertita = tuple(reversed(t))
print(invertita)


s = "programmazione"
t = tuple( set(s) )
print(t)