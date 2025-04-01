# -*- coding: UTF-8 -*-

while True:
    v = int(input("digite um número, porém quando se encerra em -999:"))
    if v == -999:
        print("voce encerrou, tchau")
        break
    triplo = v*3
    print(triplo)
