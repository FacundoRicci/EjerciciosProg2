from membresia_mensual import MembresiaMensual
from membresia_anual import MembresiaAnual
from club import Club
from socio import Socio

facundo = Socio("Facundo","Ricci","47104092")

membresia1 = MembresiaMensual("12-04-2027",facundo,"activa", 2000)
membresia2 = MembresiaAnual("15-09-2020",facundo,"vencida",12000,10)

#print(membresia1.id)
#print(membresia2.calcular_costo())

rosario = Club()

rosario.agregar_membresia(membresia1)
rosario.agregar_membresia(membresia2)
#membresia1.renovar_membresia()
rosario.vencer_membresia(membresia1)
membresia1.renovar_membresia()
#print(membresia1.estado)

#rosario.mostrar_importe_individual_membresias()
#rosario.mostrar_importe_total_membresias()

rosario.mostrar_datos()