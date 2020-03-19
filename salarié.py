from filiale import *

class salarie:
    def __init__(self,Nom,Prenon,salaire,id):
        self._Nom = Nom
        self._Prenon = Prenon
        self._salaire = salaire
        self._id = id


    def getNom(self):
        return self._Nom

    def getPrenon(self):
        return self._Prenon

    def getSalaire(self):
        return self._salaire

    def getId(self):
        return self._id

    def afficher(self):
        pass
