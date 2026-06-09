from webinar import Webinar

class Curso(Webinar):
    def __init__(self,nombre,mes,anio_inicio,cupo_estudiantes=30):
        super().__init__(nombre,mes,anio_inicio)
        self.cupo_estudiantes = cupo_estudiantes

    def __str__(self):
        return f"Nombre: {self.nombre}\nLista inscriptos: {self.inscriptos}"

