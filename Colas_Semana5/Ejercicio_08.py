from queue_structure import Queue


def sacar_ceros(cola):

    if cola.is_empty():
        print("La cola está vacía")
        return Queue()

    temporal = Queue()
    resultado = Queue()

    # Recorrer la cola original
    while not cola.is_empty():

        elemento = cola.dequeue()
        temporal.enqueue(elemento)

        if elemento != 0:
            resultado.enqueue(elemento)

    # Restaurar la cola original
    while not temporal.is_empty():
        cola.enqueue(temporal.dequeue())

    return resultado


# Crear la cola
cola = Queue()

# Agregar elementos
cola.enqueue(10)
cola.enqueue(0)
cola.enqueue(20)
cola.enqueue(0)
cola.enqueue(30)

print("Cola original antes:", end=" ")

temporal = Queue()

while not cola.is_empty():
    elemento = cola.dequeue()
    print(elemento, end=" ")
    temporal.enqueue(elemento)

while not temporal.is_empty():
    cola.enqueue(temporal.dequeue())

print()


# Ejecutar el ejercicio
resultado = sacar_ceros(cola)

print("Cola sin ceros:", end=" ")

temporal = Queue()

while not resultado.is_empty():
    elemento = resultado.dequeue()
    print(elemento, end=" ")
    temporal.enqueue(elemento)

while not temporal.is_empty():
    resultado.enqueue(temporal.dequeue())

print()


# Comprobar que la cola original no cambió
print("Cola original después:", end=" ")

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
sacar_ceros(cola_vacia)