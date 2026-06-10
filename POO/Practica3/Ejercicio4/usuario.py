class Usuario:
    usuarios = []

    def __init__(self,nombre,apellido,hash):
        self.nombre = nombre
        self.apellido = apellido

        if len(hash)!=16:
            raise ArithmeticError("El codigo hash debe tener una longitud de 16 caracteres")
        elif (hash in Usuario.usuarios):
            raise  AttributeError("El codigo hash ya esta regitrado")
        else:
            self.hash = hash
            Usuario.usuarios.append(hash)

    def __str__(self):
        return f"{self.nombre}-{self.apellido}"
