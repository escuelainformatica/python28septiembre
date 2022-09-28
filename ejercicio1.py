import csv

from ejercicio1_funciones import leer_csv, filtar_pasajeros, guardar_csv, actualizar_tarifa_pasajeros, total_tarifa

#   0            1       2      3   4   5    6    7     8       9    10   11
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# 1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
#

# (1,0,3,"aaa"....)  -> {"id":1,"sobrevivio":2,....}




todos_pasajeros=leer_csv('titanic-train.csv')

pasajeros_mujeres=filtar_pasajeros(todos_pasajeros,'female')
pasajeros_hombres=filtar_pasajeros(todos_pasajeros,'male')

pasajeros_mujeres=actualizar_tarifa_pasajeros(pasajeros_mujeres)

guardar_csv('solo_female.csv',pasajeros_mujeres)

print(f"pasajeros en total  {len(todos_pasajeros)}")
print(f"pasajeros que eran mujeres  {len(pasajeros_mujeres)}")
print(f"pasajeros que eran hombres  {len(pasajeros_hombres)}")

print(total_tarifa(todos_pasajeros))
