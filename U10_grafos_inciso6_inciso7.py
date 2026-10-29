from collections import deque
import heapq


# ============================================================
# UNIDAD 10: GRAFOS
# Inciso 6: Tarea / Homework
# Inciso 7: Mini-Proyecto Sistema de Navegación GPS
# ============================================================


class Grafo:
    """Grafo representado mediante una lista de adyacencia."""

    def __init__(self, dirigido=False):
        self.adj = {}
        self.dirigido = dirigido

    def agregar_vertice(self, v):
        """Agrega un vértice si no existe."""
        if v not in self.adj:
            self.adj[v] = []

    def agregar_arista(self, u, v):
        """Agrega una arista entre dos vértices."""
        self.agregar_vertice(u)
        self.agregar_vertice(v)

        self.adj[u].append(v)
        if not self.dirigido:
            self.adj[v].append(u)

    def vecinos(self, v):
        """Retorna los vecinos de un vértice."""
        return self.adj.get(v, [])

    def bfs(self, inicio):
        """Recorrido en anchura."""
        if inicio not in self.adj:
            return []

        visitados = {inicio}
        cola = deque([inicio])
        resultado = []

        while cola:
            actual = cola.popleft()
            resultado.append(actual)

            for vecino in self.vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return resultado

    def dfs(self, inicio, visitados=None, resultado=None):
        """Recorrido en profundidad recursivo."""
        if inicio not in self.adj:
            return [] if resultado is None else resultado

        if visitados is None:
            visitados = set()
            resultado = []

        visitados.add(inicio)
        resultado.append(inicio)

        for vecino in self.vecinos(inicio):
            if vecino not in visitados:
                self.dfs(vecino, visitados, resultado)

        return resultado

    # ---------------- Inciso 6.1 ----------------
    def dfs_iterativo(self, inicio):
        """Realiza DFS usando una pila, sin recursividad."""
        if inicio not in self.adj:
            return []

        visitados = set()
        pila = [inicio]
        resultado = []

        while pila:
            actual = pila.pop()

            if actual not in visitados:
                visitados.add(actual)
                resultado.append(actual)

                # Se invierten los vecinos para conservar el orden
                # habitual de recorrido de la lista de adyacencia.
                for vecino in reversed(self.vecinos(actual)):
                    if vecino not in visitados:
                        pila.append(vecino)

        return resultado

    def tiene_ciclo(self):
        """Detecta ciclos en un grafo dirigido mediante DFS."""
        if not self.dirigido:
            raise ValueError(
                "La detección de ciclos de este método requiere "
                "un grafo dirigido."
            )

        # 0 = no visitado, 1 = en proceso, 2 = terminado.
        estado = {v: 0 for v in self.adj}

        def dfs_ciclo(actual):
            estado[actual] = 1

            for vecino in self.adj[actual]:
                if estado[vecino] == 1:
                    return True

                if estado[vecino] == 0 and dfs_ciclo(vecino):
                    return True

            estado[actual] = 2
            return False

        for vertice in self.adj:
            if estado[vertice] == 0 and dfs_ciclo(vertice):
                return True

        return False
    
    def grados(self):
        """Retorna diccionarios con grados de entrada y salida."""
        if not self.dirigido:
            raise ValueError(
                "El cálculo de grados de entrada y salida requiere "
                "un grafo dirigido."
            )

        entrada = {v: 0 for v in self.adj}
        salida = {v: len(vecinos) for v, vecinos in self.adj.items()}

        for vecinos in self.adj.values():
            for vecino in vecinos:
                entrada[vecino] += 1

        return entrada, salida

    def mostrar(self):
        """Muestra la lista de adyacencia."""
        for vertice, vecinos in self.adj.items():
            print(f"{vertice} -> {vecinos}")


