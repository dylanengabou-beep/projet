from employe import Employe
from voiture import Voiture

# Etape 5 : Créez plusieurs instances de la classe Voiture et Employe
emp1 = Employe("12345", "Dupont", "Jean")
emp2 = Employe("67890", "Durand", "Marie")

car1 = Voiture("AB-123-CD", 2020, "Toyota", 15000)
car2 = Voiture("EF-456-GH", 2019, "Lamborghini", 30000)

# Etape 6 : Affichez les informations de tous les objets créés
print("----- Informations initiales -----")
emp1.afficherInformations()
emp2.afficherInformations()
car1.afficherInformations()
car2.afficherInformations()

# Etape 7 : Affectez certaines voitures à des employés et affichez à nouveau
print("\n----- Affecter car1 a emp1 -----")
emp1.affecterVoiture(car1)

print("\n----- Informations apres affectation -----")
emp1.afficherInformations()
car1.afficherInformations()

# Etape 8 : Retirer la voiture de certains employés et afficher
print("\n----- Retirer la voiture de emp1 -----")
emp1.retirerVoiture()

print("\n----- Informations apres retrait -----")
emp1.afficherInformations()
car1.afficherInformations()

# Etape 9 : Affecter une voiture deja affectee a un autre employe
print("\n----- Affecter car2 a emp1 et car1 a emp2 -----")
emp1.affecterVoiture(car2)
emp2.affecterVoiture(car1)

print("\n----- Tentative d'affecter car1 (deja prise) a emp1 -----")
emp1.affecterVoiture(car1)

print("\n----- Etat final -----")
emp1.afficherInformations()
emp2.afficherInformations()
car1.afficherInformations()
car2.afficherInformations()
