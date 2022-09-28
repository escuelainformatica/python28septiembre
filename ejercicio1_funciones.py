import csv
import decimal
from functools import reduce


def procesar_linea_csv(fila: list):
    dic = {
        "id": fila[0],
        "sobrevivio": fila[1],
        "pclass": fila[2],
        "nombre": fila[3],
        "sex": fila[4],
        "edad": fila[5],
        "sibsp": fila[6],
        "parch": fila[7],
        "ticket": fila[8],
        "fare": decimal.Decimal(fila[9]),
        "cabin": fila[10],
        "embarked": fila[11],
    }
    return dic


def leer_csv(nombre: str):
    with open(nombre, 'r', newline='') as csv_file:
        lector = csv.reader(csv_file, delimiter=',')
        valores = list(lector)  # list de listado
        valores.pop(0)  # eliminar el encabezado (el primer elemento de la lista)
        valores2 = list(map(procesar_linea_csv, valores))  # list de diccionario
        return valores2


def guardar_csv(nombre: str, pasajeros: list):
    with open(nombre, 'w', newline='') as csv_file:
        escritura = csv.writer(csv_file)
        escritura.writerow(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex',
                            'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
        for pasajero in pasajeros:  # pasajeros es una lista de diccionario, por lo tanto pasajero un diccionario
            escritura.writerow(pasajero.values())


def filtrar_por_sexo(pasajero: dict, sexo: str):
    if pasajero['sex'] == sexo:
        return True
    else:
        return False


def filtar_pasajeros(pasajeros: list, sexo: str):
    return list(filter(lambda pasajero: filtrar_por_sexo(pasajero, sexo), pasajeros))

# lambda pasajero: filtrar_por_sexo(pasajero, sexo)
# "operacion lambda: voy a llamar a la funcion fitrar_por_sexo por cada uno de los pasajeros.
#                   y cada elemento que voy a leer, lo voy a llamar pasajero.


def actualizar_tarifa_por_pasajero(pasajero: dict):
    pasajero['fare'] = pasajero['fare'] * decimal.Decimal("28.4")
    return pasajero


def actualizar_tarifa_pasajeros(pasajeros: list):
    return list(map(actualizar_tarifa_por_pasajero, pasajeros))

def calcular_total(tarifa:decimal.Decimal,sumatoria:dict):
    return {"fare":tarifa+sumatoria['fare']}

def total_tarifa(pasajeros: list):
    return reduce(lambda pasajero,sumatoria: calcular_total(pasajero['fare'],sumatoria), pasajeros)