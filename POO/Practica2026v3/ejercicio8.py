class Examen:
    def __init__(self,estudiante,nota_privada):
        self.estudiante = estudiante
        if(nota_privada >= 1 and nota_privada <= 10):
            self.__nota_privada = nota_privada
        else:
            raise TypeError("Nota invalida.")
        
    def aprobado(self):
        if(self.__nota_privada >= 6):
            print(f"El alumno {self.estudiante} esta aprobado")
        else:
            print(f"El alumno {self.estudiante} esta desaprobado")

    def mostrar_resultado(self):
        print(f"El alumno {self.estudiante} obtuvo una calificacion de: {self.__nota_privada}")



mi_examen = Examen("Facundo Ricci", 9)
mi_examen.aprobado()
mi_examen.mostrar_resultado()