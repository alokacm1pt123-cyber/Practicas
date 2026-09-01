#Pila de números enteros con menú de opciones
#Usa una lista de Python como estructura de pila (LIFO: el último
#número que entra es el primero en "salir" conceptualmente).


def agregar_numeros(pila):
    """Pide números al usuario por teclado y los agrega (apila) uno por uno."""
    while True:
        entrada = input("Ingresa un número entero (o 'fin' para terminar): ")
        if entrada.lower() == "fin":
            break
        try:
            numero = int(entrada)
            pila.append(numero)
            print(f"  -> {numero} agregado a la pila.")
        except ValueError:
            print("  -> Eso no es un número entero. Intenta de nuevo.")


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
        print(f"  {pila[i]}")


def promedio_numeros(pila):
    """Calcula y muestra el promedio de los números en la pila."""
    if not pila:
        print("La pila está vacía, no se puede calcular un promedio.")
        return
    promedio = sum(pila) / len(pila)
    print(f"Promedio: {promedio:.2f}")


def mostrar_menu():
    """Imprime el menú de opciones."""
    print("\n*** Menú de Opciones ***")
    print("1. Agregar números")
    print("2. Contar elementos")
    print("3. Mostrar todos los elementos")
    print("4. Promedio de todos los números")
    print("5. Salir del sistema")


def main():
    pila = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            agregar_numeros(pila)
        elif opcion == "2":
            contar_elementos(pila)
        elif opcion == "3":
            mostrar_elementos(pila)
        elif opcion == "4":
            promedio_numeros(pila)
        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, elige un número del 1 al 5.")

if __name__ == "__main__":
    main()