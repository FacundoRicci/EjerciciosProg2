from webinar import Webinar
from cursos import Curso
from estudiante import Estudiante

programacionweb = Curso("Programacion Web",5,2020)
facundo = Estudiante("Facundo","Ricci","facuricci0141@gmail.com")
facundo.inscribir(programacionweb)
print(programacionweb)