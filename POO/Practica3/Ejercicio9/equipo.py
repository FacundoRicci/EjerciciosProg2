from jugador import Jugador

class Equipo:
    def __init__(self,nombre):
        self.nombre = nombre
        self.lista_jugadores = []

    def lista_numeros(self):
        lista = []
        for jugador in self.lista_jugadores:
            lista.append(jugador.numero_camiseta)
        return lista

    def agregar_jugador(self,jugador):
        if isinstance(jugador,Jugador) and (jugador.numero_camiseta not in self.lista_numeros()):
            self.lista_jugadores.append(jugador)
        else:
            raise AttributeError("Solo se pueden ingresar jugadores que tengan distinto numero")

    def cantidad_jugadores(self):
        contador = 0
        for jugador in self.lista_jugadores:
            contador += 1
        return contador
    
    def mostrar_club(self):
        print(f"CLUB {self.nombre}")
        for jugador in self.lista_jugadores:
            print(jugador)