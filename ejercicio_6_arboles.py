from collections import deque


class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)
        # Los valores duplicados no se insertan.

    def buscar(self, valor):
        actual = self.raiz
        while actual is not None:
            if valor == actual.valor:
                return True
            actual = actual.izquierdo if valor < actual.valor else actual.derecho
        return False

    def inorden(self):
        resultado = []

        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.izquierdo)
                resultado.append(nodo.valor)
                recorrer(nodo.derecho)

        recorrer(self.raiz)
        return resultado

    def eliminar(self, valor):
        """Elimina un valor y devuelve True si se encontró."""
        self.raiz, eliminado = self._eliminar_recursivo(self.raiz, valor)
        return eliminado

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return None, False

        if valor < nodo.valor:
            nodo.izquierdo, eliminado = self._eliminar_recursivo(
                nodo.izquierdo, valor
            )
            return nodo, eliminado

        if valor > nodo.valor:
            nodo.derecho, eliminado = self._eliminar_recursivo(
                nodo.derecho, valor
            )
            return nodo, eliminado

        # Caso 1: nodo hoja.
        if nodo.izquierdo is None and nodo.derecho is None:
            return None, True

        # Caso 2: el nodo tiene un solo hijo.
        if nodo.izquierdo is None:
            return nodo.derecho, True
        if nodo.derecho is None:
            return nodo.izquierdo, True

        # Caso 3: dos hijos. Se usa el sucesor inorden.
        sucesor = nodo.derecho
        while sucesor.izquierdo is not None:
            sucesor = sucesor.izquierdo

        nodo.valor = sucesor.valor
        nodo.derecho, _ = self._eliminar_recursivo(
            nodo.derecho, sucesor.valor
        )
        return nodo, True

    def por_niveles(self):
        """Recorrido BFS usando una cola."""
        if self.raiz is None:
            return []

        resultado = []
        cola = deque([self.raiz])

        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)

            if nodo.izquierdo is not None:
                cola.append(nodo.izquierdo)
            if nodo.derecho is not None:
                cola.append(nodo.derecho)

        return resultado

    def suma(self):
        """Suma los valores sin modificar el árbol."""
        def sumar(nodo):
            if nodo is None:
                return 0
            return nodo.valor + sumar(nodo.izquierdo) + sumar(nodo.derecho)

        return sumar(self.raiz)

    def es_completo(self):
        """Según el enunciado: cada nodo tiene 0 o 2 hijos."""
        def comprobar(nodo):
            if nodo is None:
                return True

            tiene_izquierdo = nodo.izquierdo is not None
            tiene_derecho = nodo.derecho is not None

            if tiene_izquierdo != tiene_derecho:
                return False

            return comprobar(nodo.izquierdo) and comprobar(nodo.derecho)

        return comprobar(self.raiz)

    def altura(self):
        """Altura medida en aristas: árbol vacío = -1."""
        def calcular(nodo):
            if nodo is None:
                return -1
            return 1 + max(calcular(nodo.izquierdo), calcular(nodo.derecho))

        return calcular(self.raiz)


def balancear_arbol(arbol):
    """Devuelve un árbol nuevo balanceado, sin modificar el original."""
    valores = arbol.inorden()
    nuevo = ArbolBinarioBusqueda()

    def construir(inicio, fin):
        if inicio > fin:
            return None

        medio = (inicio + fin) // 2
        nodo = NodoArbol(valores[medio])
        nodo.izquierdo = construir(inicio, medio - 1)
        nodo.derecho = construir(medio + 1, fin)
        return nodo

    nuevo.raiz = construir(0, len(valores) - 1)
    return nuevo


if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    for numero in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(numero)

    print("Árbol original (inorden):", arbol.inorden())
    print("Recorrido por niveles (BFS):", arbol.por_niveles())
    print("Suma de los valores:", arbol.suma())
    print("¿Cada nodo tiene 0 o 2 hijos?:", arbol.es_completo())
    print("Altura original:", arbol.altura())

    print("\nEliminando 30:", arbol.eliminar(30))
    print("Después de eliminar (inorden):", arbol.inorden())

    balanceado = balancear_arbol(arbol)
    print("\nÁrbol balanceado (inorden):", balanceado.inorden())
    print("Altura del árbol balanceado:", balanceado.altura())
    print("El árbol original sigue siendo independiente:", arbol.inorden())
