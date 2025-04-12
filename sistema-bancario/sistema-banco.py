import datetime

# Lista para armazenar os usuários e as contas
usuarios = []
contas = []

# Função do menu
def menu():
    return input(
        "\n===== MENU =====\n"
        "[u] Criar usuário\n"
        "[c] Criar conta corrente\n"
        "[d] Depositar\n"
        "[s] Sacar\n"
        "[e] Extrato\n"
        "[l] Listar contas\n"
        "[m] Mostrar conta e horário\n"
        "[r] Relatório de transações\n"
        "[g] Relatório geral de contas\n"
        "[q] Sair\n=> "
    )

# Função para criar usuários (agora com nome, data de nascimento, CPF e endereço)
def criar_usuario():
    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ")
    cpf = input("Informe seu CPF: ")
    endereco = input("Informe seu endereço: ")
    
    id_usuario = len(usuarios) + 1
    novo_usuario = {
        "id": id_usuario,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    }
    usuarios.append(novo_usuario)
    print(f"Usuário criado com sucesso! ID do usuário: {id_usuario}")

# Função para criar conta corrente vinculada a um usuário
def criar_conta_corrente():
    if not usuarios:
        print("Nenhum usuário cadastrado. Crie um usuário primeiro.")
        return

    id_usuario = int(input("Informe o ID do usuário para vincular à conta corrente: "))
    usuario = next((u for u in usuarios if u["id"] == id_usuario), None)
    
    if usuario:
        numero_agencia = "001"  # Definindo a agência fixa
        novo_id_conta = len(contas) + 1
        nova_conta_corrente = {
            "id": novo_id_conta,
            "usuario_id": usuario["id"],  # Vinculando a conta ao usuário
            "nome": usuario["nome"],
            "data_nascimento": usuario["data_nascimento"],
            "cpf": usuario["cpf"],
            "endereco": usuario["endereco"],
            "numero_agencia": numero_agencia,  # Agência fixa "001"
            "saldo": 0,
            "limite": 500,
            "saques": 0,
            "limite_saques": 3,
            "limite_transacoes": 10,
            "transacoes_diarias": 0,
            "extrato": []
        }
        contas.append(nova_conta_corrente)
        print(f"Conta corrente criada com sucesso! ID da conta corrente: {novo_id_conta}")
    else:
        print("Usuário não encontrado.")

# Função para depositar
def depositar(conta, valor):
    if conta["transacoes_diarias"] >= conta["limite_transacoes"]:
        print("Você excedeu o limite de transações permitidas por hoje!")
        return
    
    if valor > 0:
        conta["saldo"] += valor
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conta["extrato"].append(f"{data_hora} -- Depósito: R$ {valor:.2f}")
        conta["transacoes_diarias"] += 1
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido!")

# Função para sacar
def sacar(conta, valor):
    if conta["transacoes_diarias"] >= conta["limite_transacoes"]:
        print("Você excedeu o limite de transações permitidas por hoje!")
        return
    
    if valor > conta["saldo"]:
        print("Saldo insuficiente!")
    elif valor > conta["limite"]:
        print("O valor excede o limite de saque!")
    elif conta["saques"] >= conta["limite_saques"]:
        print("Número máximo de saques atingido!")
    elif valor > 0:
        conta["saldo"] -= valor
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conta["extrato"].append(f"{data_hora} -- Saque: R$ {valor:.2f}")
        conta["saques"] += 1
        conta["transacoes_diarias"] += 1
        print("Saque realizado com sucesso!")
    else:
        print("Valor inválido!")

# Função para exibir extrato
def exibir_extrato(conta):
    print("\n===== EXTRATO =====")
    print("\n".join(conta["extrato"]) if conta["extrato"] else "Sem movimentações.")
    print(f"Saldo: R$ {conta['saldo']:.2f}\n===================")

# Função para listar contas
def listar_contas():
    if contas:
        for conta in contas:
            print(f"ID: {conta['id']} | Agência: {conta['numero_agencia']} | Saldo: R$ {conta['saldo']:.2f}")
    else:
        print("Nenhuma conta cadastrada.")

