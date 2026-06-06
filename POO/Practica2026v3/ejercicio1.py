class Estudiante:
    def __init__(self,nombre,apellido,legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo

    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}, Legajo: {self.legajo}"
    
    def mostrarFicha(self):
        print(self)

estudiante1 = Estudiante("Facundo","Ricci", 56717)

estudiante1.mostrarFicha()