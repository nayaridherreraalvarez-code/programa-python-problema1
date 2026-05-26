# ============================================
# FASE 5 - EVALUACION FINAL POA
# PROBLEMA 1
# Clasificación de compromiso de clientes
# ============================================

clientes = [
    ["C001", 250, 10],
    ["C002", 40, 2],
    ["C003", 120, 5],
    ["C004", 300, 12],
    ["C005", 55, 1]
]

def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


print("====================================")
print(" INFORME DE COMPROMISO DE CLIENTES ")
print("====================================")

for cliente in clientes:

    id_cliente = cliente[0]
    duracion = cliente[1]
    clics = cliente[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("Cliente:", id_cliente)
    print("Duracion:", duracion, "segundos")
    print("Clics:", clics)
    print("Clasificacion:", clasificacion)
    print("------------------------------------")
