class Libro:
    def __init__(self,titulo,anio,genero,copias,autor="Desconocido"):
        self.titulo = titulo
        self.anio = anio
        self.genero = genero
        self.copias = copias
        self.autor = autor
    
    def disponible(self):
        if(self.copias > 0):
            return True
        else:
            return False
    
    def __str__(self):
        return f"Titulo: {self.titulo}\nAño: {self.anio}\nGenero: {self.genero}\nCopias: {self.copias}\nAutor: {self.autor}"
