class Produit:
    def __init__(self,nom,prixHT,TVA):
        self.nom = nom 
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    
    def afficher(self):
        print(f"Nom du produit : {self.nom}")
        print(f"Prix HT : {self.prixHT} €")
        print(f"TVA : {self.TVA} %")
        print(f"Prix TTC : {self.CalculerPrixTTC():.2f} €")

produit1 = Produit("citron" , 49.89 , 20)
produit1.afficher()
produit2 = Produit("casque", 629.99, 20)
produit2.afficher()
