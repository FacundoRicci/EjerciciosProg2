class ContadorPasos:
    def __init__(self):
        self.pasos = 0

    def caminar(self,cantidad):
        self.pasos += cantidad

    def reiniciar(self):
        self.pasos = 0
    
    def mostrar_pasos(self):
        print(f"Cantidad de pasos caminados: {self.pasos}")


paseo = ContadorPasos()
paseo.caminar(100)
paseo.mostrar_pasos()
paseo.reiniciar()
paseo.mostrar_pasos()