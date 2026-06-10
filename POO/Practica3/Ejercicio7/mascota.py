class Mascota:
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        if peso > 0:
            self.peso = peso
        else:
            raise AttributeError ("El peso ingresado debe ser mayor o igual a 0")

    @property
    def modificar_peso(self):
        return self.peso
    
    @modificar_peso.setter
    def modificar_peso(self,peso_nuevo):
        if peso_nuevo > 0:
            self.peso=peso_nuevo
        else:
            raise AttributeError ("El peso ingresado debe ser mayor o igual a 0")