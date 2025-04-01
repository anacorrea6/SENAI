# -*- coding: UTF-8 -*-
cont = 0
acum = 0
while True:
    valor = float(input("""digite valores e no final lhe darei a média. Digite valor negativpo para sair: """))
    if valor < 0:
        print("voce escolheu sair")
        break
acum = acum + valor
cont = cont + 1
     # print (" a media dos valores digitados é de: %2f"% (acum / cont))
print (f"a media dos valores digitados é de: (acum/ cont:.2f)")
