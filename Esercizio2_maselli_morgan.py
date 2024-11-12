import sys
def analizza_produzione_agricola(regione,coltura):
    media=[]
    tempo=[]
    flag1=False
    flag2=False
    for area, *prodotti in tupla_produzione_agricola:
        if area==regione:
            flag1=True
            for produzioni in prodotti:
                for mese, (pianta,quantità) in produzioni:
                    if coltura==pianta:
                        flag2=True
                        tempo.append((mese, (pianta,quantità)))
                        media.append(quantità)
    if flag1==False:
        print("Mese non presente in elenco")
        sys.exit()
    elif flag2==False:
        print("Coltura non presente in elenco")
        sys.exit()
    elif flag1==False and flag2==False:
        print("Mese e coltura non presenti in elenco")
        sys.exit()
    else:
        return tuple((media_produzione(media),(max_produzione(media),mese_max_produzione(media,tempo))))


def media_produzione(array_dati):
    return(sum(array_dati)/len(array_dati))

def max_produzione(array_dati):
    return max(array_dati)

def mese_max_produzione(array_dati1,array_dati2):
    mesi=[]
    massimo= max_produzione(array_dati1)
    for mese, (pianta,quantità) in array_dati2:
        if massimo==quantità:
            mesi.append(mese)
    return mesi

tupla_produzione_agricola = (
    ("toscana", [
        ("gennaio", ("grano", 1200)),
        ("gennaio", ("mais", 900)),
        ("febbraio", ("grano", 1100)),
        ("febbraio", ("mais", 950)),
        ("marzo", ("grano", 900)),
        ("marzo", ("mais", 700)),
        ("aprile", ("grano", 1050)),
        ("aprile", ("mais", 950)),     
    ]),
    ("lombardia", [
        ("gennaio", ("grano", 1300)),
        ("gennaio", ("mais", 850)),
        ("febbraio", ("grano", 1250)),
        ("febbraio", ("mais", 920)),
        ("marzo", ("grano", 1100)),
        ("marzo", ("mais", 950)),
        ("aprile", ("grano", 1100)),
        ("aprile", ("mais", 950)),     
    ]),
    ("sicilia", [
        ("gennaio", ("grano", 1300)),
        ("gennaio", ("mais", 850)),
        ("febbraio", ("grano", 1250)),
        ("febbraio", ("mais", 920)),
        ("marzo", ("grano", 1100)),
        ("marzo", ("mais", 950)),
        ("aprile", ("grano", 1100)),
        ("aprile", ("mais", 950)),     
    ]),
    ("puglia", [
        ("gennaio", ("grano", 1300)),
        ("gennaio", ("mais", 850)),
        ("febbraio", ("grano", 1250)),
        ("febbraio", ("mais", 920)),
        ("marzo", ("grano", 1100)),
        ("marzo", ("mais", 950)),
        ("aprile", ("grano", 1100)),
        ("aprile", ("mais", 950)),     
    ]),
)
regione=str(input("Inserire la regione in prendere sotto esame\n")).lower()
coltura=str(input("Inserire la coltura in prendere sotto esame\n")).lower()
risultato=analizza_produzione_agricola(regione,coltura)
print(f"Risultato per {regione} e {coltura}: {risultato}")