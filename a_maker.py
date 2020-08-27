from plistlib import *
from funciones import *
import valores as v
from about import *

print(f'''============================================
Creador de Horario | Versión {version}
Creado por: Javier Zepeda Avello – javier@uc.cl

''')

#Lo que se debe actualizar es: ColorSettings y WeekEvents
archivo = dict(
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

nuevo_ramo(archivo)
cond = True
while cond:
    new = input("¿Desea añadir un nuevo curso? (S/n): ")
    if sino(new) and new!="":
        nuevo_ramo(archivo)
    elif new == "":
        cond = True
    else:
        cond = False



#fileName = "Timetable.timetable"

#with open(fileName, 'rb') as fp:
#    pl = load(fp)
#hor = pl["WeekEvents"]

fileName = "archivoGenerado.timetable"

with open(fileName, 'wb+') as fp:
    dump(archivo, fp)
