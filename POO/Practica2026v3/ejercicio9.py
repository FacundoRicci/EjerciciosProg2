class Cuenta:
    def __init__(self, titular, saldo_privado, limite_extraccion):
        self.titular = titular
        self.__saldo_privado = saldo_privado
        self.limite_extraccion = limite_extraccion
    
    def extraer(self, cantidad):
        if(cantidad < 0 or cantidad > self.__saldo_privado or cantidad > self.limite_extraccion):
            print("Error, ingrese una cantidad valida")
        else:
            self.__saldo_privado -= cantidad
            print(f"Usted extrajo correctamente ${cantidad} de su cuenta")

    def __str__(self):
        return f"Cuenta a nombre de {self.titular} con un saldo de ${self.__saldo_privado}"
    

persona1 = Cuenta("Juan",2000,20000)
persona1.extraer(200)
print(persona1)