# 2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives.
# Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana 
# (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.


quantidade_votos = int(input("Por favor, informe quantos alunos irão votar "))

Segunda_feira = 0
Terça_feira = 0
Quarta_feira = 0
Quinta_feira = 0
Sexta_feira = 0
alunos = 0

for votos in range(1, quantidade_votos +1, 1):
    votação = input("Qual o melhor dia da semana para a realização das lives? SEGUNDA-FEIRA, TERÇA-FEIRA, QUARTA-FEIRA, QUINTA-FEIRA, SEXTA-FEIRA ")
    alunos = alunos + votos
    if votação.upper() == "SEGUNDA-FEIRA":
        Segunda_feira = Segunda_feira + 1
    elif votação.upper() == "TERÇA-FEIRA":
        Terça_feira = Terça_feira + 1    
    elif votação.upper() == "QUARTA-FEIRA":
        Quarta_feira = Quarta_feira + 1
    elif votação.upper() == "QUINTA-FEIRA":
        Quinta_feira = Quinta_feira + 1
    elif votação.upper() == "SEXTA-FEIRA":
        Sexta_feira = Sexta_feira + 1     
    else:
        print("Dia da semana inexistente, por favor, digite um dia da semana válido")
    
if Segunda_feira > Terça_feira and Segunda_feira > Quarta_feira and Segunda_feira > Quinta_feira and Segunda_feira > Sexta_feira:
    print("O dia da semana escolhido foi Segunda-feira")
elif Terça_feira > Segunda_feira and Terça_feira > Quarta_feira and Terça_feira > Quinta_feira and Terça_feira > Sexta_feira:
    print("O dia da semana escolhido foi Terça-feira")
elif Quarta_feira > Segunda_feira and Quarta_feira > Terça_feira and Quarta_feira > Quinta_feira and Quarta_feira > Sexta_feira:
    print("O dia da semana escolhido foi Quarta-feira")
elif Quinta_feira > Segunda_feira and Quinta_feira > Terça_feira and Quinta_feira > Quarta_feira and Quinta_feira > Sexta_feira:
    print("O dia da semana escolhida foi Quinta-feira")
elif Sexta_feira > Segunda_feira and Sexta_feira > Terça_feira and Sexta_feira > Quarta_feira and Sexta_feira > Quinta_feira:
    print("O dia da semana escolhido foi Sexta-feira")
else:
    print("Houve um empate, favor entrar em contato com a direção")              
                   