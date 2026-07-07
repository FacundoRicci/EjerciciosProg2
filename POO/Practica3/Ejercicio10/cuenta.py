class Cuenta:
    def __init__(self,nro_cuenta,saldo):
        self.nro_cuenta = nro_cuenta
        if saldo >= 0:
            self.__saldo = saldo
        else:
            raise AttributeError("El saldo debe ser mayor a 0")
        
    def ingresarSaldo(self,monto):
        if monto > 0:
            self.__saldo += monto
        else:
            raise AttributeError("El monto ingresado debe ser mayor a 0")
    
    def retirarSaldo(self,monto):
        if monto > self.__saldo:
            raise AttributeError("El monto a retirar debe ser menor al saldo")
        else:
            self.__saldo -= monto

    def __str__(self):
        return f"Numero de cuenta: {self.nro_cuenta} Saldo: {self.__saldo}"