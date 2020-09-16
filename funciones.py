import valores as v
import requests

def check_nrc(nrc, semestre):
    api_url = "https://bc.horariomaker.com/api/v3"
    parametros = {"nrc": f"{nrc}", "semestre": f"{semestre}"}
    unprocessed = requests.get(api_url, parametros)
    data = unprocessed.json()
    if nrc.isalpha() or len(nrc) != 5:
        return "fix", data
    if data['status'].lower() == "ok":
        return "ok", data
    elif data['status'].lower() == "accepted":
        return "fix", data
    else:
        return "bad", data

def check_all_nrc(lista, semestre):
    ramos = []
    for i in lista:
        status, data = check_nrc(i, semestre)
        ramos.append(data)
        good_nrc = []
        fix_nrc = []
        # bad_nrc = []
        if status == "ok":
            good_nrc.append(i)
        elif status == "fix":
            fix_nrc.append(i)      
    return {"status": status, "good": good_nrc, "fix": fix_nrc}, ramos

def dia_num(dia):
    x = ["L","M","W","J","V","S"]
    if dia in x:
        indice = x.index(dia)
    return indice

def num_mod(mod):
    return "mod"+mod

def sino(string):
    if string.lower() in ["s","y","si","yes"]:
        return True
    elif string.lower() in ["n","no"]:
        return False

def read_mod(string):
    # Se mantiene en v2.0
    horario = string.split(":")
    dias = horario[0].split("-")
    modulos = horario[1].split(",")
    dias2 = []
    modulos2 = []
    for dia in dias:
        dias2.append(dia_num(dia))
    for modulo in modulos:
        modulos2.append(num_mod(modulo))
    return {"dias": dias2, "modulos": modulos2}

def procesar_ramos(lista):
    for ramo in lista:
        nombre = ramo['Nombre']
        sigla = ramo['Sigla']
        nrc = ramo['NRC']
        modulos = {}
        for i in ramo['Modulos']:
            if len(i)>0:
                pass
                # modulos = 


# FUNCIÓN DE v1.0
# def read_horario(supstr):
#     resultado = dict(
#         CLAS = {"existe": False},
#         AYU = {"existe": False},
#         LAB = {"existe": False},
#         TER = {"existe": False},
#         TAL = {"existe": False},
#         PRA = {"existe": False},
#         TES = {"existe": False},
#         SUP = {"existe": False},
#         LIB = {"existe": False}
#         )
#     lineas = supstr.split("\n")
#     for z in lineas:
#         linea = z.split("\t")
#         horario = linea[0]
#         tipo = linea[1]
#         sala = linea[2]
#         if horario != ":":
#             horario = read_mod(horario)
#             resultado[tipo]["existe"] = True
#             resultado[tipo].update(horario)
#             resultado[tipo]["sala"] = sala
#     return resultado

# def nuevo_ramo(file):
#     print("=== Ingrese los datos del curso a añadir ===")
#     nombre = input("Nombre: ")
#     str_horario = ""
#     n = int(input("Tipos de horario: "))
#     print("Ingrese la(s) linea(s) de horario abajo (número):")
#     for i in range(n):
#         x = input()
#         if i < n-1:
#             str_horario += x+"\n"
#         else:
#             str_horario += x
#     horario = read_horario(str_horario)
#     def_bloques(file, nombre, horario)

def def_pre(tipo):
    if tipo != "CLAS":
        if tipo in ["TER", "TES", "OTRO"]:
            pre = f"[{tipo}] "
        else:
            pre = f"[{tipo[0]}] "
    else:
        pre = ""
    return pre

def def_color(file, nombre, tipo):
    pre = def_pre(tipo)
    file["Settings"]["ColorSettings"][f"{pre}{nombre}"] = v.colores[f"{tipo}"]

def def_bloques(file, nombre, horario):
    for tipo in horario:
        if horario[tipo]["existe"]:
            pre = def_pre(tipo)
            if horario[tipo]["sala"] != "SIN SALA":
                sala = f"Sala: {horario[tipo]['sala']}"
            else:
                sala = "SIN SALA"
            def_color(file, nombre, tipo)
            for dia in horario[tipo]["dias"]:
                for modulo in horario[tipo]["modulos"]:
                    bloque = dict(
                        dayNum = int(dia),
                        endTime = float(v.modulos[modulo]["endTime"]),
                        info = f"{sala}",
                        time = float(v.modulos[modulo]["time"]),
                        title = f"{pre}{nombre}",
                        weekNum = 0
                        )
                    file["WeekEvents"].append(bloque)


