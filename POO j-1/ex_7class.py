class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y  

    #se déplacer à gauche
    def gauche(self):
        self.y -= 1

    #se déplacer à droite
    def droite(self):
        self.y += 1 

    #se déplacer en haut
    def haut(self):
        self.x -= 1 

    #se déplacer en bas
    def bas(self):
        self.x += 1  

    def position(self):
        return (self.x, self.y)

joueur = Personnage(0, 0)  #personnage à la position (0, 0)

#position initiale
print("Position initiale :", joueur.position())  # Affiche : (0, 0)

#déplacement du personnage
joueur.droite()  # déplacement à droite
print("Après déplacement à droite :", joueur.position())  # Affiche : (0, 1)

joueur.bas()  # déplacement en bas
print("Après déplacement en bas :", joueur.position())  # Affiche : (1, 1)

joueur.gauche()  # déplacement à gauche
print("Après déplacement à gauche :", joueur.position())  # Affiche : (1, 0)

joueur.haut()  # déplacement en haut
print("Après déplacement en haut :", joueur.position())  # Affiche : (0, 0)