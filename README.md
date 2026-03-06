# Gestion des Employés et Voitures

## Description
Ce projet implemente un systeme de gestion d'employes et de voitures de service. 
Il permet d'affecter des voitures aux employes, de retirer des voitures et de consulter les informations.

## Fichiers du Projet

### 1. **employe.py**
Contient la classe `Employe` avec :
- **Attributs** : numeroPermis, nom, prenom, voitureService
- **Methodes** :
  - `afficherInformations()` : affiche les details de l'employe
  - `affecterVoiture(voiture)` : assigne une voiture a l'employe
  - `retirerVoiture()` : retire la voiture de l'employe
  - `modifierNom(nom)` : modifie le nom de l'employe

### 2. **voiture.py**
Contient la classe `Voiture` avec :
- **Attributs** : matricule, annee, marque, kilometrage, chauffeur
- **Methodes** :
  - `afficherInformations()` : affiche les details de la voiture
  - `augmenterKilometrage(km)` : augmente le kilometrage de la voiture
  - `obtenirAge()` : retourne l'age de la voiture

### 3. **main.py**
Programme principal qui :
- Crée plusieurs instances d'employes et de voitures
- Affiche les informations initiales
- Affecte les voitures aux employes
- Teste les retraits et les affectations conflictuelles

## Comment Utiliser

1. **Executer le programme**
   ```
   python main.py
   ```

2. **Tester les differentes operations**
   - Affichage des informations
   - Affectation de voitures
   - Retrait de voitures
   - Gestion des conflits

## Exemple d'Utilisation

```python
from employe import Employe
from voiture import Voiture

# Creer un employe
emp = Employe("12345", "Dupont", "Jean")

# Creer une voiture
car = Voiture("AB-123-CD", 2020, "Toyota", 15000)

# Affecter la voiture
emp.affecterVoiture(car)

# Afficher les informations
emp.afficherInformations()
car.afficherInformations()

# Retirer la voiture
emp.retirerVoiture()
```

## Contraintes et Regles

- Un employe ne peut avoir qu'une seule voiture
- Une voiture ne peut etre affectee qu'a un seul employe
- Impossible d'affecter une voiture deja occupee
- Impossible de retirer une voiture non affectee

## Commits Realises

Le projet contient 9 commits correspondant aux differentes etapes :
1. Creation classe Employe
2. Implementation methodes Employe
3. Creation classe Voiture
4. Implementation methodes Voiture
5. Creation instances
6. Affichage informations
7. Affectation voitures
8. Retrait voitures
9. Affectation voiture deja assignee
