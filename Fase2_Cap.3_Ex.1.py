tipo_de_assinatura = input("Por favor, informe o tipo de assinatura: BASIC, SILVER, GOLD OU PLATINUM ")
faturamento_anual = float(input("Por favor, informe o faturamento anual "))
bonus = 0

if tipo_de_assinatura.upper() == "BASIC":
    bonus = faturamento_anual * 0.3
elif tipo_de_assinatura.upper() == "SILVER":
    bonus = faturamento_anual * 0.2
elif tipo_de_assinatura.upper() == "GOLD":
    bonus = faturamento_anual * 0.1
elif tipo_de_assinatura.upper() == "PLATINUM":
    bonus = faturamento_anual * 0.05
else:
    print("Tipo de assinatura inexistete, não será concedido nenhum bônus") 
    
print("O clinte deve pagar R${:.2f} de bônus".format(bonus))                    
