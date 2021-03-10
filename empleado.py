class Empleado():

    def __init__(self, nombre, apellidos, salario):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__salario = salario

    def nombre(self):
        return self.__nombre

    def apellidos(self):
        return self.__apellidos

    def salario(self):
        return self.__salario

    @staticmethod
    def desde_cadena(cadena):
        parametros = cadena.split("-")
        Empleado(parametro[0], parametro[1], parametro[2])
