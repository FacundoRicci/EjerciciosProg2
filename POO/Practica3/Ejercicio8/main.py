from empleado import Empleado
from administrativo import Administrativo
from tecnico import Tecnico

facundo = Administrativo("Facundo","Ricci",24000)
juan = Tecnico("Juan","Ricci",32000)

print(facundo.id)
print(juan.id)

juan.mostrar_empleado()