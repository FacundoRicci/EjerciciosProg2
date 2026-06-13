from socio import Socio

class Membresia:
    contador = 1
    def __init__(self,fecha_alta,socio,estado,costo):
        #fecha_alta
        self.fecha_alta = fecha_alta
        #socio
        if isinstance(socio,Socio):
            self.socio = socio
        else:
            raise AttributeError("Ingrese un socio valido")
        #id
        self.id = Membresia.contador
        Membresia.contador += 1
        #estado
        if estado == "activa" or estado == "vencida":
            self.estado = estado
        else:
            raise AttributeError("El estado de la membresia solo puede ser 'activa' o 'vencida'")
        #costo
        if costo > 0:
            self.__costo = costo
        else:
            raise AttributeError("El costo debe ser mayor a 0")
        
    #Getter
    @property
    def costo(self):
        return self.__costo
    
    #Dejo a costo sin setter, ya que es un valor que no quiero que se modifique
    #Setter
    """
    @costo.setter
    def costo(self,nuevo_costo):
        if nuevo_costo>0:
            self.__costo = nuevo_costo
        else:
            raise AttributeError("El costo debe ser mayor a 0")
    """

    def renovar_membresia(self):
        if self.estado == "activa":
            raise AttributeError("No se puede renovar una membresia activa")
        else:
            self.estado = "activa"