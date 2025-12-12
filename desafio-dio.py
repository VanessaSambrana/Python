import textwrap

def exibir_menu():
    opcoes = """
    ========= MENU =========

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta
    [6] Listar Contas
    [0] Sair

    => """
    return input(textwrap.dedent(opcoes))


def operacao_deposito(conta, valor, /):
    if valor <= 0:
        print("\n Valor inválido para depósito. ")
        return
    
    conta["saldo"] += valor
    conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
    print("\n Depósito concluído! ")


def operacao_saque(conta, valor, max_saques):
    if conta["saques_realizados"] >= max_saques:
        print("\n Limite diário de saques atingido. ")
        return

    if valor <= 0:
        print("\n Valor de saque inválido. ")
        return

    if valor > conta["saldo"]:
        print("\n Saldo insuficiente. ")
        return

    conta["saldo"] -= valor
    conta["saques_realizados"] += 1
    conta["extrato"].append(f"Saque: R$ {valor:.2f}")
    print("\n Saque efetuado! ")


def mostrar_extrato(saldo, /, *, extrato):
    print("\n========= EXTRATO =========")

    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for linha in extrato:
            print(linha)

    print(f"\n Saldo atual: R$ {saldo:.2f}")
    print("===========================")


def localizar_usuario(cpf, banco_usuarios):
    for usuario in banco_usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def cadastrar_usuario(banco_usuarios):
    cpf = input("Informe o CPF: ")
    if localizar_usuario(cpf, banco_usuarios):
        print("\n Já existe um usuário com esse CPF. ")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ")

    novo = {
        "nome": nome,
        "cpf": cpf,
        "nascimento": nascimento,
        "endereco": endereco
    }

    banco_usuarios.append(novo)
    print("\n Usuário cadastrado com sucesso! ")


def criar_conta_corrente(agencia, banco_usuarios, lista_contas):
    cpf = input("CPF do titular: ")
    usuario = localizar_usuario(cpf, banco_usuarios)

    if not usuario:
        print("\n Usuário não encontrado. ")
        return

    numero = len(lista_contas) + 1
    conta = {
        "agencia": agencia,
        "numero": numero,
        "titular": usuario,
        "saldo": 0,
        "extrato": [],
        "saques_realizados": 0
    }

    lista_contas.append(conta)
    print("\n Conta criada com sucesso! ")


def listar_todas_contas(lista_contas):
    if not lista_contas:
        print("\nNenhuma conta registrada. ")
        return

    print("\n========= CONTAS =========")
    for conta in lista_contas:
        print(f"""
        Agência: {conta['agencia']}
        Conta:   {conta['numero']}
        Titular: {conta['titular']['nome']}
        -------------------------""")

def main():
    AGENCIA_PADRAO = "0001"
    LIMITE_SAQUES_DIA = 3

    usuarios = []
    contas = []

    while True:
        escolha = exibir_menu()

        if escolha == "1":
            if not contas:
                print("\n Nenhuma conta criada ainda. ")
                continue

            numero = int(input("Informe o número da conta: "))
            conta = next((conta for conta in contas if conta["numero"] == numero), None)

            if not conta:
                print("\n Conta não encontrada. ")
                continue

            valor = float(input("Valor do depósito: "))
            operacao_deposito(conta, valor)

        elif escolha == "2":
            if not contas:
                print("\n Nenhuma conta criada ainda. ")
                continue

            numero = int(input("Número da conta: "))
            conta = next((conta for conta in contas if conta["numero"] == numero), None)

            if not conta:
                print("\n Conta não encontrada. ")
                continue

            valor = float(input("Valor do saque: "))
            operacao_saque(conta, valor, LIMITE_SAQUES_DIA)

        elif escolha == "3":
            if not contas:
                print("\n Nenhuma conta para exibir extrato. ")
                continue

            numero = int(input("Número da conta: "))
            conta = next((conta for conta in contas if conta["numero"] == numero), None)

            if conta:
                mostrar_extrato(conta["saldo"], extrato=conta["extrato"])
            else:
                print("\n Conta não encontrada. ")


        elif escolha == "4":
            cadastrar_usuario(usuarios)

        elif escolha == "5":
            criar_conta_corrente(AGENCIA_PADRAO, usuarios, contas)

        elif escolha == "6":
            listar_todas_contas(contas)

        elif escolha == "0":
            print("\nSaindo... até a próxima!")
            break

        else:
            print("\n Opção inválida, tente novamente. ")


main()
