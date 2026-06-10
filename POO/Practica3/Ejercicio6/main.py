from libro import Libro
from estanteria import Estanteria
from estanteria import EstanteriaSimple

harry = Libro("Harry Potter","JK Rowling",200)
shrek = Libro("Shrek","Juan",120)

estanteria1 = Estanteria("Estanteria Principal")
estanteria2 = Estanteria("Estanteria Accion")

estanteria1.agregar_contenido(harry)
estanteria1.agregar_contenido(shrek)

estanteria2.agregar_contenido(estanteria1)
estanteria2.agregar_contenido(harry)
estanteria2.agregar_contenido(harry)


#print(estanteria2.cantidad_paginas)
#estanteria2.mostrar_contenidos()

estanteria_simple1 = EstanteriaSimple("Estanteria Simple Comedia")
estanteria_simple1.agregar_contenido(shrek)
estanteria_simple1.agregar_contenido(estanteria1)
estanteria_simple1.agregar_contenido(harry)
estanteria_simple1.mostrar_contenidos()