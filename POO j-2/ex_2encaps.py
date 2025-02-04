class Livre:
    #initialisation
    def __init__(self,titre,auteur,nombre_page):
        self.__titre = titre
        self.__auteur = auteur
        self.set_nombre_page(nombre_page)
#accesseur
    def get_titre_privee(self):
        return self.__titre
    
    def get_auteur_privee(self):
        return self.__auteur
    
    def get_nombre_page_privee(self):
        return self.__nombre_page
#mutateur
    def set_titre(self , nouveau_titre):
        self.__titre = nouveau_titre
    def set_auteur(self , nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nombre_page(self,nouveau_nombre_page):
        if isinstance(nouveau_nombre_page,int) and nouveau_nombre_page >0:
            self.__nombre_page = nouveau_nombre_page
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def afficher_info(self):
        print(f"Livre : Tittre = {self.__titre}, Auteur = {self.__auteur}, Nombre de pages = {self.__nombre_page}")

    #création d'un livre
mon_livre = Livre("Le Petit Prince" , "Antoine de saint-exupéry", 96)

mon_livre.afficher_info()

#modification des attributs
mon_livre.set_titre("1984")
mon_livre.set_auteur("George orwell")
mon_livre.set_nombre_page("328")

mon_livre.afficher_info()


#erreur
mon_livre.set_nombre_page(-100)
mon_livre.set_nombre_page("abc")