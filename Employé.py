from salarié import *

class employe(salarie):
    def __init__(self,Nom,Prenon,salaire,id,AnneeEmbauche,NbreJourTravail):
        salarie.__init__(self,Nom,Prenon,salaire,id)
        self._AnneeEmbauche = AnneeEmbauche
        self._NbreJourTravail = NbreJourTravail

    def afficher(self):
        pass
