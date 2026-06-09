from libro import Libro

class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.prestamos = []

    def nombreSistema(self):
        return f"{self.apellido}-{self.nombre}"
    
    def tomarPrestado(self,material):
        if material.disponible():
            self.prestamos.append(material)
            material.copias -= 1
            print("Libro tomado con exito")
        else:
            print("No hay ninguna copia para tomar prestada")
    
    def devolver(self,material):
        if(material in self.prestamos):
            material.copias += 1
            self.prestamos.remove(material)
            print("Libro devuelto con exito")
        else:
            print("No tienes ese material")

    def __str__(self):
        return f"{self.nombreSistema()}\nPrestamos: {self.prestamos}"

harry = Libro("Harry potter",2019,"Accion",2)
shrek = Libro("Shrek",2005,"Comedia",5)

facu = Usuario("Facundo","Ricci")

facu.tomarPrestado(harry)
print(harry)
print(facu)
