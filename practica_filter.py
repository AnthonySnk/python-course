# def numero_par(num):
#     if num % 2 == 0:
#         return True
numeros=[17,23,2,4,23,0,52]
print(list(filter(lambda numero_par:numero_par % 2 ==0,numeros)))
# [2, 4, 0, 52]


class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return f"{self.nombre} que trabaja como {self.cargo} tiene un salario de $ {self.salario}"

listaEmpleado=[
    Empleado("juan","Director", 783480),
    Empleado("Ana","Presidente", 850000),
    Empleado("Antonio","Administrativo", 25000),
    Empleado("April","Secretaria", 27000),
    Empleado("Mario","botones", 21000),
]

salarios_altos = filter(lambda empleado:empleado.salario>50000,listaEmpleado)

for empleado_salario in salarios_altos:
    print (empleado_salario)