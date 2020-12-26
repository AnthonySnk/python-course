class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} que trabaja como {self.cargo} tiene un salario de $ {self.salario}"


listaEmpleado = [
    Empleado("juan", "Director", 6700),
    Empleado("Ana", "Presidente", 7500),
    Empleado("Antonio", "Administrativo", 2500),
    Empleado("April", "Secretaria", 2700),
    Empleado("Mario", "botones", 2100),
]


def calculo_comision(empleado):
    if (empleado.salario<=3000):
        empleado.salario = empleado.salario*1.03
    return empleado

listaEmpleadoComision=map(calculo_comision,listaEmpleado)

for empleado in listaEmpleadoComision:
    print(empleado)

