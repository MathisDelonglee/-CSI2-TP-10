from entreprise import *
from filiale import *
from salarié import *
from directeur import *
from administrateur import *
from Employé import *
from IngéJunior import *
from IngéSénior import *

Entreprise = entreprise("U-log","France")

#Entreprise.afficher()

F1 = filiale("Super U", "Allemagne",1999)
Entreprise.ajouter(F1)

F2 = filiale("Hyper U","Belgique",1995)
Entreprise.ajouter(F2)

S1 = administrateur("Busquet","Mathieu","5","144","2003","220","comptable")
F2.ajoutersalarie(S1)

S2 = salarie("Julian","Burtin","5","145")
F1.ajoutersalarie(S1)

D = directeur("Martin",'Ascouet',"10","001","2000")
F2.ajoutersalarie(D)



Entreprise.afficher()

