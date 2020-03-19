from Employé import *

class administrateur(employe):
    def __init__(self,Nom,Prenon,salaire,id,AnneeEmbauche,NbreJourTravail,Service):
        employe.__init__(self,Nom,Prenon,salaire,id,AnneeEmbauche,NbreJourTravail)
        self._service = Service

    def afficher(self):
        print("* [id=",self.getId(),"] Nom et prénon :", self.getNom(),self.getPrenon(),", Salaire :",self.getSalaire(),", Statut : Ingénieur Junior, Annee d'embauche :",self._AnneeEmbauche,"Nombre Jour de travail :", self._NbreJourTravail,", Service :", self._service)
