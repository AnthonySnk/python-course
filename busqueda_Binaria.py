# -*- coding: utf-8 -*-
def run(numbers,numbers_to_find,low,high):
    # vamos haer una busqueda
    if low > high:
        return False
    mid  = int((low + high)/2)
    if(numbers[mid]== numbers_to_find):
        return True
    elif numbers[mid]>numbers_to_find:
        return run(numbers,numbers_to_find,low,mid-1)
    else:
        return run(numbers,numbers_to_find,mid+1,high)

if __name__ == "__main__":
    numbers = [1,3,4,5,6,9,10,11,25,27,28,34,36,49,51]
    numbers_to_find =int(input("Digita el número que deseas buscar:\n"))
    result = run(numbers,numbers_to_find,0,len(numbers)-1)
    if(result):
        print("El número si esta en la lista")
    else:
        print("El número no esta en la lista")