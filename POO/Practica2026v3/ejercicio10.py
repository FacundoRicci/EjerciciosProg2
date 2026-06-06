class ProductoCodificado:
    contador = 0

    def __init__(self, nombre, precio):
        self.codigo_automatico = f"PROD-00{ProductoCodificado.contador}"
        self.nombre = nombre
        self.precio = precio
        ProductoCodificado.contador += 1

    def __str__(self):
        return f"Nombre: {self.nombre} Precio: {self.precio} Codigo: {self.codigo_automatico}"

coca = ProductoCodificado("Coca cola",300)
print(coca)
fanta = ProductoCodificado("Fanta", 250)
print(fanta)