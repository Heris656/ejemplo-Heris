nombre = input("Ingrese su nombre: ")

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido para la edad.")

print(f"Hola, {nombre}! Tienes {edad} años.")
