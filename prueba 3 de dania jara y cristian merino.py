import os
import pyfiglet

os.system("cls")

print(pyfiglet.figlet_format("CELULARES"))

fecha = ""
folio = 10000

productos = [  #   id    producto          tamaño    stock  precio
    ["p001", "iPhone 13", "128GB", 50, 900000],
    ["p002", "Samsung S21", "256GB", 30, 850000],
    ["p003", "Xiaomi Mi 11", "128GB", 40, 700000],
    ["p004", "Huawei P40", "256GB", 20, 750000],
    ["p005", "Google Pixel 5", "128GB", 25, 800000],
    ["p006", "OnePlus 9", "256GB", 35, 820000],
    ["p007", "Sony Xperia 1", "128GB", 15, 900000],
    ["p008", "LG Velvet", "128GB", 25, 600000],
    ["p009", "Motorola Edge", "256GB", 20, 650000],
    ["p010", "Nokia 8.3", "128GB", 30, 550000]
]

ventas = [  # folio     fecha      id     cantidad  total
    ["10001", "10-05-2024", "p001", 5, 4500000],
    ["10002", "30-05-2024", "p004", 3, 2250000],
    ["10003", "25-06-2024", "p006", 4, 3280000],
    ["10004", "27-06-2024", "p003", 2, 1400000],
    ["10005", "28-06-2024", "p005", 3, 2400000],
    ["10006", "28-06-2024", "p006", 5, 4100000],
    ["10007", "28-06-2024", "p007", 2, 1800000],
    ["10008", "29-06-2024", "p008", 4, 2400000],
    ["10009", "29-06-2024", "p009", 3, 1950000],
    ["10010", "30-06-2024", "p010", 5, 2750000],
    ["10011", "30-07-2024", "p002", 4, 3400000],
    ["10012", "31-07-2024", "p001", 5, 4500000],
    ["10013", "01-07-2024", "p003", 3, 2100000],
    ["10014", "02-07-2024", "p004", 4, 3000000],
    ["10015", "03-07-2024", "p007", 3, 2700000],
    ["10016", "04-07-2024", "p008", 5, 3000000],
    ["10017", "05-07-2024", "p010", 5, 2750000],
    ["10018", "06-07-2024", "p006", 4, 3280000],
    ["10019", "07-07-2024", "p009", 5, 3250000],
    ["10020", "08-07-2024", "p005", 4, 3200000],
]

id = ""
opcion = 0

def get_folio():
    elemento = len(ventas)
    return int(ventas[elemento - 1][0]) + 1

def buscar_id(id):
    for p in productos:
        if p[0] == id:
            return p
    return -1

def ventas_por_fecha(fecha):
    ventas_fecha = [venta for venta in ventas if venta[1] == fecha]
    return ventas_fecha

def ventas_por_rango(fecha_inicio, fecha_fin):
    ventas_rango = [venta for venta in ventas if fecha_inicio <= venta[1] <= fecha_fin]
    return ventas_rango

def cargar_datos():
    global productos, ventas
    if not productos or not ventas:
        try:
            with open("productos.txt", "r") as f:
                productos = [line.strip().split(",") for line in f.readlines()]
                for producto in productos:
                    producto[3] = int(producto[3])
                    producto[4] = int(producto[4])
        except FileNotFoundError:
            print("Archivo productos.txt no encontrado.")
        try:
            with open("ventas_prod.txt", "r") as f:
                ventas = [line.strip().split(",") for line in f.readlines()]
                for venta in ventas:
                    venta[3] = int(venta[3])
                    venta[4] = int(venta[4])
        except FileNotFoundError:
            print("Archivo ventas_prod.txt no encontrado.")

def grabar_datos():
    with open("productos.txt", "w") as f:
        for producto in productos:
            f.write(",".join(map(str, producto)) + "\n")
    with open("ventas_prod.txt", "w") as f:
        for venta in ventas:
            f.write(",".join(map(str, venta)) + "\n")

