class People:
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def Mostrar(self):
        print(f'Caracterisiticas del objeto : {self.nombre} {self.apellido} {self.edad}')