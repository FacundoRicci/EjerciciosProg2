class contadorPasos:
    def __init__(self):
        self.pasos = 0
    
    def caminar(self,cantidad):
        if(cantidad > 0):
            self.pasos += cantidad
            print("caminando...")
        else:
            print("La cantidad de pasos debe ser positiva")
        
    def reiniciar(self):
        self.pasos=0 

    def mostrarPasos(self):
        print(f'Pasos totales: {self.pasos}')

pasos1 = contadorPasos()

pasos1.caminar(20)
pasos1.reiniciar()
pasos1.mostrarPasos()