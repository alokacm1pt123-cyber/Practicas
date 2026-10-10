# Inciso 6 - Tarea de Recursividad

def multiplicacion_rusa(a: int, b: int) -> int:
    """Multiplica dos enteros mediante sumas y recursividad."""
    signo = -1 if (a < 0) != (b < 0) else 1
    a, b = abs(a), abs(b)

    
    if b == 0:
        return 0

    
    if b % 2 == 0:
        resultado = multiplicacion_rusa(a + a, b // 2)
    else:
        resultado = a + multiplicacion_rusa(a + a, b // 2)

    return signo * resultado


def contar_vocales(cadena: str) -> int:
    """Cuenta vocales, incluyendo vocales acentuadas."""
    if cadena == "": 
        return 0

    vocales = "aeiou"
    cantidad = 1 if cadena[0].lower() in vocales else 0
    return cantidad + contar_vocales(cadena[1:]) 


def imprimir_patron(n: int, nivel: int = 1) -> None:
    """Imprime un patrón creciente de asteriscos."""
    if nivel > n:  
        return

    print("*" * nivel)
    imprimir_patron(n, nivel + 1)  


def contar_caminos(n: int, m: int, i: int = 0, j: int = 0) -> int:
    """Cuenta caminos en tablero NxM, moviéndose abajo o a la derecha."""
    if n <= 0 or m <= 0:
        return 0

    if i == n - 1 and j == m - 1:  
        return 1

    if i >= n or j >= m:  
        return 0

    
    return contar_caminos(n, m, i + 1, j) + contar_caminos(n, m, i, j + 1)


def aplanar_lista(lista: list) -> list:
    """Convierte una lista anidada en una lista plana."""
    resultado = []

    for elemento in lista:
        if isinstance(elemento, list):  # Caso recursivo
            resultado.extend(aplanar_lista(elemento))
        else:
            resultado.append(elemento)

    return resultado


if __name__ == "__main__":
    print("=== INCISO 6: TAREA DE RECURSIVIDAD ===")

    print("\n1. Multiplicación rusa:")
    print("5 x 4 =", multiplicacion_rusa(5, 4))
    print("7 x 3 =", multiplicacion_rusa(7, 3))
    print("-5 x 4 =", multiplicacion_rusa(-5, 4))

    print("\n2. Conteo de vocales:")
    print("'Hola Mundo' tiene", contar_vocales("Hola Mundo"), "vocales.")
    print("'Recursividad' tiene", contar_vocales("Recursividad"), "vocales.")

    print("\n3. Patrón de asteriscos para n = 3:")
    imprimir_patron(3)

    print("\n4. Caminos en un tablero:")
    print("Tablero 3x3:", contar_caminos(3, 3), "caminos")
    print("Tablero 2x3:", contar_caminos(2, 3), "caminos")

    print("\n5. Flatten List:")
    datos = [1, [2, [3, 4], 5], [6, [7, 8]]]
    print("Lista original:", datos)
    print("Lista plana:", aplanar_lista(datos))
