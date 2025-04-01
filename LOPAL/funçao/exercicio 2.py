# -*- coding: UTF-8 -*-

def multiplo(a, b):
    if a % b == 0 :
        return True
    else:
        return False

valor = int(input("digite um valor:"))
valor2 = int(input("digite outro valor:"))

resultado = multiplo (valor, valor2)

if resultado:
     print ("os numeros são multiplicavéis")
else:
    print ("não são multiplos")
