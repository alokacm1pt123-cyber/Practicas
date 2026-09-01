#Pila de nombres (primer nombre de personas) con menú de opciones
#Usa una lista de Python como estructura de pila (LIFO).

def agregar_nombre(pila):
    """Pide un nombre por teclado y lo agrega (apila) al tope."""
    nombre = input("Escribe el nombre a agregar: ").strip()
    if nombre == "":
        print("  -> No escribiste nada, no se agregó.")
        return
    pila.append(nombre)  # append = apilar (push)
    print(f"  -> '{nombre}' agregado a la pila.")


def eliminar_nombre(pila):
    """Elimina (desapila) el nombre que está en la cima de la pila."""
    if not pila:
        print("La pila está vacía, no hay nada que eliminar.")
        return
    eliminado = pila.pop()  # pop = desapilar, quita y devuelve el último
    print(f"  -> '{eliminado}' fue eliminado de la pila.")


def mostrar_cima(pila):
    """Muestra el último elemento agregado (la cima), sin quitarlo."""
    if not pila:
        print("La pila está vacía.")
        return
    print(f"El elemento en la cima es: {pila[-1]}")


def buscar_nombre(pila):
    """Busca un nombre dentro de la pila y dice si está y en qué posición."""
    nombre = input("¿Qué nombre quieres buscar?: ").strip()
    if nombre in pila:
        # Buscamos la posición contando desde la cima (índice 1 = tope)
        posicion_desde_cima = len(pila) - pila.index(nombre)
        print(f"  -> '{nombre}' SÍ está en la pila (a {posicion_desde_cima} lugar(es) de la cima).")
    else:
        print(f"  -> '{nombre}' no se encuentra en la pila.")


def contar_elementos(pila):
    """Muestra cuántos elementos hay actualmente en la pila."""
    print(f"La pila tiene {len(pila)} elemento(s).")


def mostrar_elementos(pila):
    """Muestra todos los elementos, del tope (último agregado) hacia la base."""
    if not pila:
        print("La pila está vacía.")
        return
    print("Elementos de la pila (de tope a base):")
    for i in range(len(pila) - 1, -1, -1):
        marca = "  <- cima" if i == len(pila) - 1 else ""
        print(f"  {pila[i]}{marca}")


def limpiar_pila(pila):
    """Elimina todos los elementos de la pila."""
    pila.clear()
    print("  -> La pila fue vaciada por completo.")


def mostrar_menu():
    """Imprime el menú de opciones."""
    print("\n*** Menú de Opciones ***")
    print("1. Agregar un nombre a la Pila")
    print("2. Eliminar un nombre a la Pila")
    print("3. Mostrar el último elemento en la Cima")
    print("4. Buscar un elemento en la Pila")
    print("5. Contar cuantos elementos tiene la Pila")
    print("6. Mostrar todos los elementos de la pila")
    print("7. Limpiar la Pila")
    print("8. Salir")


def main():
    pila = []  # aquí se guardan los nombres; empieza vacía

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-8): ")

        if opcion == "1":
            agregar_nombre(pila)
        elif opcion == "2":
            eliminar_nombre(pila)
        elif opcion == "3":
            mostrar_cima(pila)
        elif opcion == "4":
            buscar_nombre(pila)
        elif opcion == "5":
            contar_elementos(pila)
        elif opcion == "6":
            mostrar_elementos(pila)
        elif opcion == "7":
            limpiar_pila(pila)
        elif opcion == "8":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, elige un número del 1 al 8.")


if __name__ == "__main__":
    main()