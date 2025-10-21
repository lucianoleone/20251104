# Hacer una clase facil, como alumno, con nombre y nota, con un metodo imprimir().
# Crear un programa principal que importe la clase y cree un alumno, le asigne nombre y nota e imprima.
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        return f"Alumno: {self.nombre}, Nota: {self.nota}"