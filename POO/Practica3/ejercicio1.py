class Factura:
    contador = 1

    def __init__(self,producto,cantidad,empresa):
        self.numeroFactura = Factura.contador
        self.producto = producto
        self.cantidad = cantidad
        self.empresa = empresa
        Factura.contador +=1

    def __str__(self):
        return f"Nro factura: {self.numeroFactura}\nNombre producto: {self.cantidad}\nCantidad: {self.producto}\nEmpresa: {self.empresa}\n----------------"
    
tomates = Factura("Tomates",3,"Arcor")
naranjas = Factura("Naranjas",5,"Laserenisima")
print(tomates)
print(naranjas)