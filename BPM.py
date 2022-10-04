'''Verificar se os batimentos cardíacos por minuto se encontram na faixa adequada. Para isso, você deve solicitar ao usuário que informe o seu número de
BATIMENTOS POR MINUTO (BPM) e a IDADE. A partir disso,o script deve verificar e  exibir  uma  mensagem  informando  se  os  batimentos  do  usuário  
encontram-se DENTRO  da  faixa  adequada,  ACIMA  da  faixa  adequada  ou  ABAIXO  da  faixa adequada, de acordo com o site Tua Saúde'''

'''Até 2 anos de idade: 120 a 140 bpm,
Entre 8 anos até 17 anos: 80 a 100 bpm,
Adulto entre 18 até 60 anos: 70 a 80 bpm,
Idosos acima de 60 anos: 50 a 60 bpm.'''

print ("Verificador de frequências cardácas")
idade = int(input("Por favor, informe a sua idade "))
bpm = int(input("Por favor, informe seu número de batimentos por minuto (BPM) "))

atividade_fisica = ("Você pratica atividade física? (s/n)")

if idade <= 2:
    if bpm >= 120:
        if bpm <= 140:
            print ("Frequência cardíaca dentro da faixa adequada")
        else:
            print ("Frequência cardíaca acima da faixa adequada")
    else:
        print ("Frequência cardíaca abaixo da faixa adequada")     
elif idade >= 8 and idade <= 17:
    if bpm >= 80:
        if bpm <= 100:
            print ("Frequência cardíaca dentro da faixa adequada")
        else:
            print ("Frequência cardíaca acima da faixa adequada")
    else:
        print ("Frequência cardíaca abaixo da faixa adequada")
elif idade >= 18 and idade <= 60:
    if bpm >= 70:
        if bpm <= 80:
            print ("Frequência cardíaca dentro da faixa adequada")
        else:
            print ("Frequência cardíaca acima da faixa adequada")
    else:
        print ("Frequência cardíaca abaixo da faixa adequada")
elif idade >= 60:
    if bpm >= 50:
        if bpm <= 60:
            print ("Frequência cardíaca dentro da faixa adequada")
        else:
            print ("Frequência cardíaca acima da faixa adequada")
    else:
        print ("Frequência cardíaca abaixo da faixa adequada")
else:
    print ("Não foi possível verificar os batimentos para essa idade")


    
    


    
    