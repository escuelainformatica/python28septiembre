from functools import reduce

numeros = [1, 22, 3, 4, 5]

paises=["Chile","Argentina","Peru","Bolivia"]


def sumar(actual: int, acumulador: int):
    return actual + acumulador


print(reduce(lambda actual, acumulador: sumar(actual, acumulador), numeros))

def menor(actual:str, acumulador:str):
    if actual<acumulador:
        return actual
    else:
        return acumulador

print(reduce(lambda actual,acumulador: menor(actual,acumulador),paises))

def contar(actual: int, acumulador: int):
    print(f"el acumulador vale {actual} {acumulador} ")
    return acumulador+1

print(reduce(lambda actual, acumulador: contar(actual, acumulador), numeros))

