from membresia import Membresia

class MembresiaAnual(Membresia):
    def __init__(self, fecha_alta, socio, estado, costo, descuento):
        super().__init__(fecha_alta, socio, estado, costo)
        self.descuento = descuento

    def calcular_costo(self):
        return self.costo - (self.costo/100*self.descuento)
    
    def __str__(self):
        return f"DATOS MEMBRESIA ID {self.id}:\n{self.socio}\nFecha de alta: {self.fecha_alta}\nEstado membresia: {self.estado}\nCosto: {self.costo}\nDescuento: {self.descuento}%\nCosto final: {self.calcular_costo()}"