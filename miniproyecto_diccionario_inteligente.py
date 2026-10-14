"""
Mini-proyecto: Diccionario Inteligente con un Árbol Binario de Búsqueda.
Guarda palabras y definiciones; permite búsqueda exacta, autocompletado
por prefijo y mostrar el diccionario completo en orden alfabético.
"""


class Palabra:
    def __init__(self, texto, definicion):
        self.texto = texto.strip().lower()
        self.definicion = definicion.strip()

    def __str__(self):
        return f"{self.texto}: {self.definicion}"


class NodoPalabra:
    def __init__(self, palabra):
        self.palabra = palabra
        self.izquierdo = None
        self.derecho = None


class DiccionarioBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, palabra):
        if self.raiz is None:
            self.raiz = NodoPalabra(palabra)
        else:
            self._insertar_recursivo(self.raiz, palabra)

    def _insertar_recursivo(self, nodo, palabra):
        if palabra.texto < nodo.palabra.texto:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoPalabra(palabra)
            else:
                self._insertar_recursivo(nodo.izquierdo, palabra)
        elif palabra.texto > nodo.palabra.texto:
            if nodo.derecho is None:
                nodo.derecho = NodoPalabra(palabra)
            else:
                self._insertar_recursivo(nodo.derecho, palabra)
        else:
            # Si la palabra ya existe, actualizamos su definición.
            nodo.palabra.definicion = palabra.definicion

    def buscar(self, texto):
        texto = texto.strip().lower()
        actual = self.raiz

        while actual is not None:
            if texto == actual.palabra.texto:
                return actual.palabra
            if texto < actual.palabra.texto:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        return None

    def buscar_por_prefijo(self, prefijo):
        prefijo = prefijo.strip().lower()
        resultados = []

        def recorrer(nodo):
            if nodo is None:
                return
            # Inorden: los resultados salen en orden alfabético.
            recorrer(nodo.izquierdo)
            if nodo.palabra.texto.startswith(prefijo):
                resultados.append(nodo.palabra)
            recorrer(nodo.derecho)

        recorrer(self.raiz)
        return resultados

    def todas_las_palabras(self):
        resultado = []

        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.izquierdo)
                resultado.append(nodo.palabra)
                recorrer(nodo.derecho)

        recorrer(self.raiz)
        return resultado

    def cargar_desde_archivo(self, ruta):
        """Formato del archivo: palabra|definición, una por línea."""
        cantidad = 0
        with open(ruta, "r", encoding="utf-8") as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue
                partes = linea.split("|", 1)
                if len(partes) != 2 or not partes[0].strip() or not partes[1].strip():
                    print(f"Aviso: línea {numero_linea} ignorada por formato incorrecto.")
                    continue
                self.insertar(Palabra(partes[0], partes[1]))
                cantidad += 1
        return cantidad


