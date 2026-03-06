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