# Função para mostrar conta específica
def mostrar_conta():
    try:
        id_conta = int(input("Informe o ID da conta: "))
        conta = next((conta for conta in contas if conta["id"] == id_conta), None)
        
        if conta:
            hora_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n===== CONTA {id_conta} =====")
            print(f"Nome: {conta['nome']}")
            print(f"Data de Nascimento: {conta['data_nascimento']}")
            print(f"CPF: {conta['cpf']}")
            print(f"Endereço: {conta['endereco']}")
            print(f"Agência: {conta['numero_agencia']}")
            print(f"Saldo: R$ {conta['saldo']:.2f}")
            print(f"Data e hora atual: {hora_atual}")
        else:
            print("Conta não encontrada.")
    except ValueError:
        print("ID inválido!")

# Função para gerar relatório de transações
def gerar_relatorio():
    if not contas:
        print("Nenhuma conta criada.")
        return

    try:
        id_conta = int(input("Informe o ID da conta: "))
        conta = next((conta for conta in contas if conta["id"] == id_conta), None)

        if not conta:
            print("Conta não encontrada!")
            return

        transacoes_filtradas = [t for t in conta["extrato"] if "Depósito" in t or "Saque" in t]
        if not transacoes_filtradas:
            print("Nenhuma transação de saque ou depósito encontrada.")
            return

        print("\n===== RELATÓRIO DE TRANSAÇÕES =====")
        for transacao in transacoes_filtradas:
            print(transacao)
            continuar = input("Pressione Enter para próxima ou 'q' para sair: ")
            if continuar.lower() == 'q':
                break
        print("Fim do relatório.")

    except ValueError:
        print("ID inválido!")

# Nova função: Relatório geral de contas
def relatorio_geral():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\n===== RELATÓRIO GERAL DE CONTAS =====")
    for conta in contas:
        print(f"\nID: {conta['id']}")
        print(f"Nome: {conta['nome']}")
        print(f"Data de Nascimento: {conta['data_nascimento']}")
        print(f"CPF: {conta['cpf']}")
        print(f"Endereço: {conta['endereco']}")
        print(f"Agência: {conta['numero_agencia']}")
        print(f"Saldo atual: R$ {conta['saldo']:.2f}")
        print(f"Transações hoje: {conta['transacoes_diarias']} de {conta['limite_transacoes']}")
        print("-" * 30)

# Loop principal
while True:
    opcao = menu()
    
    if opcao == "u":
        criar_usuario()

    elif opcao == "c":
        criar_conta_corrente()

    elif opcao == "d":
        if contas:
            try:
                id_conta = int(input("Informe o ID da conta: "))
                conta = next((conta for conta in contas if conta["id"] == id_conta), None)
                if conta:
                    valor = float(input("Valor do depósito: "))
                    depositar(conta, valor)
                else:
                    print("Conta não encontrada.")
            except ValueError:
                print("ID ou valor inválido.")
        else:
            print("Nenhuma conta criada.")

    elif opcao == "s":
        if contas:
            try:
                id_conta = int(input("Informe o ID da conta: "))
                conta = next((conta for conta in contas if conta["id"] == id_conta), None)
                if conta:
                    valor = float(input("Valor do saque: "))
                    sacar(conta, valor)
                else:
                    print("Conta não encontrada.")
            except ValueError:
                print("ID ou valor inválido.")
        else:
            print("Nenhuma conta criada.")

    elif opcao == "e":
        if contas:
            try:
                id_conta = int(input("Informe o ID da conta: "))
                conta = next((conta for conta in contas if conta["id"] == id_conta), None)
                if conta:
                    exibir_extrato(conta)
                else:
                    print("Conta não encontrada.")
            except ValueError:
                print("ID inválido.")
        else:
            print("Nenhuma conta criada.")

    elif opcao == "l":
        listar_contas()

    elif opcao == "m":
        mostrar_conta()

    elif opcao == "r":
        gerar_relatorio()

    elif opcao == "g":
        relatorio_geral()

    elif opcao == "q":
        print("Obrigado por usar nosso banco!")
        break

    else:
        print("Opção inválida!")