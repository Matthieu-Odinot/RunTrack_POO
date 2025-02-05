class Livre:
    #initialisation
    def __init__(self,titre,auteur,nombre_page):
        self.__titre = titre
        self.__auteur = auteur
        self.set_nombre_page(nombre_page)

        self.__dispo = True

#accesseur
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nombre_page(self):
        return self.__nombre_page
    
    def get_dispo(self):
        return self.__dispo
#mutateur
    def set_titre(self , nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self , nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nombre_page(self,nouveau_nombre_page):
        if isinstance(nouveau_nombre_page,int) and nouveau_nombre_page >0:
            self.__nombre_page = nouveau_nombre_page
        else:
            print("erreur : le nombre de pages doit être un entier positif")

    def verification_dispo(self):
        return self.__dispo

    def emprunter(self):
        if self.verification_dispo():
            self.__dispo = False
            print("Le livre a été emprunté avec succès.")
        else:
            print("Erreur : Le livre n'est pas disponible.")

    def rendre(self):
        if not self.verification_dispo():
            self.__dispo = True
            print("Le livre a été rendu avec succès.")
        else:
            print("Erreur : Le livre n'a pas été emprunté.")



    def afficher_info(self):
        disponibilite = "Disponible" if self.__dispo else "Indisponible"
        print(f"livre : titre = {self.__titre}, Auteur = {self.__auteur}, Nombre de pages = {self.__nombre_page}, Statut = {disponibilite}")


# Création d'un livre
mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
# Affichage des informations initiales
mon_livre.afficher_info()  # Livre : Titre = Le Petit Prince, Auteur = Antoine de Saint-Exupéry, Nombre de pages = 96, Statut = Disponible

# Emprunter le livre
mon_livre.emprunter()  # Le livre a été emprunté avec succès.
mon_livre.afficher_info()  

# Essayer d'emprunter à nouveau (erreur attendue)
mon_livre.emprunter()  # Erreur : Le livre n'est pas disponible.

# Rendre le livre
mon_livre.rendre()  # Le livre a été rendu avec succès.
mon_livre.afficher_info()  # Livre : Titre = Le Petit Prince, Auteur = Antoine de Saint-Exupéry, Nombre de pages = 96, Statut = Disponible

# Essayer de rendre à nouveau (erreur attendue)
mon_livre.rendre()  