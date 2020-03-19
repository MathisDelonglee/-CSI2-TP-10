from entreprise import *
from salarié import *

class filiale:
    def __init__(self,Nom,Pays,DateCreation):
        self._Nom = Nom
        self._Pays = Pays
        self._DateCreation = DateCreation
        self._ListeSalarie=[]

    def getDateCreation(self):
        return self._DateCreation

    def getPays(self):
        return self._Pays

    def getNom(self):
        return self._Nom

    def getListeSalarie(self):
        return self._ListeSalarie

    def getNbreSalarie(self):
        return len(self._ListeSalarie)

    def ajoutersalarie(self,Salarie):
        self._ListeSalarie.append(Salarie)

    def supprimersalarie(self,Salarie):
        self._ListeSalarie.remove(Salarie)

    def afficher(self):
        for i in self._ListeSalarie:
            i.afficher()
            print("Site :",self._Pays)
