class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur

#accesseurs
    def get_longueur_privee(self):
        return self.__longueur
    
    def get_largeur_privee(self):
        return self.__largeur
#mutateurs
    def set_longueur(self, nouvelle_longueur):
        if nouvelle_longueur > 0:
            self.__longueur = nouvelle_longueur
        else:
            print("erreur : la longueur doit etre positive.")

    def set_largeur(self, nouvelle_largeur):
        if nouvelle_largeur > 0:
            self.__largeur = nouvelle_largeur
        else:
            print("erreur : la longueur doit etre positive.")
#Méthode pour afficher les informations du rectangle
    def afficher_infos(self):
        print(f"Rectangle : Longueur = {self.__longueur}, Largeur = {self.__largeur}")

#taille initiale
mon_rectangle = Rectangle(10, 5)
mon_rectangle.afficher_infos()
#modification
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(7)
mon_rectangle.afficher_infos()
#valeurs invalides
mon_rectangle.set_longueur(-5)
mon_rectangle.set_largeur(0)
mon_rectangle.afficher_infos()