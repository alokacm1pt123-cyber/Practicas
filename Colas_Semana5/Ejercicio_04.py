from queue_structure import Queue


def colocar_menor_al_frente(cola):

    if cola.is_empty():
        print("La cola está vacía")
        return

    temporal = Queue()
    menor = None

    # Buscar el número menor
    while not cola.is_empty():
        elemento = cola.dequeue()

        if menor is None or elemento < menor:
            menor = elemento

        temporal.enqueue(elemento)

    # Regresar los elementos excepto el menor
    menor_eliminado = False

    while not temporal.is_empty():
        elemento = temporal.dequeue()

        if elemento == menor and not menor_eliminado:
            menor_eliminado = True
        else:
            cola.enqueue(elemento)

    # Colocar el menor en la cima
    cola_temp = Queue()

    while not cola.is_empty():
        cola_temp.enqueue(cola.dequeue())

    cola.enqueue(menor)

    while not cola_temp.is_empty():
        cola.enqueue(cola_temp.dequeue())


# Crear la cola
cola = Queue()

# Agregar elementos
cola.enqueue(20)
cola.enqueue(40)
cola.enqueue(10)
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
colocar_menor_al_frente(cola)

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
colocar_menor_al_frente(cola_vacia)