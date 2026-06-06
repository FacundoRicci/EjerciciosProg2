class Pelicula:
    def __init__(self,titulo,genero,duracion_minutos):
        self.titulo = titulo
        self.genero = genero
        self.duracion_minutos = duracion_minutos
    
    def mostrar_info(self):
        print("---------------------------")
        print(f"Pelicula: {self.titulo}\nGenero: {self.genero}\nDuracion: {self.duracion_minutos}")
        print("---------------------------")

    def es_larga(self):
        if(self.duracion_minutos > 120):
            print("La pelicula es larga")
        else:
            print("La pelicula no es larga")


pinocho = Pelicula("Pinocho","Aventura",121)

pinocho.mostrar_info()
pinocho.es_larga()