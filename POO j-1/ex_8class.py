class Cercle:
    PI = 3.14159
    def __init__(self,rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Cercle de rayon : {self.rayon}")
        print(f"Cercle de circonférence : {self.circonference()}")
        print(f"Diamètre : {self.diametre()}")
        print(f"Aire : {self.aire()}")

    def circonference(self):
        return 2 * self.PI * self.rayon
    
    def aire(self):
        return self.PI * (self.rayon ** 2)
    
    def diametre(self):
        return 2 * self.rayon
    
cercle1 = Cercle(4)
cercle2 = Cercle(7)

print("Cercle 1 :")
cercle1.afficherInfos()

print("\nCercle 2 :")
cercle2.afficherInfos()