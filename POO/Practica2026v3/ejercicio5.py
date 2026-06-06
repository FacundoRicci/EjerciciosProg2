class CajaAhorro:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self,monto):
        if(monto > 0): 
            self.saldo += monto
            print(f"Usted deposito ${monto} en su cuenta...")
        else:
            print("Ingrese un monto valido...")

    def extraer(self,monto):
        if(self.saldo >= monto and monto > 0):
            self.saldo -= monto
            print(f"Usted extrajo ${monto} de su cuenta...")
        else:
            print("Ingrese un monto valido...")

    def consultar_saldo(self):
        print(f"La cuenta a nombre de {self.titular} tiene un saldo de ${self.saldo}")

    
cuentaBanco = CajaAhorro("Facundo Ricci", 1000)
cuentaBanco.extraer(2000)
cuentaBanco.extraer(500)
cuentaBanco.depositar(2000)
cuentaBanco.consultar_saldo()