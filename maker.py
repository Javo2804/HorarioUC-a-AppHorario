from plistlib import dump
import requests
import json
from funciones import *
import valores as v

print(f'''============================================
Horario UC a App | Versión 2.0
Creado por: Javier Zepeda Avello – javier@uc.cl
''')

dicc = dict(
    Settings = dict(
        ColorSettings = dict(),
        NumberOfWeeks = 1,
        SelectedWeek = 0,
        WeekendDaysAreActive = True
        ),
    TaskCategories = [],
    TaskEvents = [],
    WeekEvents = []
    )

url = "https://api.jsonbin.io/b/5f5b9546ad23b57ef91037e3/1"
data0 = requests.get(url)
data = data0.json()
semestre = data['semestre_actual']

cond = True
lista_nrc = []
print("Ingrese los NRC de los cursos que desea agregar. Para finalizar, ingrese un 0 (cero).")
while cond:
    nrc = input("Ingrese NRC: ")
    if nrc == "0" or nrc == "":
        print("== Revisando los NRC ==")
        if len(lista_nrc)>0:
            revision, pre_ramos = check_all_nrc(lista_nrc, semestre)
            if revision['status'] == "ok":
                cond = False
                print(f'''Se han ingresado los NRC correctamente: {lista_nrc}''')
            else:
                print(f"Hay al menos un NRC que no existe.\nNRC Correctos:   {revision['good']}\nNRC Incorrectos: {revision['fix']}\n¡Ingrese todos los NRC nuevamente!\n")
                lista_nrc = []
        else:
            print("No se ha almacenado ningún NRC.")
            exit()
    elif nrc.isnumeric() and len(nrc)==5:
        if nrc in lista_nrc:
            print("NRC repetido")
        else:
            lista_nrc.append(nrc)
    else:
        print("Ingrese un NRC válido...")

ramos = []
for pre_ramo in pre_ramos:
    ramo = pre_ramo['data']
    for x in ramo:
        y = ramo[x]
        for z in y:
            ramos.append(y[z])

print(ramos)





# nuevo_ramo(dicc)
# cond = True
# while cond:
#     new = input("¿Desea añadir un nuevo curso? (S/n): ")
#     if sino(new) and new!="":
#         nuevo_ramo(archivo)
#     elif new == "":
#         cond = True
#     else:
#         cond = False

# fileName = "archivoGenerado.timetable"

# with open(fileName, 'wb+') as fp:
#     dump(archivo, fp)
