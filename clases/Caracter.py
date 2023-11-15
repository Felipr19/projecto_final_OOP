


class Caracter:
    def __init__(self, nombre, salud, velocidad):
        self.nombre = nombre
        self.salud = salud
        self.velocidad = velocidad

    def mostrar_estado(self):
        print(f"{self.nombre}: Salud={self.salud}, Velocidad={self.velocidad}")

