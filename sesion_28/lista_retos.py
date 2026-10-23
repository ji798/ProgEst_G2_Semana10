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

def atender(cabeza):
    if cabeza is None:
        return None, None
    atendido = cabeza["dato"]
    cabeza = cabeza["siguiente"]
    return cabeza, atendido 

def insertar_despues(cabeza, dato, referente):    
    if not referente:
        print("El referente no puede estar vacío.")
        return cabeza
    nuevo = crear_nodo(dato)
    actual = cabeza
    while actual is not None:
        if actual["dato"] == referente:
            nuevo["siguiente"] = actual["siguiente"]
            actual["siguiente"] = nuevo
            return cabeza
        actual = actual["siguiente"]
    print("No se encontró el referente.")
    return cabeza

def invertir_lista(cabeza):
    if cabeza is None:
        print("La lista está vacía, no se puede invertir.")
        return None
     
    if cabeza["siguiente"] is None:
        print("La lista tiene un solo elemento, no se puede invertir.")
        return cabeza
        
    anterior = None
    actual = cabeza
    while actual is not None:
        siguiente = actual["siguiente"]
        actual["siguiente"] = anterior
        anterior = actual
        actual = siguiente
    return anterior

def menu():
    cabeza = None
    while True:
        print("\n1. Agregar turno  2. Mostrar  3. Buscar")
        print("4. Eliminar turno  5. Contar  6. Atender")
        print("7. Insertar después 8. Invertir lista 0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "0":
            break
        if opcion in ("1", "3", "4", "6"):
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("Escriba un nombre.")
                continue
        if opcion == "1":
            cabeza = insertar_final(cabeza, nombre)
        elif opcion == "2":
            mostrar(cabeza)
        elif opcion == "3":
            posicion = buscar(cabeza, nombre)
            if posicion == -1:
                print("No encontrado")
            else:
                print("Posición:", posicion)
        elif opcion == "4":
            cabeza, eliminado = eliminar(cabeza, nombre)
            print("Eliminado" if eliminado else "No encontrado")
        elif opcion == "5":
            print("Total:", contar(cabeza))

        elif opcion == "6":
            cabeza, atendido = atender(cabeza)
            if atendido is not None:
                print("Atendido:", atendido)
            else:
                print("No hay turnos para atender")

        elif opcion == "7":
            nombre = input("Nombre: ").strip()
            nombre_referente = input("Nombre referente: ").strip()
            if not nombre_referente:
                print("Escriba un nombre referente.")
                continue
            cabeza = insertar_despues(cabeza, nombre, nombre_referente)

        elif opcion == "8":
            cabeza = invertir_lista(cabeza)
            
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()