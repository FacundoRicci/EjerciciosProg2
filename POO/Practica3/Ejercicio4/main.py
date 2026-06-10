from archivo import Archivo
from carpeta import Carpeta
from usuario import Usuario

facu = Usuario("Facundo","Ricci","1234567890123456")
facu2 = Usuario("Facundo","Ricci","1234567890123457")

archivo1 = Archivo("texto.txt",facu,105)
archivo2 = Archivo("imagen.pdf",facu,255)
carpeta1 = Carpeta("Nueva carpeta",facu,[archivo1])
carpeta2 = Carpeta("Imagenes",facu2,[archivo2])

carpeta1.agregar_contenido(archivo2)
carpeta1.agregar_contenido(archivo2)
carpeta1.agregar_contenido(carpeta2)
carpeta1.agregar_contenido(archivo1)

#carpeta1.eliminar_contenido(archivo1)
print(carpeta1.tamanio)

carpeta1.mostrar_contenido()