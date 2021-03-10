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

    def nombre_completo(self):
        return self.nombre() + " " + self.apellidos()

    def email(self):
        __aux = self.nombre() + "." + self.apellidos() + "@company.com"
        return __aux.lower()

    @staticmethod
    def desde_cadena(cadena):
        parametro = cadena.split("-")
        return Empleado(parametro[0], parametro[1], parametro[2])
