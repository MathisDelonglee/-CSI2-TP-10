from Employé import *

class ingenieur(employe):
    def __init__(self,Nom,Prenon,salaire,id,AnneeEmbauche,NbreJourTravail,NbreHProjet,NbreHGestion):
        employe.__init__(self,Nom,Prenon,salaire,id,AnneeEmbauche,NbreJourTravail)
        self._HProjet = NbreHProjet
        self._HGestion = NbreHGestion

    def afficher(self):
        pass
