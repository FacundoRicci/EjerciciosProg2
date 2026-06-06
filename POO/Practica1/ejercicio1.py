class Item:
    def __init__(self,nombre,costo):
        self.nombre = nombre
        self.costo = costo

    def __str__(self):
        return f"{self.nombre}, Costo: ${self.costo}"
    

cocaCola = Item("Coca Cola",2000)

print(cocaCola)