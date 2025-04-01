print("digite a velocidade do carro, que eu falarei a sua multa")
velocidade= int(input("digite a velocidade do carro:"))
multa = (velocidade - 80) *5

if velocidade > 80:
    print (f"voce foi multado no valor de {multa} reais")
   
else:
    print("tudo certo")
