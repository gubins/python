from datetime import datetime

class Persona():
    def __init__(self,nom,primer,segon,genere,datan):
        self.nom=nom
        self.primer=primer
        self.segon=segon
        self.genere=genere
        self.datan=datan

    def catsalut(self):
        vgen=1        
        if self.genere.upper()=="M":
            vgen=0
        catsalut=(self.primer[:2]+self.segon[:2]+str(vgen)+self.datan[:2]+self.datan[2:]).upper()
        print(catsalut)

jo=Persona("David","Gubern","Magem","m","03/05/1976")

print(jo.datan)

jo.catsalut()
