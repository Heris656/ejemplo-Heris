nombre = input("Ingrese su nombre: ")

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Porfa, ingresa tu edad en números.")
        
if edad < 18:
    print(f"wenas, {nombre} Eres menor de edad, no debes pagar impuestos.")

elif edad >= 18:  # Se usa elif en lugar de otro if, si no se usa imprimiria los dos mensajes.
    print(f"Wenas, {nombre} ¿Como que tienes {edad} años? Pagueee.")
    
elif edad == 18: 
    print(f"Usted {nombre} inicia a paguar impuesto")
