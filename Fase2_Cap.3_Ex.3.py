'''Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês 
JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: 

o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm 
número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.


Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte
padrão:

VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.'''

soma = 0
cont = 0
for ímpar in range(1, 51, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
    notas_alunos_ímpar = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {} ".format(ímpar)))
    soma = soma + notas_alunos_ímpar
    cont = cont + 1
    media_ímpar = soma / cont
print("A MÉDIA DAS NOTAS DOS ALUNOS QUE TEM NÚMEROS ÍMPAR NA CHAMADA É {}".format(media_ímpar))
    
soma = 0    
cont = 0
for par in range(2, 51, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    notas_alunos_par = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {} ".format(par)))
    soma = soma + notas_alunos_par
    cont = cont + 1
    media_par = soma / cont
print("A MÉDIA DAS NOTAS DOS ALUNOS QUE TEM NÚMEROS PAR NA CHAMADA É {}".format(media_par))
    
if media_ímpar > media_par:
    print("A MAIOR MÉDIA DAS NOTAS, É DA TURMA ÍMPAR COM A MÉDIA {}".format(media_ímpar))
else:
    print(" MAIOR MÉDIA DAS NOTAS, É DA TURMA PAR COM A MÉDIA {}".format(media_par))        
     

