from employe import Employe
from voiture import Voiture

# débutant : on crée d'abord quelques objets
# employés
emp1 = Employe("12345", "Dupont", "Jean")
emp2 = Employe("67890", "Durand", "Marie")

# voitures
car1 = Voiture("AB-123-CD", 2020, "Toyota", 15000)
car2 = Voiture("EF-456-GH", 2019, "Lamborghini", 30000)

print("----- informations initiales -----")
emp1.afficherInformations()
emp2.afficherInformations()
car1.afficherInformations()
car2.afficherInformations()

print("\n----- affecter la voiture car1 à emp1 -----")
emp1.affecterVoiture(car1)

print("\n----- après affectation -----")
emp1.afficherInformations()
car1.afficherInformations()

print("\n----- tentative d'affecter car1 à emp2 (déjà prise) -----")
emp2.affecterVoiture(car1)

print("\n----- tentative d'affecter car2 à emp1 (emp1 a déjà une voiture) -----")
emp1.affecterVoiture(car2)

print("\n----- retirer la voiture de emp1 -----")
emp1.retirerVoiture()

print("\n----- état final -----")
emp1.afficherInformations()
car1.afficherInformations()