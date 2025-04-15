## actividad 1
'''
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("es mayor de edad")
'''
## actividad 2
'''
nota = int(input("ingrese su nota: "))
if nota >= 6:
    print("aprobado")
else:
    print("desaprobado")
'''
## actividad 3
'''
numero = int(input("ingrese un numero: "))
if numero % 2 == 0:
    print("es par")
else:
    print("es impar")
'''
## actividad 4
'''
edad = int(input("ingrese su edad: "))
if edad <= 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
'''
## actividad 5
'''
contraseña = input(print("ingrese una contraseña entre 8 y 14 caracteres: "))
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
'''
## actividad 6 
'''
import random 
from statistics import mode, median, mean 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
print(numeros_aleatorios)

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana < moda:
    print("sesgo positivo")
elif media < mediana < moda:
    print("sesgo negativo")
else:
    print("sin sesgo")
'''
## actividad 7
'''
frase = input("ingrese frase o palabra: ")
ultima_letra = frase[-1]
if ultima_letra in ("a", "A", "e", "E", "i", "I", "O", "o", "u", "U"):
    frase += "!"
print(frase)
'''
## actividad 8
'''
nombre = input("ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro")
opcion = input("elija su opcion: ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("opcion no valida")
'''
## actividad 9
'''
magnitud = float(input("Ingrese la magnitud del terremoto según la escala de Richter: "))
if magnitud < 3:
    print("muy leve")
elif 3 <= magnitud < 4:
    print("leve")
elif 4 <= magnitud < 5:
    print("moderado")
elif 5 <= magnitud < 6:
    print("fuerte")
elif 6 >= magnitud < 7:
    print("muy fuerte")
else:
    print("extremo")
'''
## ACTIVIDAD 10
emisferio = input("ingrese si encuentre el el emisferio sur con una s, en caso de estar en el emisferio norte ingrese n") 
mes = int(input("ingrese que numero de mes es: "))
dia = int(input("ingrese que numero del mes es: "))
if emisferio in ("s", "S"):
    if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
        print("VERANO")

    elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
        print("OTOÑO")
    elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
        print("INVIERNO")
    elif (mes == 9 and dia >= 21) or (mes in (10, 11)) or (mes == 12 and dia <= 20):
        print("PRIMAVERA")  
elif emisferio in ("n", "N"):
    if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
        print("INVIERNO")
    elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
        print("PRIMAVERA")
    elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
        print("VERANO")
    elif (mes == 9 and dia >= 21) or (mes in (10, 11)) or (mes == 12 and dia <= 20):
        print("OTOÑO")  


