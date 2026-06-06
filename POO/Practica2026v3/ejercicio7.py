class Usuario:
    def __init__(self,nombre_usuario,contrasena_privada):
        self.nombre_usuario = nombre_usuario
        if(len(contrasena_privada) < 6):
            raise TypeError("Contraseña muy corta")
        else:
            self.__contrasena_privada = contrasena_privada
    

#    def contrasena(self):
#        return self.__contrasena_privada

    def cambiar_contrasena(self,nueva_contrasena):
        if(len(nueva_contrasena) >= 6):
            self.__contrasena_privada = nueva_contrasena
            print("Contraseña cambiada con exito.")
        else:
            print("Nueva contraseña invalida.")

    def verificar_contrasena(self, intento):
        if(intento == self.__contrasena_privada):
            print("Contraseña correcta.")
        else:
            print("Contraseña incorrecta.")

    def __str__(self):
        return f"Usuario: {self.nombre_usuario}\nContraseña: {self.__contrasena_privada}"


facundo = Usuario("Facu141","123456")
print(facundo)
facundo.cambiar_contrasena("1234")
facundo.cambiar_contrasena("654321")
print(facundo)
facundo.verificar_contrasena("456789")
facundo.verificar_contrasena("654321")
