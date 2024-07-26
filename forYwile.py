def sum_numbers(n):
    total = 0
    for i in range(n):
        number = float(input(f"Ingrese el número {i+1}: "))
        total += number
    return total

def main():
    count = int(input("¿Cuántos números desea sumar? "))

    if count <= 0:
        print("El número de entradas debe ser mayor que cero.")
        return

    total_sum = sum_numbers(count)

    print(f"La suma total es: {total_sum}")

    counter = 0
    while counter < 3:
        print("¡Gracias por usar el programa!")
        counter += 1

main()
