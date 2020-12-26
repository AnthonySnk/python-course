# def area_triangulo(base,altura):
#     return (base*altura)/2
def area_trinagulo(base, altura): return (base*altura/2)


print(area_trinagulo(5, 2))


# al_cubo = lambda numero:pow(numero,3)
def al_cubo(numero): return numero**3


print(al_cubo(13))


def destacar_valor(comision): return f"$ {comision}!"


comision_ana = 16348
print(destacar_valor(comision_ana))
