class Operation:
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    def afficher_info(self):
        print(f"Operation object at {self.nombre1}{self.nombre2}")

premiere_operation = Operation("0x00000","2541F869CF0")
premiere_operation.afficher_info()

