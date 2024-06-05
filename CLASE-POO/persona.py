class Persona:

    # constructor __init__ (dundee - double underscore)
    def __init__(self, nombre, edad, apellido):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido

    def monstrar_conctactos(self):
        print(f''' Persona:
        Nombre: {self.nombre}
        Edad: {self.edad}
        Apellido: {self.apellido}''')


if __name__ == "__main__":
    # creacion de un primer objeto
    persona1 = Persona("Juan", 28, "Perez") # se llama de manera automatica el constructor
    persona1.monstrar_conctactos()

    # creacion de un segundo objeto
    persona2 = Persona("Maria", 25, "Gomez")
    persona2.monstrar_conctactos()

