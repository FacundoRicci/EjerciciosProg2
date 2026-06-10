class Estudiante    :
    def __init__(self,nombre,apellido,correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def inscribir(self,curso):
        if self not in curso.inscriptos:
            curso.inscriptos.append(self)
        else:
            print("El alumno ya se encuentra inscripto en este curso")