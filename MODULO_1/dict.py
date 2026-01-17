studente = {"nome" : "Matteo", "età" : "26", "corso" : "Epicode"}

studente["età"] = 27
studente["matricola"] = 123456
print(f"Non presente: {studente.get("asdadas", "non presente")}")

for key, item in studente.items():
    print(key, item)