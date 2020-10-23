# SETS


def run():
    s = set([1,2,3])
    t = set([3,4,5])
    print (s.union(t))# uniendo ambos conjuntos
    print(s.intersection(t)) # muestra solo los que son iguales en ambos conjuntos
    print(s.difference(t) )#Los que son diferentes
    print(s | t) # union
    print(s & t) # interseccion
    print(s-t) # restando t 
    print(s ^ t) #hace una union sin interseccion
    print(s <= t) # <= subconjunto          s.issubset(t)
    print(s >= t) # >= superconjunto        s.issuperset(t)

    # No se pueden cambiar los elementos de un set pero se pueden añadir:
    # mi_set.add(elemento)
    # mi_set.update([elemento1, elemento2, …])
    # También se pueden borrar:
    # mi_set.remove(elemento)

    nombres = set(['Maria', 'Jose', 'Simon', 'Eleonor', 'Jesebell', 'Taner'])
    findName = str(input('Ingresa tu nombre: '))
    if findName in nombres:
        print('Hola {} : como estas? pasa adelante'.format(findName))
    else:
        print('Uf {} tu no te encuentras en la lista, mi loco dele pa fuera'.format(findName))

if __name__ == '__main__':
    run()