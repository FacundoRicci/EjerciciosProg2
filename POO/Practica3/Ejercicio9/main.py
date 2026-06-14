from jugador import Jugador
from equipo import Equipo

facu = Jugador("Facundo","Ricci",10)
juan = Jugador("Juan","Diaz",19)

central = Equipo("Rosario Central")

central.agregar_jugador(facu)
central.agregar_jugador(juan)
print(central.cantidad_jugadores())
central.mostrar_club()