# Más de 50 palabras iniciales con definiciones breves.
PALABRAS_INICIALES = [
    ("abeja", "Insecto que produce miel y ayuda a polinizar flores."),
    ("abeto", "Árbol de hojas perennes y forma cónica."),
    ("abogado", "Profesional que asesora o representa en asuntos legales."),
    ("abundancia", "Gran cantidad de algo."),
    ("acceso", "Entrada o posibilidad de llegar a un lugar o recurso."),
    ("acorde", "Conjunto de notas musicales que suenan simultáneamente."),
    ("agua", "Líquido esencial para los seres vivos."),
    ("águila", "Ave rapaz de gran tamaño."),
    ("aire", "Mezcla de gases que forma la atmósfera terrestre."),
    ("alarma", "Señal que advierte de un peligro o situación."),
    ("álbum", "Colección de canciones, fotografías u otros elementos."),
    ("alegría", "Sentimiento de satisfacción y felicidad."),
    ("algoritmo", "Conjunto ordenado de pasos para resolver un problema."),
    ("almohada", "Objeto blando que sirve de apoyo para la cabeza."),
    ("altura", "Distancia vertical entre un punto y una referencia."),
    ("amable", "Que trata a los demás con atención y cortesía."),
    ("amistad", "Relación de afecto y confianza entre personas."),
    ("amor", "Afecto profundo hacia alguien o algo."),
    ("análisis", "Examen detallado de algo para comprenderlo."),
    ("ancho", "Dimensión de un objeto de un lado al otro."),
    ("anciano", "Persona de edad avanzada."),
    ("animal", "Ser vivo que se alimenta y puede percibir su entorno."),
    ("anillo", "Aro que suele usarse como adorno en un dedo."),
    ("antena", "Dispositivo que transmite o recibe señales."),
    ("árbol", "Planta de tronco leñoso que se ramifica a cierta altura."),
    ("archivo", "Conjunto organizado de documentos o datos."),
    ("arco", "Estructura curva o parte de una circunferencia."),
    ("arena", "Conjunto de granos pequeños de roca o mineral."),
    ("argumento", "Razón que apoya una idea o resumen de una historia."),
    ("arte", "Actividad creativa que expresa ideas o emociones."),
    ("asombro", "Sorpresa intensa ante algo inesperado."),
    ("astro", "Cuerpo celeste como una estrella o planeta."),
    ("atención", "Acción de concentrarse en algo."),
    ("audio", "Sonido o señal relacionada con el sonido."),
    ("aula", "Sala destinada a la enseñanza."),
    ("aurora", "Luz que aparece en el cielo antes de salir el sol."),
    ("auto", "Vehículo automóvil para transportar personas."),
    ("autonomía", "Capacidad de actuar o decidir por cuenta propia."),
    ("aventura", "Experiencia que implica novedad o riesgo."),
    ("avión", "Vehículo capaz de volar con alas y motores."),
    ("bailar", "Mover el cuerpo siguiendo un ritmo."),
    ("balance", "Estado de equilibrio o resumen de cuentas."),
    ("banco", "Entidad financiera o asiento alargado."),
    ("barco", "Vehículo que navega por el agua."),
    ("barrio", "Zona o conjunto de calles de una localidad."),
    ("batería", "Instrumento musical de percusión o dispositivo que almacena energía."),
    ("biblioteca", "Lugar o colección donde se conservan libros."),
    ("bienestar", "Estado de satisfacción y condiciones favorables."),
    ("bosque", "Terreno extenso poblado de árboles."),
    ("botella", "Recipiente usado para contener líquidos."),
    ("brisa", "Viento suave."),
    ("búsqueda", "Acción de intentar encontrar algo."),
    ("cable", "Conjunto de conductores protegidos por una cubierta."),
    ("camino", "Vía por la que se puede transitar."),
    ("canción", "Composición musical que suele incluir voz."),
    ("casa", "Construcción destinada a servir de vivienda."),
    ("cielo", "Espacio visible sobre la superficie terrestre."),
    ("ciencia", "Conocimiento obtenido mediante observación y estudio."),
    ("ciudad", "Área poblada con calles, edificios y servicios."),
    ("claridad", "Cualidad de lo que se entiende o se ve fácilmente."),
    ("computadora", "Máquina electrónica que procesa información."),
    ("concierto", "Presentación musical ante un público."),
    ("confianza", "Seguridad que se deposita en alguien o algo."),
    ("conocimiento", "Información y comprensión adquiridas mediante aprendizaje."),
    ("corazón", "Órgano que bombea sangre por el cuerpo."),
    ("creatividad", "Capacidad de producir ideas originales."),
    ("cultura", "Conjunto de conocimientos, costumbres y expresiones de una sociedad."),
    ("danza", "Arte de expresar mediante movimientos rítmicos."),
    ("dato", "Representación de un hecho o información."),
    ("definición", "Explicación del significado de una palabra o concepto."),
    ("desarrollo", "Proceso de crecimiento o evolución."),
    ("diccionario", "Obra que reúne palabras y explica sus significados."),
    ("diseño", "Plan o representación de cómo será algo."),
    ("educación", "Proceso de enseñanza y aprendizaje."),
    ("energía", "Capacidad de producir cambios o realizar trabajo."),
    ("equipo", "Conjunto de personas o elementos que colaboran."),
    ("escuela", "Institución dedicada a la enseñanza."),
    ("esperanza", "Confianza en que ocurra algo deseado."),
    ("estrella", "Cuerpo celeste que emite luz propia."),
    ("familia", "Grupo de personas unidas por parentesco o vínculos afectivos."),
    ("felicidad", "Estado de satisfacción y bienestar."),
    ("flor", "Estructura reproductiva de muchas plantas."),
    ("fortaleza", "Capacidad de resistir o cualidad de ser fuerte."),
    ("fruta", "Producto comestible de ciertas plantas, generalmente con semillas."),
    ("futuro", "Tiempo que todavía no ha ocurrido."),
    ("guitarra", "Instrumento musical de cuerdas."),
    ("historia", "Relato de hechos pasados o disciplina que los estudia."),
    ("idea", "Representación mental de algo."),
    ("idioma", "Sistema de comunicación propio de una comunidad."),
    ("información", "Datos organizados que aportan conocimiento."),
    ("instrumento", "Objeto utilizado para realizar una tarea o producir música."),
    ("jardín", "Terreno donde se cultivan plantas y flores."),
    ("lectura", "Acción de interpretar un texto escrito."),
    ("libertad", "Capacidad de actuar y decidir dentro de ciertos límites."),
    ("libro", "Conjunto de páginas con texto o imágenes."),
    ("luz", "Radiación visible que permite ver los objetos."),
    ("memoria", "Capacidad de conservar y recuperar información."),
    ("música", "Arte de organizar sonidos y silencios."),
    ("naturaleza", "Conjunto de seres y fenómenos del mundo físico."),
    ("palabra", "Unidad lingüística con significado."),
    ("paz", "Situación de tranquilidad y ausencia de conflicto."),
    ("programación", "Proceso de crear instrucciones para una computadora."),
    ("raíz", "Parte de una planta que suele fijarla y absorber agua."),
    ("sonido", "Vibración que puede percibirse mediante el oído."),
    ("tecnología", "Aplicación de conocimientos para crear herramientas y soluciones."),
    ("tiempo", "Magnitud que permite ordenar la duración de los acontecimientos."),
    ("universo", "Conjunto de todo el espacio, materia y energía."),
]


