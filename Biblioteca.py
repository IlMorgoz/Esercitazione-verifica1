class Libro:
    def __init__(self, titolo, autore, anno, isbn):
        self.titolo=titolo
        self.autore=autore
        self.anno=anno
        self.isbn=isbn
        
    def __str__(self):
        return f"{self.titolo} di {self.autore} ({self.anno}) - ISBN: {self.isbn}"


class Biblioteca:
    def __init__(self):
        self.lista=[]

    def aggiungi_libro(self, libro):
        self.lista.append(libro)

    def rimuovi_libro(self, isbn):
        for libro in self.lista:
            if libro.isbn==isbn:
                self.lista.remove(libro)
                print("Libro eliminato")
                return 0
        print("Libro non trovato")

    def elenco_libri(self):
        print("Libri presenti in biblioteca:")
        for libro in self.lista:
            print(libro)

    def cerca_libro(self, isbn):
        for libro in self.lista:
            if libro.isbn==isbn:
                return libro

biblioteca=Biblioteca()
def check_isbn():
    while(True):
        isbn=str(input("Inserisci l'ISBN del libro "))
        if len(isbn)!=13:
            print("ISBN incorretto. Si prega di reinserire")
            continue
        else:
            return isbn

while(True):
    scelta=int(input
        ("""
        Ciao!
        Benvenuto nel gestionale della biblioteca. Cosa vuoi fare?
        1 - Inserisci un libro
        2 - Rimuovi un libro
        3 - Stampa l'elenco dei libri
        4 - Cerca un libro
        5 - Esci
        
        """))
    if 0>scelta or scelta>5:
        print("Scelta invalida. Si prega di ripetere ")
    elif scelta==1:
        nome=str(input("Inserisci il nome del libro "))
        autore=str(input("Inserisci il nome dell'autore "))
        while(True):
            anno=int(input("Inserisci l'anno di pubblicazione "))
            if 1200<anno<2025:
                break
            else:
                print("Data non disponibile del database. Si prega di reinserire")
        isbn=check_isbn()
        biblioteca.aggiungi_libro(Libro(nome,autore,anno,isbn))
    elif scelta==2:
        isbn=check_isbn()
        biblioteca.rimuovi_libro(isbn)
    elif scelta==3:
        biblioteca.elenco_libri()
    elif scelta==4:
        isbn=check_isbn()
        print(biblioteca.cerca_libro(isbn))
    else:
        print("Grazie e arrivederci")
        break