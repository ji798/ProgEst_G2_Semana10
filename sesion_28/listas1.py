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

print(insertar_inicio(None, 5))
print(insertar_inicio(5, 8))
print(insertar_final(None, 10))
print(insertar_final(insertar_inicio(None, 5), 10))