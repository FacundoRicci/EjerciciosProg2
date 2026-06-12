from empleado import Empleado

class Tecnico(Empleado):

    def sueldo_final(self):
        return self.salario + 30000
    
    def mostrar_empleado(self):
        print(f"Tipo Empleado: Tecnico\nNombre Empleado: {self.nombre} {self.apellido}\nSueldo Final Empleado: {self.sueldo_final()}")
