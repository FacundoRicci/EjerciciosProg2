from mascota import Mascota

class Perro(Mascota):
    def calcular_costo_consulta(self):
        costo_total = 5000
        costo_total += 1500
        return costo_total