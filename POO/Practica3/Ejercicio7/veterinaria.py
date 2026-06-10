class Veterinaria:
    def __init__(self,nombre):
        self.nombre = nombre
        self.mascotas_a_cargo = []

    def agregar_mascota(self,mascota):
        self.mascotas_a_cargo.append(mascota)

    def mostrar_mascotas_a_cargo(self):
        for mascota in self.mascotas_a_cargo:
            print(f"{mascota.nombre}", end=" - ")