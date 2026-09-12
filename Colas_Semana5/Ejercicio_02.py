from queue_structure import Queue


def imprimir_cantidad(cola):

    if cola.is_empty():
        print("La cola está vacía")
        return

    print("Cantidad de elementos:", cola.size())


# Crear la cola
cola = Queue()

# Agregar elementos
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.enqueue(40)

# Mostrar la cantidad
imprimir_cantidad(cola)


# Probar con una cola vacía
cola_vacia = Queue()

print("\nPrueba con cola vacía:")
imprimir_cantidad(cola_vacia)