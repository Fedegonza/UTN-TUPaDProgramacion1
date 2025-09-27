# 1) Solicita la edad y determina si es mayor de edad
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")

# 2) Solicitar su nota al usuario

nota = int(input("ingrese su nota: "))

if nota >= 6:
    print("Aprobado!")
else:
    print("Desaprobado!")

# 3) Solicita un número y valida si es par
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Clasifica la edad en categorías
edad = int(input("Ingrese su edad: "))

if edad <= 12:
    print("Niño/a")
elif edad <= 18:
    print("Adolescente")
elif edad <=20:
    print("Adulto/a joven")
elif edad <=30:
    print("Adulto/a")

# 5) Verifica longitud de contraseña
password = input("Ingrese una contraseña: ")

if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

  # 7) Agrega un signo de exclamación si la palabra termina en vocal
frase = input("Ingrese una frase o palabra: ")

if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

# 8) Transforma el nombre según la opción elegida
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para la primera letra mayúscula: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")

# 9) Clasifica un terremoto según su magnitud
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

 # 10) Determina la estación del año según hemisferio, mes y día
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el número de mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
else:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

if hemisferio == "N":
    print("Estación:", estacion_norte)
elif hemisferio == "S":
    print("Estación:", estacion_sur)
else:
    print("Hemisferio inválido")

