from membresia import Membresia

class MembresiaMensual(Membresia):
    #Esto se podria sacar y funcionar de igual manera
    #def __init__(self, fecha_alta, socio, estado, costo):
    #    super().__init__(fecha_alta, socio, estado, costo)

    def calcular_costo(self):
        return self.costo
    
    def __str__(self):
        return f"DATOS MEMBRESIA ID {self.id}:\n{self.socio}\nFecha de alta: {self.fecha_alta}\nEstado membresia: {self.estado}\nCosto final: {self.calcular_costo()}"