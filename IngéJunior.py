from ingénieur import *

class ingeJunior(ingenieur):
    def __init__(self,Nom,Prenon,salaire,id,AnneeEmbauche,NbreJourTravail,NbreHProjet,NbreHGestion,NbreAnnExp):
        ingenieur.__init__(self,Nom,Prenon,salaire,id,AnneeEmbauche,NbreJourTravail,NbreHProjet,NbreHGestion)
        self.__NbreAExp = NbreAnnExp

    def afficher(self):
        print("* [id=",self.getId(),"] Nom et prénon :", self.getNom(),self.getPrenon(),", Salaire :",self.getSalaire(),", Statut : Ingénieur Junior, Annee d'embauche :",self._AnneeEmbauche,"Nombre Jour de travail :", self._NbreJourTravail,", Nombre d'heure de projet :",self._HProjet,", Nombre d'heure de gestion :",self._HGestion,", Nombre d'année d'experience :", self.__NbreAExp)
