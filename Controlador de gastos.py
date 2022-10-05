'''Observandoo mercado de educação infantil, você e sua equipe decidem criar um aplicativo por meio do qualas crianças aprendam a controlar os seus gastos. Comoforma  de  validar  um 
protótipo,  foi  solicitado  que  você  crie  um  script simples,  em  que  o  usuário  deve  informar  QUANTAS  TRANSAÇÕES  financeiras realizou ao longo de um dia e, na sequência, deve 
informar o VALOR DE CADA UMA das transações que realizou.Seu  programa  deverá  exibir,  ao  final,  o  valor  total  gasto  pelo  usuário,  bem comoa média do valor de cada transação.'''

numero_transacoes = int(input("Por favor, informe a quantidade de transações "))
total_gasto = 0
media_valor = 0

for transacao in range(1, numero_transacoes + 1, 1):
    valor_transacao = float(input("Por favor, informe o valor da {} transação ".format(transacao)))
    total_gasto = total_gasto + valor_transacao
    media_valor = total_gasto / numero_transacoes
    
print("O total gasto durante o dia foi de R${}. E o valor médio de gastos por transação foi de R${} ".format(total_gasto, media_valor))
