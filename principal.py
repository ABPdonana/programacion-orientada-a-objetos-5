from empleado import Empleado

emp1 = Empleado('María', 'García', 60000)
emp2 = Empleado.desde_cadena('Juan-Pérez-55000')
emp1.nombre()
emp1.salario()
emp2.nombre()
emp2.salario()
