tupla_vendite = (
                (("RepartoA","Informatica"),("Prodotto A", ("contanti",1000))),
                (("RepartoA","Informatica"),("Prodotto B", ("carta di credito",1500))),
                (("RepartoA","Informatica"),("Prodotto C", ("carta di credito",1200))),
                (("RepartoA","Informatica"),("Prodotto D", ("contanti",200))),
                (("RepartoA","Informatica"),("Prodotto E", ("contanti",800))),
                (("RepartoA","Informatica"),("Prodotto F", ("N/D",200))),
                (("RepartoB","Elettronica"),("Prodotto A", ("contanti",1500))),
                (("RepartoB","Elettronica"),("Prodotto B", ("carta di credito",900)))
                )
def media_globale(tupla):
    sommaMedia=[]
    for i in tupla:
        for tipologia,*oggetto in i:
            print(tipologia,oggetto)
            # for prodotto,*acquisto in oggetto:
            #     for come,prezzo in acquisto:
            #         sommaMedia.append(prezzo)
    # return sum(sommaMedia)/len(sommaMedia)


print(media_globale(tupla_vendite))