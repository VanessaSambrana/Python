'''Hora de decidir! Os colaboradores da sua equipe foram sorteados para ganhar um console de última geração,cada um,em razãodo bom desempenho que tiveram
nos últimos projetos. Por uma questão de logística, porém, a empresa pede que todos os cinco membros da equipe recebam o mesmo aparelho.Crie um algoritmo em
que o usuário possa digitar o voto de cada um dos 5 membros da equipe e, ao final, exiba qual foi o console escolhido e com quantos votos. As opções são: 
PLAYSTATION, XBOX e NINTENDO'''

'''Fazer os exercícios usando condicionais'''

voto1 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX, NINTENDO ")
voto2 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX, NINTENDO ")
voto3 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX, NINTENDO ")
voto4 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX, NINTENDO ")
voto5 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX, NINTENDO ")

playstation = 0
xbox = 0
nintendo = 0

if voto1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto1.upper() == "XBOX":
    xbox = xbox + 1
elif voto1.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print ("O colaborador 1 digitou um console inexistente e seu voto será desconsiderado ")
    
if voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print ("O colaborador 2 digitou um console inexistente e seu voto será desconsiderado ")
    
if voto3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto3.upper() == "XBOX":
    xbox = xbox + 1
elif voto3.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print ("O colaborador 3 digitou um console inexistente e seu voto será desconsiderado ")
    
if voto4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto4.upper() == "XBOX":
    xbox = xbox + 1
elif voto4.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print ("O colaborador 4 digitou um console inexistente e seu voto será desconsiderado ")
    
if voto5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto5.upper() == "XBOX":
    xbox = xbox + 1
elif voto5.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print ("O colaborador 5 digitou um console inexistente e seu voto será desconsiderado ")
    
if playstation > xbox and playstation > nintendo:
    print ("O console escolhido foi o Playstation ")
elif xbox > playstation and xbox > nintendo:
    print ("O console escolhido foi o Xbox ")
elif nintendo > xbox and nintendo > playstation:
    print ("O console escolhido foi o Nintendo ")
else:
    print("Houve empate, favor entrar em contato com a direção ")
    

