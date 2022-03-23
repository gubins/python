from datetime import datetime

class Persona():
    def __init__(self,nom,primer,segon,genere,datan):
        self.nom=nom.upper()
        self.primer=primer.upper()
        self.segon=segon.upper()
        self.genere=genere.upper()
        self.datan=datan

    def CIP(self):
        vgen=1        
        if self.genere.upper()=="M":
            vgen=0
        CIP=(self.primer[:2]+self.segon[:2]+str(vgen)+self.datan[-2:]+self.datan[3:5:1]+self.datan[:2]).upper()
        print(CIP)
        cip2=ord(self.primer[:1])&ord(self.primer[2:3:1])&      ord(self.segon[:1])&ord(self.segon[2:3:1])
        cip2=CIP+str("00")+str(int(str(ord(self.primer[:1]))+str(ord(self.primer[2:3:1]))+str(ord(self.segon[:1]))+str(ord(self.segon[2:3:1]))+str(vgen)+self.datan[-2:]+self.datan[3:5:1]+self.datan[:2]+"00")%9)
        print(cip2)



jo=Persona("Nom","Primer","Segon","m","25/06/2020")
print(jo.datan)

jo.CIP()