while opcion != 5:
    print("Ultimo folio: ", get_folio() - 1)
    print("""
        --------------------------------
                Sistema de ventas
       1. Vender productos
       2. Reportes
       3. Mantenedores
       4. Administración de datos
       5. Salir
          
    """)
    opcion = int(input("Ingrese una opción entre 1-5: "))
    match opcion:
        case 1:
            while True:
                os.system("cls")
                print("          VENDER PRODUCTO                  \n")
                producto_id = input("Ingrese ID: ")
                producto = buscar_id(producto_id)
                if producto != -1:
                    print(producto[0], " ", producto[1], " ", producto[2], " ", producto[3], " ", producto[4])
                    cantidad = int(input("Ingrese cantidad a comprar: "))
                    stock = producto[3]
                    if cantidad <= stock:
                        valor = cantidad * producto[4]
                        producto[3] -= cantidad
                        ventas.append([str(get_folio()), fecha, producto_id, cantidad, valor])
                        print(f"El valor de esta compra por {cantidad} productos es de: {valor}")
                        respuesta = input("¿Desea otra compra? [s]/[n]: ")
                        if respuesta.lower() == "n":
                            break
                    else:
                        print("Error, el stock no es suficiente")
                else:
                    print("Producto no encontrado")
                respuesta = input("¿Desea realizar otra compra? [s]/[n]: ")
                if respuesta.lower() == "n":
                    break
        case 2:
            os.system("cls")
            op = 0
            while op != 4:
                print("""
                    REPORTES
                    -------------------------------------
                    1. General de ventas (con total)
                    2. Ventas por fecha específica (con total)
                    3. Ventas por rango de fecha (con total)
                    4. Salir al menú principal
                """)
                op = int(input("Ingrese una opción entre 1-4: "))
                match op:
                    case 1:
                        os.system("cls")
                        print("\n  Reporte General de Ventas       \n")
                        total_ventas = 0
                        for venta in ventas:
                            print(venta)
                            total_ventas += venta[4]
                        print(f"Total de todas las ventas: {total_ventas}")
                        input("Presione Enter para continuar...")
                    case 2:
                        os.system("cls")
                        print("\n  Reporte de Ventas por Fecha Específica       \n")
                        fecha = input("Ingrese la fecha (dd-mm-aaaa): ")
                        ventas_fecha = ventas_por_fecha(fecha)
                        total_ventas = 0
                        for venta in ventas_fecha:
                            print(venta)
                            total_ventas += venta[4]
                        print(f"Total de ventas para la fecha {fecha}: {total_ventas}")
                        input("Presione Enter para continuar...")
                    case 3:
                        os.system("cls")
                        print("\n  Reporte de Ventas por Rango de Fechas       \n")
                        fecha_inicio = input("Ingrese la fecha de inicio (dd-mm-aaaa): ")
                        fecha_fin = input("Ingrese la fecha de fin (dd-mm-aaaa): ")
                        ventas_rango = ventas_por_rango(fecha_inicio, fecha_fin)
                        total_ventas = 0
                        for venta in ventas_rango:
                            print(venta)
                            total_ventas += venta[4]
                        print(f"Total de ventas desde {fecha_inicio} hasta {fecha_fin}: {total_ventas}")
                        input("Presione Enter para continuar...")
                    case 4:
                        break  # salir del menú de reportes y volver al menú principal
        case 3:
            op = 0
            while op != 6:
                print("""
                    MANTENEDOR DE PRODUCTOS
                    1. Agregar
                    2. Buscar
                    3. Eliminar
                    4. Modificar
                    5. Listar
                    6. Salir al menú principal
                """)
                op = int(input("Ingrese una opción entre 1-6: "))
                match op:
                    case 1:
                        print("\nAgregar\n")
                        id = input("Ingrese su id: ")
                        producto = input("Ingrese su nombre de producto: ")
                        tamaño = input("Ingrese tamaño del producto: ")
                        stock = int(input("Ingrese stock del producto: "))
                        precio = int(input("Ingrese precio del producto: "))
                        productos.append([id, producto, tamaño, stock, precio])
                        print(productos)
                    case 2:
                        print("\n-------------------------------------------\n")
                        id = input("Ingrese el id a buscar: ")
                        p = buscar_id(id)
                        if p != -1:
                            print(p[0], " ", p[1], " ", p[2], " ", p[3], " ", p[4])
                        else:
                            print("Error, id no existe")
                    case 3:
                        id = input("Ingrese el id a eliminar: ")
                        p = buscar_id(id)
                        if p != -1:
                            productos.remove(p)
                            print("Producto eliminado exitosamente.")
                        else:
                            print("Error, id no existe")
                    case 4:
                        id = input("Ingrese el id del producto a modificar: ")
                        p = buscar_id(id)
                        if p != -1:
                            nuevo_producto = input("Ingrese el nuevo nombre del producto: ")
                            nuevo_tamaño = input("Ingrese el nuevo tamaño: ")
                            nuevo_stock = int(input("Ingrese el nuevo stock: "))
                            nuevo_precio = int(input("Ingrese el nuevo precio: "))
                            p[1] = nuevo_producto
                            p[2] = nuevo_tamaño
                            p[3] = nuevo_stock
                            p[4] = nuevo_precio
                            print("Producto modificado exitosamente.")
                        else:
                            print("Error, id no existe")
                    case 5:
                        for p in productos:
                            print(p[0], " ", p[1], " ", p[2], " ", p[3], " ", p[4])
                        input("Presione Enter para continuar...")
                    case 6:
                        break
                    case _:
                        print("Error, debe ingresar un valor entre 1 y 6")
                        input("Presione Enter para continuar...")

        case 4:
              op = 0
              while op != 3:
                print("""
                    ADMINISTRACIÓN DE DATOS
                    1. Cargar datos desde archivos
                    2. Grabar datos en archivos
                    3. Salir al menú principal
                """)
                op = int(input("Ingrese una opción entre 1-3: "))
                match op:
                    case 1:
                        cargar_datos()
                        print("Datos cargados correctamente.")
                    case 2:
                        grabar_datos()
                        print("Datos grabados correctamente.")
                    case 3:
                        break
                    case _:
                        print("Error, debe ingresar un valor entre 1 y 3")
                        input("Presione Enter para continuar...")

        case 5:
          break
os.system("pause")