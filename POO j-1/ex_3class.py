class Operation:
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    

    def afficher_info(self):
        print(f"Le nombre1 est {self.nombre1}")
        print(f"Le nombre2 est {self.nombre2}")
    
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"le résultat est : {resultat}")
        

premiere_operation = Operation(12,3)
premiere_operation.afficher_info()
premiere_operation.addition()



