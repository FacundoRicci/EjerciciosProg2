from membresia import Membresia

class Club:
    def __init__(self):
        self.membresias = []

    def agregar_membresia(self,membresia):
        if isinstance(membresia,Membresia):
            self.membresias.append(membresia)
        else:
            raise AttributeError("Ingrese una membresia valida")
        
    def vencer_membresia(self,membresia):
        if isinstance(membresia,Membresia) and membresia in self.membresias:
            membresia.estado = "vencida"
        else:
            raise AttributeError("Ingrese una membresia valida")
        

    def mostrar_importe_individual_membresias(self):
        for membresia in self.membresias:
            print(f"{membresia.calcular_costo()}")

    def mostrar_importe_total_membresias(self):
        acum = 0
        for membresia in self.membresias:
            acum += membresia.calcular_costo()
        print(f"Costo total de todas las membresias: {acum}")

    def mostrar_datos(self):
        print ("-----DATOS DEL CLUB-----\n  ---MEMBRESIAS---  ")
        for membresia in self.membresias:
            print(membresia)
            print("---------------------")
        print(f"   ---COSTO TOTAL MEMBRESIAS--- ")
        self.mostrar_importe_total_membresias()
        