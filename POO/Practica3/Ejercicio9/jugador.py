class Jugador:
    def __init__(self,nombre,apellido,numero_camiseta):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_camiseta = numero_camiseta

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido} | Nro Camiseta: {self.numero_camiseta}"