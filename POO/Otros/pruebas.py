class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} de {self.autor}"
    

libro1 = Libro("El Hobbit","Tolkien")
libro2 = Libro("Harry Potter","JK Rowling")
#print(libro1)
#print(libro2)

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregarLibro(self,libro):
        self.libros.append(libro)

    def mostrarLibros(self):
        print("Libros disponibles:")
        for libro in self.libros:
            print(libro)


biblioteca1 = Biblioteca()
biblioteca1.agregarLibro(libro1)
biblioteca1.agregarLibro(libro2)
#biblioteca1.mostrarLibros()

class Persona:
    def __init__(self,nombre,apellido,dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"{self.nombre} {self.apellido} = {self.dni}"
    
class AlumnoTup(Persona):
    def __init__(self,nombre,apellido,dni,curso):
        Persona.__init__(self, nombre, apellido, dni)
        self.curso = curso

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.dni} | TUP {self.curso}"
    
alumno = AlumnoTup("Ana", "Gonzalez", 99999999, "Turno mañana")
print(alumno)