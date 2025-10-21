class Hobbies:
    def __init__(self, ruta_del_archivo:str="./miHobbieFavorito.txt"):
        self.ruta_del_archivo = ruta_del_archivo
        self.hobbies=[]
    def agregar_hobbie(self, hobbie:str):
        self.hobbies.append(hobbie)
    def ingresar_hobbie(self, cantidad_hobbies:int=3):
        for _ in range(cantidad_hobbies):
            hobbie = input("Ingrese un hobbie: ")
            