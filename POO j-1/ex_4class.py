class Personne:
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        print(f"je suis {self.nom} {self.prenom}")

premiere_peronne = Personne("Albertini","Nathalie")
deuxieme_personne = Personne("Odinot","Matthieu")

premiere_peronne.SePresenter()
deuxieme_personne.SePresenter()