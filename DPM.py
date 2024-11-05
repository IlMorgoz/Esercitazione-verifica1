pioggia_lombardia=( ("milano",[("Gennaio",45),("Febbraio",36),("Marzo",52),("Aprile",44),("Maggio",25),("Giugno",12),("Luglio",8),("Agosto",4),("Settembre",28),("Ottobre",42),("Novembre",56),("Dicembre",50)]),
                    ("varese",[("Gennaio",40),("Febbraio",41),("Marzo",35),("Aprile",47),("Maggio",34),("Giugno",8),("Luglio",2),("Agosto",5),("Settembre","N/D"),("Ottobre",41),("Novembre",47),("Dicembre",61)]),
                    ("lecco",[("Gennaio","N/D"),("Febbraio",45),("Marzo",59),("Aprile",41),("Maggio",33),("Giugno",21),("Luglio",11),("Agosto",0),("Settembre",34),("Ottobre",56),("Novembre",80),("Dicembre",44)]))
def media_estremi(citta):
    if citta not in pioggia_lombardia:
            return("Città non disponibile")
    mediaSum=0
    massimo=-1
    minimo=9999999999
    contaMesi=12
    mesiUp=[]
    mesiDown=[]
    for city,*records in pioggia_lombardia:  
        if city==citta:    
            for i in records:
                for mese,valore in i:
                    if (type(valore)==str):
                        contaMesi-=1
                    else:
                        mediaSum+=valore
                        if valore>massimo:
                            mesiUp=[]
                            mesiUp.append(mese)
                            massimo=valore
                        elif valore==massimo:
                            mesiUp.append(mese)
                        elif valore<minimo:
                            mesiDown=[]
                            mesiDown.append(mese)
                            minimo=valore
                        elif valore==minimo:
                            mesiDown.append(mese)
    if(contaMesi==0):
        return("Dati non disponibili")
    else:
        output=[mediaSum/contaMesi,(massimo,mesiUp),(minimo,mesiDown)]
        return tuple(output)
citta=str(input("Inserire la città da analizzare ")).lower()
print(media_estremi(citta))