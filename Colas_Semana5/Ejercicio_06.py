from queue_structure import Queue


def colocar_primer_a_al_fondo(cola):

    if cola.is_empty():
        print("La cola está vacía")
        return

    temporal = Queue()
    nombre_a = None

    # Buscar el primer nombre que inicia con A
    while not cola.is_empty():
        nombre = cola.dequeue()

        if nombre_a is None and nombre.upper().startswith("A"):
            nombre_a = nombre
        else:
            temporal.enqueue(nombre)

    # Restaurar los demás elementos
    while not temporal.is_empty():
        cola.enqueue(temporal.dequeue())

    # Colocar el primer nombre con A en el fondo
    if nombre_a is not None:
        cola.enqueue(nombre_a)
        print("Nombre colocado en el fondo:", nombre_a)
    else:
        print("No se encontró un nombre que inicie con A")


# Crear la cola
cola = Queue()

# Agregar nombres
cola.enqueue("Carlos")
cola.enqueue("Ana")
cola.enqueue("Pedro")
cola.enqueue("Andrea")
cola.enqueue("Luis")

print("Cola antes:", end=" ")

temporal = Queue()

while not cola.is_empty():
    nombre = cola.dequeue()
    print(nombre, end=" ")
    temporal.enqueue(nombre)

while not temporal.is_empty():
    cola.enqueue(temporal.dequeue())

print()

# Ejecutar el ejercicio
colocar_primer_a_al_fondo(cola)

print("Cola después:", end=" ")

temporal = Queue()

while not cola.is_empty():
    nombre = cola.dequeue()
    print(nombre, end=" ")
    temporal.enqueue(nombre)

while not temporal.is_empty():
    cola.enqueue(temporal.dequeue())

print()


# Probar con una cola vacía
cola_vacia = Queue()

print("\nPrueba con cola vacía:")
colocar_primer_a_al_fondo(cola_vacia)