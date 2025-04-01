print("digite o número que voce quer iniciar sua contagem regressiva")
num = int(input("digite o numero para que eu possa iniciar:"))

def contagem (num):
    for i in range (num, -1, -1):
        print (f"{i}")

contagem (num)
print("tenha um feliz ano novo")
