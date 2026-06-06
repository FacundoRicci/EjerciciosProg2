class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.__precio = precio

    @property
    def mi_precio(self):
        return f"Precio: ${self.__precio}"

    @mi_precio.setter
    def mi_precio(self, nuevo_precio):
        self.__precio = nuevo_precio
    

    def __str__(self):
        return f"Producto: {self.nombre} | {self.mi_precio}"

cafe = Producto("Cafe",20)
print(cafe)
cafe.mi_precio = 30
print(cafe)