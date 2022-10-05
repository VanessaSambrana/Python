def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    if(b!=0):
        return a / b
    return 0

def multiplicar(a, b):
    return a * b

op = -1
while op!=5:
    print("1 - Somar dois valores")
    print("2 - Subtrair dois valores")
    print("3 - Dividir dois valores")
    print("4 - Multiplicar dois valores")
    
    op = int(input("Digite a sua opção! "))
    if(op==1):
        print(somar(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor:  "))))
    elif(op==2):
        print(subtrair(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor:  "))))
    elif(op==3):
        print(dividir(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor:  "))))
    elif(op==4):
        print(multiplicar(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor:  "))))