def crear_diccionario():
    diccionario = DiccionarioBST()
    for texto, definicion in PALABRAS_INICIALES:
        diccionario.insertar(Palabra(texto, definicion))
    return diccionario


def menu():
    diccionario = crear_diccionario()
    print("=" * 52)
    print("          DICCIONARIO INTELIGENTE")
    print(f" Palabras cargadas: {len(diccionario.todas_las_palabras())}")
    print("=" * 52)

    while True:
        print("\nMENÚ")
        print("1. Buscar una palabra")
        print("2. Autocompletar por prefijo")
        print("3. Ver diccionario completo")
        print("4. Cargar palabras desde un archivo")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            texto = input("Escribe la palabra: ")
            palabra = diccionario.buscar(texto)
            if palabra:
                print(f"\n{palabra.texto.upper()}\nDefinición: {palabra.definicion}")
            else:
                print("La palabra no está en el diccionario.")

        elif opcion == "2":
            prefijo = input("Escribe el prefijo: ")
            resultados = diccionario.buscar_por_prefijo(prefijo)
            if resultados:
                print(f"\nCoincidencias ({len(resultados)}):")
                for palabra in resultados:
                    print(f" - {palabra.texto}: {palabra.definicion}")
            else:
                print("No se encontraron palabras con ese prefijo.")

        elif opcion == "3":
            palabras = diccionario.todas_las_palabras()
            print(f"\nDICCIONARIO COMPLETO ({len(palabras)} palabras)")
            for palabra in palabras:
                print(f" - {palabra.texto}: {palabra.definicion}")

        elif opcion == "4":
            ruta = input("Ruta del archivo .txt (formato palabra|definición): ").strip()
            try:
                cantidad = diccionario.cargar_desde_archivo(ruta)
                print(f"Se procesaron {cantidad} líneas válidas.")
            except OSError as error:
                print(f"No se pudo abrir el archivo: {error}")

        elif opcion == "5":
            print("¡Gracias por utilizar el Diccionario Inteligente!")
            break

        else:
            print("Opción no válida. Elige un número del 1 al 5.")


if __name__ == "__main__":
    menu()
