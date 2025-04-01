# -*- coding: UTF-8 -*-
cont = 0
valores = 0
acum = 0
while True:
    valor= int(input("digite um valor:"))

    if valor < 0:
        break
    
    acum = acum + valor
    cont= cont + 1

    media = cont/ valor
    print (media)
