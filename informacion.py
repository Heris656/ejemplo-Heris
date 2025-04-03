nombre = input("Ingresa tu nombre: ").strip()

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        break
    except ValueError:
        print("Porfis, coloca tu edad en números.")

if edad < 18:
    print(f"Wenas, {nombre} eres menor de edad, disfrutaaa.")
else:
    print(f"Wenas, {nombre} Cómo que tienes {edad} años? Jaja.")

