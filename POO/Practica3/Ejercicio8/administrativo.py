from empleado import Empleado

class Administrativo(Empleado):

    def sueldo_final(self):
        return self.salario + (self.salario * 0.15)
    
    def mostrar_empleado(self):
        print(f"Tipo Empleado: Administrativo\nNombre Empleado: {self.nombre} {self.apellido}\nSueldo Final Empleado: {self.sueldo_final()}")

