from queue_structure import Queue


def invertir_cola(cola):

    if cola.is_empty():
        print("La cola está vacía")
        return

    temporal = Queue()
    invertida = Queue()

    # Pasar los elementos a una cola temporal
    while not cola.is_empty():
        temporal.enqueue(cola.dequeue())

    # Sacar los elementos desde el final
    while not temporal.is_empty():

        auxiliar = Queue()

        while temporal.size() > 1:
            auxiliar.enqueue(temporal.dequeue())

        ultimo = temporal.dequeue()
        invertida.enqueue(ultimo)

        while not auxiliar.is_empty():
            temporal.enqueue(auxiliar.dequeue())

    # Pasar la cola invertida a la cola original
    while not invertida.is_empty():
        cola.enqueue(invertida.dequeue())


# Crear la cola
cola = Queue()

# Agregar elementos
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.enqueue(40)

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
invertir_cola(cola)

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
invertir_cola(cola_vacia)