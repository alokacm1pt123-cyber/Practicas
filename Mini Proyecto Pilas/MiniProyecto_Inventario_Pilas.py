from collections import deque
from typing import Any, Dict, List


class PilaDeque:
    """TDA Pila con collections.deque (O(1) en push y pop)."""
    def __init__(self) -> None:
        self._items: deque = deque()

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("La pila está vacía.")
        return self._items.pop()

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("La pila está vacía.")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def get_all(self) -> List[Any]:
        return list(self._items)


class Inventario:
    """Sistema de inventario con ventas, pérdidas y retiro parcial."""
    def __init__(self) -> None:
        self._pila = PilaDeque()
        self._ventas: List[Dict[str, Any]] = []
        self._perdidas: List[Dict[str, Any]] = []

    def agregar_producto(self, nombre: str, cantidad: int, precio: float) -> None:
        if cantidad <= 0 or precio < 0:
            print("⚠️ Cantidad y precio deben ser positivos.")
            return
        producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
        self._pila.push(producto)
        print(f"✅ Producto '{nombre}' agregado al inventario.")

    def vender_producto(self) -> None:
        try:
            producto = self._pila.pop()
            self._ventas.append(producto)
            print(f"💰 Venta registrada: {producto['nombre']} (Cantidad: {producto['cantidad']})")
        except IndexError as e:
            print(f"⚠️ {e}")

    def registrar_perdida(self) -> None:
        try:
            producto = self._pila.pop()
            self._perdidas.append(producto)
            print(f"❌ Pérdida registrada: {producto['nombre']} (Cantidad: {producto['cantidad']})")
        except IndexError as e:
            print(f"⚠️ {e}")

    def retirar_parcial(self, cantidad: int) -> None:
        """Retira solo una parte del producto en la cima de la pila."""
        if cantidad <= 0:
            print("⚠️ La cantidad a retirar debe ser positiva.")
            return
        try:
            producto = self._pila.peek()  # Ver el producto sin sacarlo
            if cantidad >= producto["cantidad"]:
                # Retiro total
                self._pila.pop()
                print(f"🛒 Producto '{producto['nombre']}' retirado completamente.")
            else:
                # Retiro parcial
                producto["cantidad"] -= cantidad
                print(f"🛒 Retiradas {cantidad} unidades de '{producto['nombre']}'. Quedan {producto['cantidad']}.")
        except IndexError as e:
            print(f"⚠️ {e}")

    def mostrar_inventario(self) -> None:
        if self._pila.is_empty():
            print("⚠️ Inventario vacío.")
            return
        print("\n📦 Inventario actual (último agregado arriba):")
        print("{:<20} {:<10} {:<10}".format("Nombre", "Cantidad", "Precio"))
        print("-" * 45)
        for producto in reversed(self._pila.get_all()):
            print("{:<20} {:<10} {:<10.2f}".format(
                producto["nombre"], producto["cantidad"], producto["precio"]
            ))

    def mostrar_ventas(self) -> None:
        if not self._ventas:
            print("⚠️ No hay ventas registradas.")
            return
        print("\n💰 Registro de Ventas:")
        print("{:<20} {:<10} {:<10}".format("Nombre", "Cantidad", "Precio"))
        print("-" * 45)
        for producto in self._ventas:
            print("{:<20} {:<10} {:<10.2f}".format(
                producto["nombre"], producto["cantidad"], producto["precio"]
            ))

    def mostrar_perdidas(self) -> None:
        if not self._perdidas:
            print("⚠️ No hay pérdidas registradas.")
            return
        print("\n❌ Registro de Pérdidas:")
        print("{:<20} {:<10} {:<10}".format("Nombre", "Cantidad", "Precio"))
        print("-" * 45)
        for producto in self._perdidas:
            print("{:<20} {:<10} {:<10.2f}".format(
                producto["nombre"], producto["cantidad"], producto["precio"]
            ))


# =========================
# Menú interactivo
# =========================
if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\n=== 📦 SISTEMA DE INVENTARIO CON PILA (deque) ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Vender producto (LIFO)")
        print("4. Registrar pérdida (LIFO)")
        print("5. Retirar parcialmente producto en cima")
        print("6. Mostrar ventas")
        print("7. Mostrar pérdidas")
        print("8. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(nombre, cantidad, precio)
            except ValueError:
                print("⚠️ Entrada inválida.")

        elif opcion == "2":
            inventario.mostrar_inventario()

        elif opcion == "3":
            inventario.vender_producto()

        elif opcion == "4":
            inventario.registrar_perdida()

        elif opcion == "5":
            try:
                cantidad = int(input("Cantidad a retirar: "))
                inventario.retirar_parcial(cantidad)
            except ValueError:
                print("⚠️ Entrada inválida.")

        elif opcion == "6":
            inventario.mostrar_ventas()

        elif opcion == "7":
            inventario.mostrar_perdidas()

        elif opcion == "8":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción no válida.")