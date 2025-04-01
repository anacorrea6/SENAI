# -*- coding: UTF-8 -*-
v = int(input("entre com números positivos e imprima quantos números foram digitados:"))
contador = 0
while True:
    num = int(input("digite um número: "))
    if num < 0:
        print ("voce escolheu sair")
        contador = contador + 1
        print ("o número foi contado")
        
    
        
