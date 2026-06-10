from mascota import Mascota

class Gato(Mascota):
    def calcular_costo_consulta(self):
        costo_total = 5000
        costo_total += self.edad*500
        return costo_total