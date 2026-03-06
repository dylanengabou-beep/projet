class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None

    def afficherInformations(self):
        print("voiture : ", self.marque)
        print("matricule : ", self.matricule)
        print("annee : ", self.annee)
        print("kilometrage : ", self.kilometrage)

        if self.chauffeur is not None:
            print("chauffeur : ", self.chauffeur.prenom,  self.chauffeur.nom)
        else:
            print("pas de chauffeur assigné")

    def augmenterKilometrage(self, km):
        self.kilometrage = self.kilometrage + km
        print("kilometrage augmente de", km, "km")