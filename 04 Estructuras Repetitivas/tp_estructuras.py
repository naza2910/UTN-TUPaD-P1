##Actividad 1
'''
for x in range (0, 100, 1):
    print (x)
'''
##Actividad 2
'''
num_entero = int(input("ingrese un numero entero: "))
cantidad_digitos = len(str(abs(num_entero)))
print(f"El número {num_entero} tiene {cantidad_digitos} dígitos")
'''
#actividad 3
'''
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
if num1 < num2:
    inicio = num1
    fin = num2
else:
    inicio = num2
    fin = num1
suma = 0
for x in range(inicio + 1, fin):
    suma += x
print(f"La suma de los números entre {inicio} y {fin}, excluyéndolos, es: {suma}")
'''
#actividad 4
'''
num_entero = int(input("ingrese un numero entero (para detener ponga 0) "))
sumatoria = 0
while num_entero != 0:
    sumatoria += num_entero
    num_entero = int(input("Ingresa otro número (para detener ponga 0) "))
print(f"La suma total de los números ingresados es: {sumatoria}")
'''
#actividad 5
'''
import random
numero_aleatorio = random.randint (0,9)
num = int(input("ingresa un numero del 0 al 9 para adivinar"))
cont_intentos = 1
while num != numero_aleatorio:
    print("¡INCORRECTO!")
    num = int(input("ingresa otro numero del 0 al 9 para adivinar"))
    cont_intentos += 1
print(f"¡ADIVINASTE! Lo lograste en {cont_intentos} intento(s).")
'''
##actividad 6
'''
for x in range (100, 0, -2):
    print(x)
'''
##actividad 7
'''
num = int(input("ingrese un numero entero positivo"))
sumatoria = 0
for x in range (0, num, 1):
    sumatoria += x
print(f"la suma de los numeros del 0 al {num} = {sumatoria}")
'''
## actividad 8
'''
cantidad = int(input("¿Cuántos números enteros vas a ingresar?"))
cont_impar = 0
cont_par = 0
cont_positivos= 0
cont_negativos = 0
for x in range (cantidad):
    num = int(input(f"Ingrese el número {x + 1}: "))
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

    if num > 0:
        cont_positivos += 1
    elif num < 0:
        cont_negativos += 1
print(f"Pares: {cont_par}")
print(f"Impares: {cont_impar}")
print(f"Positivos: {cont_positivos}")
print(f"Negativos: {cont_negativos}")
'''
##actividad 9
'''
cantidad = int(input("¿Cuántos números enteros vas a ingresar?"))
suma = 0
for x in range (cantidad):
    num = int(input(f"Ingrese el número {x + 1}: "))
    suma += num
promedio = suma / cantidad
print(f"el promedio los numeros ingresados es: {promedio}")
'''
##actividad 10 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
##usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745
num = int(input("ingrese un numero para invertirlo"))
num_cadena = str(abs(num))
num_invertido = num_cadena[::-1]
num_invertido = int(num_invertido)
if num < 0:
    num_invertido = -num_invertido
print(f"El número invertido es: {num_invertido}")