class GrafoPonderado(Grafo):
    """Grafo cuyas aristas tienen un peso numérico."""

    def __init__(self, dirigido=False):
        super().__init__(dirigido)

    def agregar_arista(self, u, v, peso):
        """Agrega una arista ponderada."""
        if isinstance(peso, bool) or not isinstance(peso, (int, float)):
            raise ValueError("El peso debe ser un número.")
        if peso < 0:
            raise ValueError("Dijkstra requiere pesos no negativos.")

        self.agregar_vertice(u)
        self.agregar_vertice(v)

        self.adj[u].append((v, peso))
        if not self.dirigido:
            self.adj[v].append((u, peso))

    def vecinos(self, v):
        """Retorna los vecinos sin sus pesos."""
        return [vecino for vecino, peso in self.adj.get(v, [])]

    def dijkstra(self, inicio):
        """Calcula las distancias mínimas desde el nodo inicial."""
        if inicio not in self.adj:
            raise ValueError(f"El vértice '{inicio}' no existe.")

        distancias = {v: float("inf") for v in self.adj}
        distancias[inicio] = 0
        cola = [(0, inicio)]

        while cola:
            dist_actual, actual = heapq.heappop(cola)

            if dist_actual > distancias[actual]:
                continue

            for vecino, peso in self.adj.get(actual, []):
                distancia = dist_actual + peso

                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola, (distancia, vecino))

        return distancias

    # ---------------- Inciso 6.4 ----------------
    def dijkstra_camino(self, inicio, destino):
        """Retorna (camino, distancia); si no existe, (None, infinito)."""
        if inicio not in self.adj or destino not in self.adj:
            return None, float("inf")

        distancias = {v: float("inf") for v in self.adj}
        anteriores = {v: None for v in self.adj}
        distancias[inicio] = 0
        cola = [(0, inicio)]

        while cola:
            dist_actual, actual = heapq.heappop(cola)

            if dist_actual > distancias[actual]:
                continue

            if actual == destino:
                break

            for vecino, peso in self.adj[actual]:
                nueva_distancia = dist_actual + peso

                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = actual
                    heapq.heappush(
                        cola, (nueva_distancia, vecino)
                    )

        if distancias[destino] == float("inf"):
            return None, float("inf")

        camino = []
        actual = destino

        while actual is not None:
            camino.append(actual)
            actual = anteriores[actual]

        camino.reverse()
        return camino, distancias[destino]


# ============================================================
# INCISO 6: EJEMPLOS DE LOS CINCO EJERCICIOS
# ============================================================

def demostrar_inciso_6():
    print("\n" + "=" * 60)
    print("INCISO 6: TAREA / HOMEWORK")
    print("=" * 60)

    # 1. DFS iterativo
    g = Grafo()
    g.agregar_arista("A", "B")
    g.agregar_arista("A", "C")
    g.agregar_arista("B", "D")
    g.agregar_arista("C", "D")
    print("\n1. DFS iterativo desde A:")
    print(g.dfs_iterativo("A"))

    # 2. Detección de ciclos en un grafo dirigido
    gd = Grafo(dirigido=True)
    gd.agregar_arista("A", "B")
    gd.agregar_arista("B", "C")
    gd.agregar_arista("C", "A")
    print("\n2. ¿El grafo dirigido tiene ciclo?")
    print(gd.tiene_ciclo())

    # 3. Grafo ponderado de red de computadoras: latencia en ms
    gp = GrafoPonderado()
    gp.agregar_arista("Router", "Servidor_A", 10)
    gp.agregar_arista("Router", "Servidor_B", 5)
    gp.agregar_arista("Servidor_A", "Servidor_C", 15)
    gp.agregar_arista("Servidor_B", "Servidor_C", 3)
    gp.agregar_arista("Servidor_C", "Servidor_D", 7)
    gp.agregar_arista("Servidor_B", "Servidor_D", 20)
    print("\n3. Latencias mínimas desde Router:")
    for nodo, latencia in gp.dijkstra("Router").items():
        print(f"{nodo}: {latencia} ms")

    # 4. Camino exacto después de ejecutar Dijkstra
    camino, latencia = gp.dijkstra_camino("Router", "Servidor_D")
    print("\n4. Camino mínimo hasta Servidor_D:")
    print("Camino:", camino)
    print("Latencia total:", latencia, "ms")

    # 5. Grado de entrada y salida en grafo dirigido
    gg = Grafo(dirigido=True)
    gg.agregar_arista("A", "B")
    gg.agregar_arista("A", "C")
    gg.agregar_arista("B", "C")
    gg.agregar_arista("C", "A")
    entrada, salida = gg.grados()
    print("\n5. Grados de entrada y salida:")
    for nodo in gg.adj:
        print(
            f"{nodo}: entrada={entrada[nodo]}, "
            f"salida={salida[nodo]}"
        )


# ============================================================
# INCISO 7: MINI-PROYECTO SISTEMA DE NAVEGACIÓN GPS
# ============================================================

