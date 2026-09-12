from queue_structure import Queue
import math


def crear_cola_raices(cola):

    if cola.is_empty():
        print("La cola está vacía")
        return Queue()

    temporal = Queue()
    resultado = Queue()

    # Recorrer la cola original
    while not cola.is_empty():
        numero = cola.dequeue()

        temporal.enqueue(numero)
        resultado.enqueue(math.sqrt(numero))

    # Restaurar la cola original
    while not temporal.is_empty():
        cola.enqueue(temporal.dequeue())

    return resultado


# Crear la cola de enteros
cola = Queue()

# Agregar valores
cola.enqueue(4)
cola.enqueue(9)
cola.enqueue(16)
cola.enqueue(25)

print("Cola original antes:", end=" ")

temporal = Queue()

while not cola.is_empty():
    numero = cola.dequeue()
    print(numero, end=" ")
    temporal.enqueue(numero)

while not temporal.is_empty():
    cola.enqueue(temporal.dequeue())

print()


# Crear la cola con las raíces cuadradas
resultado = crear_cola_raices(cola)

print("Cola de raíces cuadradas:", end=" ")

temporal = Queue()

while not resultado.is_empty():
    raiz = resultado.dequeue()
    print(raiz, end=" ")
    temporal.enqueue(raiz)

while not temporal.is_empty():
    resultado.enqueue(temporal.dequeue())

print()


# Comprobar que la cola original no cambió
print("Cola original después:", end=" ")

temporal = Queue()

while not cola.is_empty():
    numero = cola.dequeue()
    print(numero, end=" ")
    temporal.enqueue(numero)

while not temporal.is_empty():
    cola.enqueue(temporal.dequeue())

print()


# Probar con una cola vacía
cola_vacia = Queue()

print("\nPrueba con cola vacía:")
crear_cola_raices(cola_vacia)