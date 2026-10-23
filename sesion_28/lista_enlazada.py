def crear_nodo(dato):
    return {"dato": dato, "siguiente": None}

def insertar_inicio(lista, dato):
    nuevo = crear_nodo(dato)
    nuevo["siguiente"] = lista
    return nuevo

def insertar_final(cabeza, dato):
    nuevo = crear_nodo(dato)
    if cabeza is None:
        return nuevo
    actual = cabeza
    while actual["siguiente"] is not None:
        actual = actual["siguiente"]
    actual["siguiente"] = nuevo
    return cabeza

def mostrar(cabeza):
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end=" → ")
        actual = actual["siguiente"]
    print("None")

def eliminar(cabeza, dato):
    if cabeza is None:
        return None, False
    if cabeza["dato"] == dato:
        return cabeza["siguiente"], True
    anterior = cabeza
    actual = cabeza["siguiente"]
    while actual is not None:
        if actual["dato"] == dato:
            anterior["siguiente"] = actual["siguiente"]
            return cabeza, True
        anterior = actual
        actual = actual["siguiente"]
    return cabeza, False

def buscar(cabeza, dato):
    actual = cabeza
    posicion = 0
    while actual is not None:
        if actual["dato"] == dato:
            return posicion
        actual = actual["siguiente"]
        posicion += 1
    return -1

def contar(cabeza):
    total = 0
    actual = cabeza
    while actual is not None:
        total += 1
        actual = actual["siguiente"]
    return total

cabeza = None
cabeza = insertar_final(cabeza, "Ana")
cabeza = insertar_final(cabeza, "Luis")
cabeza = insertar_inicio(cabeza, "Marta")
mostrar(cabeza)
print("Posición de Luis:", buscar(cabeza, "Luis"))
cabeza, eliminado = eliminar(cabeza, "Ana")
print("¿Se eliminó Ana?", eliminado)
mostrar(cabeza)
print("Total:", contar(cabeza))