rubrica = []

def aggiungi_contatto(nome, numero, email):
    contatto = {"nome" : nome, "numero" : numero, "email" : email}
    rubrica.append(contatto)
    print(f"Contatto {nome} aggiunto")

def modifica_contatto(nome, nuovo_numero= None, nuova_email= None):
    for contatto in rubrica:
        if contatto["nome"].lower() == nome.lower():
            contatto["numero"] = nuovo_numero
            contatto["email"]  = nuova_email
            print(f"Contatto {nome} modificato correttamente")
            return
        else:
            print(f"Contatto {nome} non trovato in rubrica")

def cerca_contatto(nome = None):
    contatto_trovato = None
    if nome != None:
        for contatto in rubrica:
            if contatto["nome"].lower() == nome.lower():
                contatto_trovato= contatto

    return contatto_trovato

def elimina_contatto(nome = None):
    for contatto in rubrica:
        if contatto["nome"].lower() == nome.lower():
            rubrica.remove(contatto)
            print(f"Contatto {nome} eliminato")
            return

def mostra_contatti():
    if not rubrica:
        print("Rubrica vuota")
        return
    
    ordinati = sorted(rubrica, key= lambda x: x["nome"].lower())

    for contatto in ordinati:
        print(contatto)


aggiungi_contatto("Matteo", "34502014749", "teofrenk99@gmail.com")
aggiungi_contatto("Mattia", "12345674894", "mattia.pavin@gmail.com")

mostra_contatti()

modifica_contatto("Matteo", "12546894123", "matteo.franchi@teaminformatica.ch")
cerca_contatto("Mattia")
elimina_contatto("Mattia")
mostra_contatti()
