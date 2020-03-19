from filiale import *
from salarié import *

class entreprise:
    def __init__(self,Nom,PaysOrigine):
        self.__Nom = Nom
        self.__PaysOrigine = PaysOrigine
        self.__ListeFiliale = []

    def setNom(self,Nom):
        self.__Nom = Nom

    def setPaysOrigine(self,PaysOrigine):
        self.__PaysOrigine = PaysOrigine

    def getNom(self):
        return self.__Nom

    def getPaysOrigine(self):
        return self.__PaysOrigine

    def getListeFiliale(self):
        return self.__ListeFiliale

    def ajouter(self,Filiale):
        self.__ListeFiliale.append(Filiale)

    def afficher(self):
        print("- La multinationale",self.__Nom,"est composé de",len(self.__ListeFiliale),"filiales. Son pays d'origine est la",self.__PaysOrigine,".")
        liste=[]
        compteur=0

        for i in self.__ListeFiliale:
            liste.append(i.getDateCreation())

        liste2 = sorted(liste)
        i=0
        while liste2[0]!=liste[i]:
            i = i + 1

        Nom = self.__ListeFiliale[i].getNom()
        Pays = self.__ListeFiliale[i].getPays()
        liste = self.__ListeFiliale[i].getNbreSalarie()

        Stotale = 0

        for i in self.__ListeFiliale:
            Stotale += i.getNbreSalarie()

        print("- La filiale la plus ancienne de cette multinationale de",self.__PaysOrigine,"est :",Nom,". Elle est composé de ",liste,"employés.")
        print("-",self.__Nom,"est composé de ",Stotale,"salariés :")

        for i in self.__ListeFiliale:
            i.afficher()
