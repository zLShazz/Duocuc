stock = 20
reserva = []
reservadas = 0

def hacer_reserva():
    global stock, reservadas
    nombre = input("Ingrese su nombre: ")
    frase = input("Ingrese frase secreta: ")
    if frase == "EstoyEnListaDeReserva":
        if stock > 0:
            print("La reserva se ejecuto correctamente.")
            persona = {"nombre": nombre, "estado": "normal"}
            reserva.append(persona)
            stock -= 1
            reservadas += 1
        else:
            print("No hay stock disponible.")
    else:
        print("Error... Frase incorrecta.")

def buscar():
    nombre = input("Nombre de reserva: ")
    for F in reserva:
        if F["nombre"] == nombre:
            print("¿Desea pagar adicional para VIP y reservar 2 pares?")
            vip = input("S/N: ").lower()
            if vip == "s":
                F["estado"] = "vip"
                print("Estado actualizado a VIP.")
            else:
                print("Saliendo de la búsqueda.")
            return
    print("Reserva no encontrada.")

def borrar():
    global reservadas, stock
    if not reserva:
        print("No hay reservas para cancelar.")
        return

    nombre = input("Ingrese el nombre de la reserva que desea cancelar: ")
    for F in reserva:
        if F["nombre"] == nombre:
            reserva.remove(F)
            stock += 1
            reservadas -= 1
            print(f"Reserva de '{nombre}' cancelada correctamente.")
            return

    print("No se encontró esa reserva.")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Reservar Zapatillas")
        print("2. Buscar Zapatillas Reservadas")
        print("3. Cancelar Reserva de Zapatillas")
        print("4. Salir")

        try:
            op = int(input("Elegir opcion: "))
            if op == 1:
                hacer_reserva()
            elif op == 2:
                buscar()
            elif op == 3:
                borrar()
            elif op == 4:
                print("Saliendo del programa...")
                break
            else:
                print("Debe ingresar una opcion válida.")
        except ValueError:
            print("Debe ingresar un numero valido.")

menu()