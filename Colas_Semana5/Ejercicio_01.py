from queue_structure import Queue


def imprimir_primero(cola):

    if cola.is_empty():
        print("La cola está vacía")
        return

    print("Primer elemento:", cola.front())


# Crear la cola
cola = Queue()

# Agregar elementos
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)

print("Primer elemento antes de consultar:", cola.front())

imprimir_primero(cola)

print("Primer elemento después de consultar:", cola.front())


# Probar con una cola vacía
cola_vacia = Queue()

print("\nPrueba con cola vacía:")
imprimir_primero(cola_vacia)