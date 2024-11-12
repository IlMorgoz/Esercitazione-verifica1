import sys
def media_punteggio_competizioni(tupla):
    media=[]
    for chef,piatto,punteggio,giudici in tupla:
        media.append(punteggio)
    if(len(media)>0):
        return (sum(media)/len(media))
    else:
        print("Media dei punteggi non disponibile")
        sys.exit()#termina il programma

def media_punteggio_chef(tupla,cuoco):
    media=[]
    for chef,piatto,punteggio,giudici in tupla:
        if cuoco==chef:
            media.append(punteggio)
    if(len(media)>0):
        return (sum(media)/len(media))
    else:
        print(f"Media dei punteggi non disponibile per {cuoco}")
        sys.exit()

def competizione_con_più_giudici(tupla):
    maggiore=[]
    judges=[]
    for chef,piatto,punteggio,giudici in tupla:
        judges.append(giudici)
    massimo=max(judges)
    for chef,piatto,punteggio,giudici in tupla:
        if giudici==massimo:
            maggiore.append((chef,piatto,punteggio,giudici))
    return tuple(maggiore)

def competizione_con_meno_giudici(tupla):
    minore=[]
    judges=[]
    for chef,piatto,punteggio,giudici in tupla:
        judges.append(giudici)
    minimo=min(judges)
    for chef,piatto,punteggio,giudici in tupla:
        if giudici==minimo:
            minore.append((chef,piatto,punteggio,giudici))
    return tuple(minore)

tupla_competizioni = (
    ("barbieri", "Abbacchio", 8.5, 5),
    ("cannavacciuolo", "Risotto al vino rosso, speck e radicchio", 7.2, 4),
    ("ramsay", "Beef Wellington", 9.0, 6),
    ("barbieri", "Maiale in agrodolce ", 7.8, 5),
    ("cannavacciuolo", "Arrosto di vitello all'arancia", 8.1, 4),
)

while(True):
    scelta=int(input("Benvenuto, cosa desideri fare?\n1 - Media dei punteggi delle competizioni\n2 - Media dei punteggi di un singolo chef\n3 - Trova le competizioni valutate da più giudici\n4 - Trova le competizioni valutate da meno giudici\n0 - Esci\n"))
    if scelta not in range(0,5):
        print("Scelta invalida si prega di reinserire")
    else:
        if scelta==1:
            print(f"\nMedia di tutti i punteggi: {media_punteggio_competizioni(tupla_competizioni):.2f}\n")
        elif scelta==2:
            chef=str(input("Inserire lo chef da controllare\n")).lower()
            print(f"\nMedia dei punteggi di chef {chef}: {media_punteggio_chef(tupla_competizioni,chef):.2f}\n")
        elif scelta==3:
            print(f"\nValutazioni con più giudici: {competizione_con_più_giudici(tupla_competizioni)}\n")
        elif scelta==4:
            print(f"\nValutazioni con meno giudici: {competizione_con_meno_giudici(tupla_competizioni)}\n")
        else:
            print("\nGrazie per avere usato il programma\n")
            sys.exit()