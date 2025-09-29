def mostrar_menu():
    print("\n--- MENÚ LISTA DE COMPRAS ---")
    print("1. Ver lista")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Salir")

def ver_lista(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        print("Lista de compras:")
        for i, producto in enumerate(lista, start=1):
            print(f"{i}. {producto}")

def agregar_producto(lista):
    producto = input("Ingresa el producto a agregar: ")
    lista.append(producto)
    print(f"{producto} agregado a la lista.")

def eliminar_producto(lista):
    ver_lista(lista)
    if len(lista) > 0:
        try:
            indice = int(input("Ingresa el número del producto a eliminar: ")) - 1
            eliminado = lista.pop(indice)
            print(f"❌ {eliminado} eliminado de la lista.")
        except (ValueError, IndexError):
            print("⚠️ Opción no válida.")

# def main():
#     lista_compras = []
#     while True:
#         mostrar_menu()
#         opcion = input("Elige una opción: ")

#         if opcion == "1":
#             ver_lista(lista_compras)
#         elif opcion == "2":
#             agregar_producto(lista_compras)
#         elif opcion == "3":
#             eliminar_producto(lista_compras)
#         elif opcion == "4":
#             print("👋 Saliendo del programa. ¡Adiós!")
#             break
#         else:
#             print("⚠️ Opción no válida. Intenta de nuevo.")

def main():
    lista_compras = []
    # while True:
    #     mostrar_menu()
    #     opcion = input("Elige una opción: ")
    activo = True  # flag de control

    while activo:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                ver_lista(lista_compras)
            case "2":
                agregar_producto(lista_compras)
            case "3":
                eliminar_producto(lista_compras)
            case "4":
                print("¡Adiós!")
                break
            case _:
                print(" Opción no válida. Intenta de nuevo.")


# Ejecutar programa
main()
