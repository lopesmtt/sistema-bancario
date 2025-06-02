from datetime import datetime
import json
import os

USUARIOS_FILE = "usuarios.json"
CONTAS_FILE = "contas.json"

usuarios = []
contas = []

# ---------------- Persistência ----------------
def salvar_dados():
    with open(USUARIOS_FILE, 'w') as f:
        json.dump(usuarios, f, indent=4)
    with open(CONTAS_FILE, 'w') as f:
        json.dump(contas, f, indent=4)

def carregar_dados():
    global usuarios, contas
    if os.path.exists(USUARIOS_FILE):
        with open(USUARIOS_FILE, 'r') as f:
            usuarios = json.load(f)
    if os.path.exists(CONTAS_FILE):
        with open(CONTAS_FILE, 'r') as f:
            contas = json.load(f)

# ---------------- Utilitários ----------------
def encontrar_usuario(cpf):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def encontrar_conta(numero):
    return next((conta for conta in contas if conta["numero"] == numero), None)

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    if encontrar_usuario(cpf):
        print("Usuário já existente com esse CPF!")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({"cpf": cpf, "nome": nome, "nascimento": nascimento, "endereco": endereco})
    salvar_dados()
    print("Usuário cadastrado com sucesso!")

def criar_conta():
    cpf = input("Informe o CPF do titular: ")
    usuario = encontrar_usuario(cpf)
    if not usuario:
        print("Usuário não encontrado! Cadastre-o primeiro.")
        return

    numero_conta = len(contas) + 1
    conta = {
        "agencia": "0001",
        "numero": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": [],
        "limite_saque": 3,
        "saques_hoje": 0,
        "ultimo_saque_data": ""
    }
    contas.append(conta)
    salvar_dados()
    print(f"Conta criada com sucesso! Número: {numero_conta}")

def depositar():
    numero = int(input("Informe o número da conta: "))
    conta = encontrar_conta(numero)
    if not conta:
        print("Conta não encontrada!")
        return

    valor = float(input("Valor do depósito: "))
    if valor <= 0:
        print("Valor inválido!")
        return

    conta["saldo"] += valor
    conta["extrato"].append(f"Depósito: +R$ {valor:.2f}")
    salvar_dados()
    print("Depósito realizado com sucesso!")

def sacar():
    numero = int(input("Número da conta: "))
    conta = encontrar_conta(numero)
    if not conta:
        print("Conta não encontrada!")
        return

    hoje = datetime.date.today().isoformat()
    if conta["ultimo_saque_data"] != hoje:
        conta["saques_hoje"] = 0
        conta["ultimo_saque_data"] = hoje

    if conta["saques_hoje"] >= conta["limite_saque"]:
        print("Limite diário de saques atingido!")
        return

    valor = float(input("Valor do saque: "))
    if valor <= 0 or valor > conta["saldo"]:
        print("Valor inválido ou saldo insuficiente!")
        return

    conta["saldo"] -= valor
    conta["extrato"].append(f"Saque: -R$ {valor:.2f}")
    conta["saques_hoje"] += 1
    salvar_dados()
    print("Saque realizado com sucesso!")

def mostrar_extrato():
    numero = int(input("Número da conta: "))
    conta = encontrar_conta(numero)
    if not conta:
        print("Conta não encontrada!")
        return

    print(f"\nEXTRATO da conta {conta['numero']}")
    print("\n".join(conta["extrato"]) if conta["extrato"] else "Nenhuma movimentação.")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}\n")

def listar_usuarios():
    print("\nUsuários cadastrados:")
    for u in usuarios:
        print(f"{u['nome']} - CPF: {u['cpf']}")

def listar_contas():
    print("\nContas cadastradas:")
    for c in contas:
        print(f"Agência: {c['agencia']}, Conta: {c['numero']}, Titular: {c['usuario']['nome']}")

# ---------------- Programa Principal ----------------
def menu():
    carregar_dados()
    while True:
        print("""
========= MENU =========
[1] Criar usuário
[2] Criar conta
[3] Depositar
[4] Sacar
[5] Extrato
[6] Listar usuários
[7] Listar contas
[0] Sair
========================
        """)
        opcao = input("Escolha uma opção: ")
        if opcao == "1": criar_usuario()
        elif opcao == "2": criar_conta()
        elif opcao == "3": depositar()
        elif opcao == "4": sacar()
        elif opcao == "5": mostrar_extrato()
        elif opcao == "6": listar_usuarios()
        elif opcao == "7": listar_contas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
