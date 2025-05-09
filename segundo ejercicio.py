from random import randint

# Desarrollar un programa en Python que permita ingresar dos números enteros que indiquen un
# rango numérico. El primer valor debe ser menor que el segundo. Luego, debe poder generar
# un número aleatorio (al azar) entre ese rango numérico.

valor = True
while valor:
    try:
        num1 = int(input("Ingrese primer valor del rango: "))
        num2 = int(input("Ingrese segundo valor del rango: "))
        
        if num2 < num1:
            print("El primer rango tiene que ser menor al número dos!!")
            continue
        
        numero = randint(num1, num2)
        print("################")
        print(f"#      {numero}      #")####### Valor del numero randint#######
        print("################")
        print(f"El numero a adivinar esta entre {num1} y {num2}.")
        
        cont = 3
        for i in range(3):
            adivinar = int(input("Adivine el número: "))
            
            if adivinar < num1 or adivinar > num2:
                print(f"El numero debe estar dentro del rango ({num1} - {num2}). Intenta nuevamente.")
                continue
            
            if adivinar == numero:
                print("Felicitaciones, pudiste adivinar el numero!")
                break
            elif adivinar < numero:
                cont = cont-1
                print(f"Te quedan {cont} intentos!!")
                print("El numero es mayor que", adivinar)
            elif adivinar > numero:
                cont = cont-1
                print(f"Te quedan {cont} intentos!!")
                print("El numero es menor que", adivinar)

        if cont == 0:
            print(f"Perdiste, el numero correcto era {numero}.")
        
        valor = False 

    except ValueError:
        print("Valor invalido, por favor ingrese un numero entero.")
