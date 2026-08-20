#=======================================
#  CONSTANTES GLOBALES
#========================================
NOTA_MINIMA_APROBACION = 3.0
NOTA_MAXIMA = 5.0
NOTA_MINIMA_APROBACION = 2.0
CANTIDAD_NOTAS = 6


#===========================================================
#   FUNCIONES AUXILIARES (sin retorno, sin parametros)
#===========================================================

def funcion_mostrar_linea():
    """"Imprime una linea de separacion, funcion sin parametros y sin retorno"""
    print ("= " * 60)

def funcion_mostrar_encabezado(titulo):
    """"Imprime un encabezado con el titulo proporcionado, funcion con parametros y sin retorno"""
    funcion_mostrar_linea()
    print (f" {titulo}")
    funcion_mostrar_linea()

def funcion_pausar():
    """Pausa la ejecucion del programa hasta que el usuario presione un tecla , funcion sin parametros """
    input ("Presione una tecla para continuar...")


#===========================================================
#    FUNCIONES CON RETORNO (operaciones y validaciones)
#===========================================================

def funcion_leer_texto(mensaje):
    """Leer un texto desde la entrada estandar, funcion con parametros y con retorno"""
    while True:
        texto = input(f"{mensaje}").strip()
        if texto:
            return texto
        print ("Advertencia: El texto no puede estar vacio. Intente nuevamente.")

def funcion_leer_numero(mensaje, minimo, maximo):
    """Leer un numero flotante y valida un rango"""
    while True:
        try:
            valor = float(input(f"  {mensaje}"))
            if minimo <= valor <= maximo:
                return valor
                print (f"Advertencia : El numero debe estar entre {minimo} y {maximo}. Intente nuevamente.")
        except ValueError:
            print ("Error: Entrada invalida, Por favor ingrese un numero valido.")

def funcion_calcular_promedio(notas):
    if (len(notas) == 0):
        return 0.0
    return sum(notas) / len(notas)

def funcion_determinar_estado(promedio):
    """Determina el estado del estudiante segun su promedio"""
    if promedio >= NOTA_MINIMA_APROBACION:
        return "Aprobado"
    else:
        return "Reprobado"    

def funcion_determinar_mencion(promedio):
    """Determina la mencion del estudiante segun su promedio"""
    if promedio >=4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy Bueno"  
    elif promedio >=3.5:
        return "Bueno"
    elif promedio >= NOTA_MINIMA_APROBACION:
        return "Regular"
    else:
        return "En Recuperacion"


#=====================================================================
#    CLASE ESTUDIANTE (POO - encapsulamiento, herencia, polimorfismo)  
#======================================================================   

class Estudiante:
    """
    Clase que representa a un estudiante con sus atributos y métodos.
    Encapsulamiento: Los atributos son privados y se accede a ellos mediante métodos.
    """
    #Variable de clae
    _cantidad_estudiantes = 0

    def __init__(self, NombreCompleto, edad, grado):
        """
        Inicializa un objeto Estudiante con nombre, apellido y lista de notas.
        Constructor de la clase
        Hace referencia al objeto actual
        """   

        Estudiante._cantidad_estudiantes +=1
        self._id = Estudiante._cantidad_estudiantes
        self._nombreCompleto = NombreCompleto
        self._edad = edad
        self._grado = grado
        self._notas = [] #Declaracion de lista vacia que recibe las notas
        self._promedio = 0.0
        self._estado = ""
        self._mencion = ""
        self._rendimiento = ""


#========================================
#    GETTERS (Encapsulamiento) 
#========================================

@property       
def id(self):
    """Devuelve el ID del estudiante"""
    return self._id

@property
def nombreCompleto(self):
    """Devuelve la nombreCompleto del estudiante"""
    return self._nombreCompleto

@property
def edad(self):
    """Devuelve la edad del estudiante"""
    return self._edad

@property
def grado(self):
    """Devuelve el grado del estudiante"""
    return self._grado

@property
def notas(self):
    """Devuelve las notas del estudiante"""
    return self._notas.copy()

@property
def promedio(self):
    """Devuelve el promedio del estudiante"""
    return self._promedio

@property
def estado(self):
    """Devuelve el estado del estudiante"""
    return self._estado

@property
def mencion(self):
    """Devuelve el mencion del estudiante"""
    return self._mencion

@property
def rendimiento(self):
    """Devuelve el rendimiento del estudiante"""
    return self._rendimiento

#========================================
#SETTERS (modificadores)
#========================================

@edad.setter
def edad(self, valor):
    """Establece la edad del estudiante"""
    if 0 < valor > 65:
        self.edad_ = valor
    else:
        raise ValueError("La edad debe ser un numero positivo")