from queue_structure import Queue


def colocar_mayor_al_fondo(cola):

    if cola.is_empty():
        print("La cola está vacía")
        return

    temporal = Queue()
    mayor = None

    # Buscar el número mayor
    while not cola.is_empty():
        elemento = cola.dequeue()

        if mayor is None or elemento > mayor:
            mayor = elemento

        temporal.enqueue(elemento)

    # Regresar los elementos excepto el mayor
    mayor_eliminado = False

    while not temporal.is_empty():
        elemento = temporal.dequeue()

        if elemento == mayor and not mayor_eliminado:
            mayor_eliminado = True
        else:
            cola.enqueue(elemento)

    # Colocar el mayor en el fondo
    cola.enqueue(mayor)


# Crear la cola
cola = Queue()

# Agregar elementos
cola.enqueue(10)
cola.enqueue(40)
cola.enqueue(20)
cola.enqueue(30)

print("Cola antes:", end=" ")

temporal = Queue()

while not cola.is_empty():
    elemento = cola.dequeue()
    print(elemento, end=" ")
    temporal.enqueue(elemento)

while not temporal.is_empty():
    cola.enqueue(temporal.dequeue())

print()

# Ejecutar el ejercicio
colocar_mayor_al_fondo(cola)

print("Cola después:", end=" ")

temporal = Queue()

while not cola.is_empty():
    elemento = cola.dequeue()
    print(elemento, end=" ")
    temporal.enqueue(elemento)

while not temporal.is_empty():
    cola.enqueue(temporal.dequeue())

print()


# Probar con una cola vacía
cola_vacia = Queue()

print("\nPrueba con cola vacía:")
colocar_mayor_al_fondo(cola_vacia)