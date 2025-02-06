class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    def vieillir(self):
        self.age += 1
    def afficherAge(self):
        print(f"L'age de l'animal est {self.age} ans.")
    def nommer(self,nom):
        self.prenom = nom
        print(f"L'animal a été nommé {self.prenom}.")

mon_animal = Animal()
mon_animal.nommer("Rex")
mon_animal.afficherAge()
mon_animal.vieillir()
mon_animal.afficherAge()
