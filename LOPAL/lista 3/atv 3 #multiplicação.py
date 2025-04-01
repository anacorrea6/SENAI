print("me de um numero de 1 a 10 e lhe mostrarei a tabuada dele")
num= int(input("digite o valor que voce quer a tabuada:"))

def tabuada (num):
    for i in range (1,11):
            print (f"{num} * {i} = {num*i}")
tabuada(num)
