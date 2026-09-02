#Lista oficial de los 15 departamentos de Nicaragua, escritos tal
# como deben ingresarse (con mayúscula inicial y tildes correctas).
DEPARTAMENTOS_VALIDOS = {
    "Boaco",
    "Carazo",
    "Chinandega",
    "Chontales",
    "Estelí",
    "Granada",
    "Jinotega",
    "León",
    "Madriz",
    "Managua",
    "Masaya",
    "Matagalpa",
    "Nueva Segovia",
    "Río San Juan",
    "Rivas",
}


def es_departamento_valido(nombre):
    """Verifica si el nombre corresponde exactamente a un departamento de Nicaragua."""
    return nombre in DEPARTAMENTOS_VALIDOS


def agregar(pila, departamento):
    """Agrega (push) un departamento a la cima de la pila, si es válido."""
    if not es_departamento_valido(departamento):
        print("Por favor ingresa solo departamentos de Nicaragua ")
        return
    pila.append(departamento)
    print(f"'{departamento}' se agregó a la pila.")


def eliminar(pila):
    """Elimina (pop) el departamento que está en la cima de la pila."""
    if not pila:
        print("La pila está vacía. No hay nada que eliminar.")
    else:
        eliminado = pila.pop()
        print(f"Se eliminó '{eliminado}' de la pila.")


def mostrar_cima(pila):
    """Muestra el departamento en la cima de la pila, sin eliminarlo."""
    if not pila:
        print("La pila está vacía.")
    else:
        print(f"El departamento en la cima es: '{pila[-1]}'")


def buscar(pila, departamento):
    """Busca si un departamento existe dentro de la pila."""
    if not es_departamento_valido(departamento):
        print("Por favor ingresa solo departamentos de Nicaragua ")
        return
    if departamento in pila:
        print(f"'{departamento}' SÍ está en la pila.")
    else:
        print(f"'{departamento}' NO está en la pila.")


def contar(pila):
    """Cuenta cuántos departamentos hay actualmente en la pila."""
    print(f"La pila tiene {len(pila)} departamento(s).")


def mostrar_todos(pila):
    """Imprime todos los departamentos, de la cima hacia la base."""
    if not pila:
        print("La pila está vacía.")
    else:
        print("Contenido de la pila (de la cima a la base):")
        for departamento in reversed(pila):
            print(f"  -> {departamento}")


def limpiar(pila):
    """Vacía por completo la pila."""
    pila.clear()
    print("La pila fue vaciada.")


def mostrar_menu():
    print("\n===== PILA DE DEPARTAMENTOS DE NICARAGUA =====")
    print("1. Agregar departamento")
    print("2. Eliminar departamento")
    print("3. Mostrar cima")
    print("4. Buscar departamento")
    print("5. Contar departamentos")
    print("6. Mostrar todos")
    print("7. Limpiar pila")
    print("8. Salir")
    print("===============================================")


def main():
    pila = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ").strip()

        if opcion == "1":
            departamento = input("Nombre del departamento: ").strip()
            if departamento:
                agregar(pila, departamento)
            else:
                print("El nombre no puede estar vacío.")
        elif opcion == "2":
            eliminar(pila)
        elif opcion == "3":
            mostrar_cima(pila)
        elif opcion == "4":
            departamento = input("Departamento a buscar: ").strip()
            buscar(pila, departamento)
        elif opcion == "5":
            contar(pila)
        elif opcion == "6":
            mostrar_todos(pila)
        elif opcion == "7":
            limpiar(pila)
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()