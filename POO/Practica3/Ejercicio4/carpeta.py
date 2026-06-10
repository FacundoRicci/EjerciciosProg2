from archivo import Archivo

class Carpeta:
    def __init__(self,nombre,usuario,contenidos = []):
        self.nombre = nombre
        self.usuario = usuario
        self.contenidos = contenidos

    @property
    def tamanio(self):
        acum=0
        for contenido in self.contenidos:
            acum += contenido.tamanio
        return acum
    
    def agregar_contenido(self,nuevo_contenido):
        if nuevo_contenido in self.contenidos:
            contenido_temporal = Archivo("copia_"+nuevo_contenido.nombre,nuevo_contenido.usuario,nuevo_contenido.tamanio)
            self.contenidos.append(contenido_temporal)
        else:
            self.contenidos.append(nuevo_contenido)
    
    def eliminar_contenido(self, contenido):
        self.contenidos.remove(contenido)

    def mostrar_contenido(self):
        for contenido in self.contenidos:
            print(f"{contenido.nombre}", end=" - ")

