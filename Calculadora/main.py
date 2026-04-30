from calculadora import Calculator

def main():
    while True:
        print("\n" + "="*33)
        print("|{:^31}|".format("Calculadora"))
        print("="*33)
        print("| {:<2} {:<25}|".format("1.", "Sumar"))
        print("| {:<2} {:<25}|".format("2.", "Restar"))
        print("| {:<2} {:<25}|".format("3.", "Multiplicar"))
        print("| {:<2} {:<25}|".format("4.", "Dividir"))
        print("| {:<2} {:<25}|".format("5.", "Salir"))
        print("="*33)
        opcion = input("Seleccione una opción: ")

        if opcion == '5':
            print("Saliendo...")
            break

        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Debe ingresar valores numéricos.")
            continue

        calc = Calculator(num1, num2)

        if opcion == '1':
            print(f"Resultado: {calc.add()}")
        elif opcion == '2':
            print(f"Resultado: {calc.subtract()}")
        elif opcion == '3':
            print(f"Resultado: {calc.multiply()}")
        elif opcion == '4':
            print(f"Resultado: {calc.divide()}")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
