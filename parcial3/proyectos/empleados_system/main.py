from usuariosBD import conexion

def menu():
    bd = conexion(host='localhost', database='mi_empresa', user='root', password='')
    if conexion:
        while True:
            print("\n--- Menú de Opciones ---")
            print("1. Crear empleado")
            print("2. Leer empleados")
            print("3. Actualizar empleado")
            print("4. Eliminar empleado")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                nombre = input("Nombre: ")
                puesto = input("Puesto: ")
                salario = input("Salario: ")
                bd.crear_empleado(nombre, puesto, salario)

            elif opcion == '2':
                bd.leer_empleados()

            elif opcion == '3':
                id = input("ID del empleado a actualizar: ")
                nombre = input("Nuevo nombre: ")
                puesto = input("Nuevo puesto: ")
                salario = input("Nuevo salario: ")
                bd.actualizar_empleado(id, nombre, puesto, salario)

            elif opcion == '4':
                id = input("ID del empleado a eliminar: ")
                bd.eliminar_empleado(id)

            elif opcion == '5':
                bd.cerrar_conexion()
                break
            
            else:
                print("Opción no válida. Inténtalo de nuevo.")
    else:
        print(f"No se ha podido crear la conexion con la base de datos")

menu()