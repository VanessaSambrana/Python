'''Viajar  é  bom  demais!  Uma  agência  de  viagens  está  propondo  uma estratégia para alavancar as vendas após os impactos da pandemia do coronavírus.
A  empresa  ofertará  descontos  progressivos  na compra  de  pacotes, dependendo do número de viajantes que estão no mesmo grupo e moram na mesma 
residência.Para  ajudar  a  tornar  esse  projeto  real,  você  deve  criar  um  algoritmo  que receba o VALOR BRUTO do pacote, a CATEGORIA DOS ASSENTOS 
no voo e a QUANTIDADE  DE  VIAJANTES  que  moram  em  uma  mesma  casa  e  calcule  os descontos de acordo com a tabela abaixo

CategoriaDESCONTOS

Econômica 

2 viajantes 3% 
3 viajantes 4%
4 viajantes ou mais 5% 

Executiva

2 viajantes 5%
3 viajantes7% 
4 viajantes ou mais 8%

Primeira classe
2 viajantes 10%
3 viajantes 15%
4 viajantes ou mais 20% 

O programa deverá exibir o valor BRUTO DA VIAGEM (o mesmo que foi digitado), o VALOR DO DESCONTO, o VALOR LÍQUIDO DA VIAGEM (valor bruto menos os descontos)
e o VALOR MÉDIO POR VIAJANTE'''

valor_bruto = float(input("Por favor informe o valor bruto da viagem "))
categoria = input("Por favor informe a categoria: Econômica, Executiva ou Primeira classe ")
quantidade_viajantes = int(input("Por favor informe a quantidade de viajantes "))
valor_desconto = 0

if categoria.upper() == "ECONÔMICA":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.03
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.04
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.05
elif categoria.upper() == "EXECUTIVA":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.05
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.07
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.08
elif categoria.upper() == "PRIMEIRA CLASSE":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.1
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.15
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.2
else:
    print("Categoria inexixtente, não será concedido nenhum desconto")
    
valor_liquido = valor_bruto - valor_desconto
media_viajante = valor_liquido / quantidade_viajantes

print("O valor da viajem é de R${}. Após os descontos de R${}, a viagem custará R${}. Cada passageiro tem o custo médio de R${}".format(valor_bruto, valor_desconto, valor_liquido, media_viajante))
    