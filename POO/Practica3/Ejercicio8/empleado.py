class Empleado:
    contador = 1
    def __init__(self,nombre,apellido,salario_inicial):
        self.nombre = nombre
        self.apellido = apellido
        if salario_inicial > 0:
            self.__salario_privado = salario_inicial
        else:
            raise AttributeError("El salario debe ser mayor a 0")
        self.id = Empleado.contador
        Empleado.contador += 1

    @property
    def salario(self):
        return self.__salario_privado
    
    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario_privado = nuevo_salario
        else:
            raise AttributeError("El salario debe ser mayor 0")

