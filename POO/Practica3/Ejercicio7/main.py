from perro import Perro
from gato import Gato
from veterinaria import Veterinaria

gato1 = Gato("Juancho",22,23)
perro1 = Perro("Catalina",10,4)

print(perro1.calcular_costo_consulta())
gato1.modificar_peso = 25
print(gato1.calcular_costo_consulta())
print(gato1.peso)


veterinaria1 = Veterinaria("Maria")

veterinaria1.agregar_mascota(gato1)
veterinaria1.agregar_mascota(perro1)

veterinaria1.mostrar_mascotas_a_cargo()