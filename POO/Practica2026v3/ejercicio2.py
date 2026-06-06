class Termometro:
    def __init__(self,temperatura):
        self.temperatura = temperatura

    def __str__(self):
        return f"Temperatura: {self.temperatura}"
    
    def mostrarTemperatura(self):
        print(self)
    
    def estado(self):
        if(self.temperatura < 18):
            print("Temperatura baja")
        elif(self.temperatura > 26):
            print("Temperatura alta")
        else:
            print("Temperatura media")
    

termometro1 = Termometro(25)
termometro2 = Termometro(10)

termometro1.mostrarTemperatura()
termometro1.estado()

termometro2.mostrarTemperatura()
termometro2.estado()