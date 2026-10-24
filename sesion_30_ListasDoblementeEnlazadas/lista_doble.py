#Antes de ejecutarlo: ¿qué ocurre si olvidas cola["siguiente"] = nuevo?
"""al olvidar cola["siguiente"] = nuevo, el recorrido inverso aún puede funcionar, pero el recorrido hacia adelante se interrumpe."""
cabeza = None
cola = None

def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}

def agregar_final(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)
    if cabeza is None:
        cabeza = nuevo
        cola = nuevo
    else:
        nuevo["anterior"] = cola
        """cola["siguiente"] = nuevo"""
        cola = nuevo


agregar_final("Inicio")
agregar_final("Catálogo")
agregar_final("Contacto")

#Predice ambas salidas antes de ejecutar. ¿Por qué el segundo recorrido comienza en cola?
""""""

def mostrar_adelante():
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end=" ↔ " if actual["siguiente"] else "\n")
        actual = actual["siguiente"]

def mostrar_atras():
    actual = cola
    while actual is not None:
        print(actual["dato"], end=" ↔ " if actual["anterior"] else "\n")
        actual = actual["anterior"]

mostrar_adelante()
mostrar_atras()

#Prueba la función también con una lista vacía. Explica por qué se actualizan cabeza y cola.
""""""

def agregar_inicio(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)
    if cabeza is None:
        cabeza = cola = nuevo
    else:
        nuevo["siguiente"] = cabeza
        cabeza["anterior"] = nuevo
        cabeza = nuevo

agregar_inicio("Bienvenida")
mostrar_adelante()
mostrar_atras()

#Prueba eliminar el primer nodo, el último, uno inexistente y el único nodo de una lista nueva. ¿Qué casos requieren especial cuidado?
""""""

def eliminar(dato):
    global cabeza, cola
    actual = cabeza
    while actual is not None and actual["dato"] != dato:
        actual = actual["siguiente"]
    if actual is None:
        return False

    anterior = actual["anterior"]
    siguiente = actual["siguiente"]
    if anterior is None:
        cabeza = siguiente
    else:
        anterior["siguiente"] = siguiente
    if siguiente is None:
        cola = anterior
    else:
        siguiente["anterior"] = anterior
    return True

print("Eliminado:", eliminar("Catálogo"))
mostrar_adelante()
mostrar_atras()