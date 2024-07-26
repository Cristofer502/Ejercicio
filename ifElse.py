from datetime import datetime

def main():
    while True:
        print("\nMenú:")
        print("1. Mostrar un saludo")
        print("2. Mostrar la fecha actual")
        print("3. Mostrar la hora actual")
        print("4. Salir")
        
        option = input("Selecciona una opción (1-4): ")
        
        if option == "1":
            print("¡Hola! ¿Cómo estás?")
        elif option == "2":
            print("Fecha actual:", datetime.now().strftime("%Y-%m-%d"))
        elif option == "3":
            print("Hora actual:", datetime.now().strftime("%H:%M:%S"))
        elif option == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")

main()
