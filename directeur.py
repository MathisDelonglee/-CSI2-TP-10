from salarié import *

class directeur(salarie):
    def __init__(self,Nom,Prenon,salaire,id,AnneeNomination):
        salarie.__init__(self,Nom,Prenon,salaire,id)
        self.__AnneeNomination = AnneeNomination

    def afficher(self):
        print("* [id=",self.getId(),"] Nom et prénon :", self.getNom(),self.getPrenon(),", Salaire :",self.getSalaire(),", Statut : Directeur, Année de nomination :",self.__AnneeNomination)
