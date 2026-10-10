# Inciso 7 - Mini-proyecto: Explorador de Directorios
class ExploradorRecursivo:
    """Explora un sistema de archivos representado con diccionarios."""

    @staticmethod
    def imprimir_arbol(sistema: dict, nivel: int = 0) -> None:
        if not sistema:
            return

        for nombre, contenido in sistema.items():
            indentacion = "    " * nivel

            if isinstance(contenido, dict):
                print(f"{indentacion}[CARPETA] {nombre}/")
                ExploradorRecursivo.imprimir_arbol(contenido, nivel + 1)
            else:
                print(f"{indentacion}[ARCHIVO] {nombre} ({contenido})")

    @staticmethod
    def buscar_archivo(
        sistema: dict, nombre: str, ruta: str = ""
    ) -> str | None:
        if not sistema:
            return None

        for nombre_elemento, contenido in sistema.items():
            ruta_actual = f"{ruta}/{nombre_elemento}"

            if isinstance(contenido, dict):
                resultado = ExploradorRecursivo.buscar_archivo(
                    contenido, nombre, ruta_actual
                )
                if resultado is not None:
                    return resultado
            elif nombre_elemento == nombre:
                return ruta_actual

        return None

    @staticmethod
    def contar_archivos(sistema: dict) -> int:
        if not sistema:
            return 0

        total = 0
        for contenido in sistema.values():
            if isinstance(contenido, dict):
                total += ExploradorRecursivo.contar_archivos(contenido)
            else:
                total += 1

        return total

sistema_archivos = {
    "Documentos": {
        "apuntes.txt": "10kb",
        "fotos": {
            "vacaciones.png": "2mb",
            "perro.jpg": "1mb"
        }
    },
    "sistema.dll": "500kb"
}


if __name__ == "__main__":
    print("=== INCISO 7: EXPLORADOR DE DIRECTORIOS ===")

    print("\nÁrbol de directorios:")
    ExploradorRecursivo.imprimir_arbol(sistema_archivos)

    print("\nBúsqueda de archivo:")
    nombre_buscado = "perro.jpg"
    ruta = ExploradorRecursivo.buscar_archivo(
        sistema_archivos, nombre_buscado
    )

    if ruta is not None:
        print(f"Archivo encontrado: {ruta}")
    else:
        print(f"El archivo '{nombre_buscado}' no fue encontrado.")

    print("\nConteo de archivos:")
    print("Total de archivos:", ExploradorRecursivo.contar_archivos(sistema_archivos))
