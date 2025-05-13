import math
class Pagelle:
    def __init__(self,vettore):
        self.vettore=vettore
        
    def __repr__(self):
        return str(self.vettore)
    
    def media(self):
        return sum(a for a in self.vettore)/len(self.vettore)
    
    def __getitem__(self,index):
        return self.vettore[index]
    
    def __eq__(self,altroVettore):
        if(len(self.vettore))!=len(altroVettore.vettore):
            print("Le pagelle hanno un numero diverso di materie e non possono essere confrontate")
        else:
            for i in range(len(self.vettore)):
                if altroVettore[i]!=self.vettore[i]:
                    return False
            return True
    
    def __sub__(self,altroVettore):
        if(len(self.vettore))!=len(altroVettore.vettore):
            print("Le pagelle hanno un numero diverso di materie e non possono essere confrontate")
        else:
            nVettore=[]
            for i in range(len(self.vettore)):
                nVettore.append(self.vettore[i]-altroVettore[i])
            return nVettore
    
    def impegno(self):
        return math.sqrt(sum(math.pow(a,2) for a in self.vettore))

p1=Pagelle([2,4,6])
p2=Pagelle([6,7,9])
p3=Pagelle([2,4,6])
p4=Pagelle([6,8])

print(p1)
print(p2)
print(p1.media())
print(p2[1])
print(p1==p2)
print(p1==p3)
print(p2-p1)
print(p4.impegno())