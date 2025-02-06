class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(f"coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"la coordonnée du point X est :({self.x})")

    def afficherY(self):
        print(f"la coordonnée du point Y est :({self.y})")

    def changerX(self,nouvelle_valeur_x):
        self.x = nouvelle_valeur_x
    def changerY(self,nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

point = Point(5,6)
point.afficherLesPoints()

point.afficherX()
point.afficherY()

point.changerX(3)
point.changerY(40)

point.afficherLesPoints()