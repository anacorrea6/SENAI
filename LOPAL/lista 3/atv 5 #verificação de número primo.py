print("digite um número que eu vou  verificar se ele irá ser primo")

def verificarPrimo(x):
    cont = 0
    for i in range(1,x):
        if x%i==0:
            cont+=1

    if cont == 1:
        return (f"{x} O NÚMERO É PRIMO!")
    else:
        return (f"{x} O NÚMERO NÃO É PRIMO!")


num = int(input("digite um número:"))
print(verificarPrimo(num))
