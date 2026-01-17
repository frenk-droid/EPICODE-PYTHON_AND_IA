corso_a = {"Matteo" , "Mattia", "Fabrizio" , "Anna" , "Riccardo"}
corso_b = {"Mattia", "Dave", "Riccardo", "Francesco", "Mauro"}

print(f"Gli studenti che seguono entrambi i corsi sono {corso_a.intersection(corso_b)}")
print(f"Gli studenti che seguono solo il corso a sono {corso_a - corso_b}")
print(f"Gli studenti che seguono solo il corso B sono{corso_b - corso_a}")
print(f"Gli studenti che seguono almeno un corso sono {corso_a.union(corso_b)}")
print(f"Gli studenti unici in totale sono {len(corso_a.union(corso_b))}")
