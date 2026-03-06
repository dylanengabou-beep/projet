class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None

    def afficherInformations(self):
        print("employe : ", self.prenom, self.nom)
        print("permis :", self.numeroPermis)

        if self.voitureService is not None:
            print("voiture : ", self.voitureService.marque, self.voitureService.matricule)
        else:
            print("pas de voiture de service")

    def affecterVoiture(self, voiture):
        if self.voitureService is None and voiture.chauffeur is None:
            self.voitureService = voiture
            voiture.chauffeur = self
            print("voiture assignee")
        else:
            print("impossible d'assigner la voiture")

    def retirerVoiture(self):
        if self.voitureService is not None:
            self.voitureService.chauffeur = None
            self.voitureService = None
            print("voiture retiree")
        else:
            print("cet employe n'a pas de voiture")