class SistemaGPS:
    """Sistema GPS de consola basado en un grafo ponderado."""

    def __init__(self):
        # ciudad: [(ciudad_vecina, tiempo_en_minutos)]
        self.grafo = {}

    def agregar_ciudad(self, ciudad):
        """Agrega una ciudad si no existe."""
        ciudad = ciudad.strip()

        if not ciudad:
            raise ValueError("El nombre de la ciudad no puede estar vacío.")

        if ciudad not in self.grafo:
            self.grafo[ciudad] = []
            return True

        return False

    def agregar_ruta(self, origen, destino, tiempo):
        """Agrega una ruta bidireccional entre dos ciudades."""
        origen = origen.strip()
        destino = destino.strip()

        if not origen or not destino:
            raise ValueError("Los nombres de las ciudades son obligatorios.")

        if origen == destino:
            raise ValueError("La ruta debe conectar ciudades diferentes.")

        if isinstance(tiempo, bool) or not isinstance(tiempo, (int, float)):
            raise ValueError("El tiempo debe ser un número.")

        if tiempo <= 0:
            raise ValueError("El tiempo debe ser mayor que cero.")

        self.agregar_ciudad(origen)
        self.agregar_ciudad(destino)

        if any(vecino == destino for vecino, _ in self.grafo[origen]):
            raise ValueError("Esta ruta ya existe.")

        self.grafo[origen].append((destino, tiempo))
        self.grafo[destino].append((origen, tiempo))

    def mostrar_ciudades(self):
        """Muestra las ciudades y sus conexiones."""
        if not self.grafo:
            print("No hay ciudades registradas.")
            return

        print("\n--- CIUDADES Y RUTAS ---")
        for ciudad, vecinos in self.grafo.items():
            print(f"\n{ciudad}:")

            if not vecinos:
                print("  Sin rutas conectadas.")
            else:
                for vecino, tiempo in vecinos:
                    print(f"  -> {vecino}: {tiempo:g} minutos")

    def dijkstra(self, origen, destino):
        """Devuelve la ruta más rápida y el tiempo total."""
        if origen not in self.grafo:
            raise ValueError(f"La ciudad '{origen}' no existe.")

        if destino not in self.grafo:
            raise ValueError(f"La ciudad '{destino}' no existe.")

        distancias = {ciudad: float("inf") for ciudad in self.grafo}
        anteriores = {ciudad: None for ciudad in self.grafo}
        distancias[origen] = 0
        cola = [(0, origen)]

        while cola:
            tiempo_actual, actual = heapq.heappop(cola)

            if tiempo_actual > distancias[actual]:
                continue

            if actual == destino:
                break

            for vecino, tiempo in self.grafo[actual]:
                nuevo_tiempo = tiempo_actual + tiempo

                if nuevo_tiempo < distancias[vecino]:
                    distancias[vecino] = nuevo_tiempo
                    anteriores[vecino] = actual
                    heapq.heappush(cola, (nuevo_tiempo, vecino))

        if distancias[destino] == float("inf"):
            return None, float("inf")

        camino = []
        actual = destino

        while actual is not None:
            camino.append(actual)
            actual = anteriores[actual]

        camino.reverse()
        return camino, distancias[destino]

    def consultar_ruta(self, origen, destino):
        """Imprime el recorrido completo y el tiempo mínimo."""
        camino, tiempo = self.dijkstra(origen, destino)

        if camino is None:
            print(f"No existe una ruta entre {origen} y {destino}.")
            return

        print("\n--- RUTA MÁS RÁPIDA ---")
        print("Recorrido:", " -> ".join(camino))
        print(f"Tiempo total: {tiempo:g} minutos")


def crear_mapa_ejemplo():
    """Construye un mapa inicial de ejemplo."""
    gps = SistemaGPS()
    gps.agregar_ruta("Managua", "Masaya", 35)
    gps.agregar_ruta("Managua", "Granada", 50)
    gps.agregar_ruta("Masaya", "Granada", 20)
    gps.agregar_ruta("Masaya", "Carazo", 30)
    gps.agregar_ruta("Granada", "Rivas", 80)
    gps.agregar_ruta("Carazo", "Rivas", 60)
    return gps


def menu_gps():
    """Menú interactivo del mini-proyecto."""
    gps = crear_mapa_ejemplo()

    while True:
        print("\n====== SISTEMA DE NAVEGACIÓN GPS ======")
        print("1. Mostrar ciudades y rutas")
        print("2. Agregar una ciudad")
        print("3. Agregar una ruta")
        print("4. Consultar la ruta más rápida")
        print("5. Ejecutar ejemplos del inciso 6")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                gps.mostrar_ciudades()

            elif opcion == "2":
                ciudad = input("Nombre de la ciudad: ")
                if gps.agregar_ciudad(ciudad):
                    print("Ciudad agregada correctamente.")
                else:
                    print("La ciudad ya estaba registrada.")

            elif opcion == "3":
                origen = input("Ciudad de origen: ")
                destino = input("Ciudad de destino: ")
                tiempo_texto = input("Tiempo de viaje en minutos: ").strip()
                tiempo = float(tiempo_texto)

                gps.agregar_ruta(origen, destino, tiempo)
                print("Ruta agregada correctamente.")

            elif opcion == "4":
                origen = input("Ciudad de origen: ").strip()
                destino = input("Ciudad de destino: ").strip()
                gps.consultar_ruta(origen, destino)

            elif opcion == "5":
                demostrar_inciso_6()

            elif opcion == "6":
                print("Gracias por utilizar el sistema GPS.")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        except ValueError as error:
            print("Error:", error)

        except (EOFError, KeyboardInterrupt):
            print("\nPrograma finalizado.")
            break


if __name__ == "__main__":
    menu_gps()
