from libro import Libro

class Estanteria:
    def __init__(self,titulo):
        self.titulo = titulo
        self.contenidos = []
    
    @property
    def cantidad_paginas(self):
        acum = 0
        for contenido in self.contenidos:
            acum += contenido.cantidad_paginas
        return acum
    
    def agregar_contenido(self,contenido):
        if contenido in self.contenidos:
            contenido_temporal = Libro("copia_"+contenido.titulo,contenido.autor,contenido.cantidad_paginas)
            self.contenidos.append(contenido_temporal)
        else:
            self.contenidos.append(contenido)

    def eliminar_contenido(self,contenido):
        self.contenidos.remove(contenido)

    def mostrar_contenidos(self):
        for contenido in self.contenidos:
            print(f"{contenido.titulo}",end=" - ")


class EstanteriaSimple(Estanteria):
    
    def agregar_contenido(self, contenido):
        #print(isinstance(contenido, Libro))
        if isinstance(contenido, Libro):
            if contenido in self.contenidos:
                contenido_temporal = Libro("copia_"+contenido.titulo,contenido.autor,contenido.cantidad_paginas)
                self.contenidos.append(contenido_temporal)
            else:
                self.contenidos.append(contenido)
        else:
            print("Solo se pueden agregar libros a una estanteria simple")