class Webinar:
    def __init__(self,nombre,mes,anio_inicio):
        self.nombre = nombre
        self.mes = mes
        self.anio_inicio = anio_inicio
        self.inscriptos = []
        self.finalizados = []
    
    def inscribir(self,alumno):
        if alumno not in self.inscriptos:
            self.inscriptos.append(alumno)
        else:
            print("El alumno ya se encuentra inscripto en este curso")

