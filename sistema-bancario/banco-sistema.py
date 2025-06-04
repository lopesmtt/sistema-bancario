import json
import os
from datetime import datetime, date

BANCO_FILE = "banco.json"

class Usuario:
    def __init__(self, cpf, nome, nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.endereco = endereco

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Usuario(**data)

class Conta:
    def __init__(self, numero, agencia, usuario_cpf, saldo=0, saques_hoje=0, ultimo_saque_data=""):
        self.numero = numero
        self.agencia = agencia
        self.usuario_cpf = usuario_cpf
        self.saldo = saldo
        self.saques_hoje = saques_hoje
        self.ultimo_saque_data = ultimo_saque_data

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Conta(**data)

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.transacoes = []
        self.carregar_dados()

    def salvar_dados(self):
        with open(BANCO_FILE, "w") as f:
            json.dump({
                "usuarios": [u.to_dict() for u in self.usuarios],
                "contas": [c.to_dict() for c in self.contas],
                "transacoes": self.transacoes
            }, f, indent=4)

    def carregar_dados(self):
        if os.path.exists(BANCO_FILE):
            with open(BANCO_FILE, "r") as f:
                data = json.load(f)
                self.usuarios = [Usuario.from_dict(u) for u in data.get("usuarios", [])]
                self.contas = [Conta.from_dict(c) for c in data.get("contas", [])]
                self.transacoes = data.get("transacoes", [])

    def encontrar_usuario(self, cpf):
        return next((u for u in self.usuarios if u.cpf == cpf), None)

    def encontrar_conta(self, numero):
        return next((c for c in self.contas if c.numero == numero), None)

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente números): ")
        if self.encontrar_usuario(cpf):
            print("Usuário já existente com esse CPF!")
            return
        nome = input("Nome completo: ")
        nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ")
        self.usuarios.append(Usuario(cpf, nome, nascimento, endereco))
        self.salvar_dados()
        print("Usuário cadastrado com sucesso!")

    def criar_conta(self):
        cpf = input("Informe o CPF do titular: ")
        if not self.encontrar_usuario(cpf):
            print("Usuário não encontrado! Cadastre-o primeiro.")
            return
        numero = len(self.contas) + 1
        conta = Conta(numero=numero, agencia="0001", usuario_cpf=cpf)
        self.contas.append(conta)
        self.salvar_dados()
        print(f"Conta criada com sucesso! Número: {numero}")

    def depositar(self):
        numero = int(input("Número da conta: "))
        conta = self.encontrar_conta(numero)
        if not conta:
            print("Conta não encontrada!")
            return
        valor = float(input("Valor do depósito: "))
        if valor <= 0:
            print("Valor inválido!")
            return
        conta.saldo += valor
        self.transacoes.append({
            "conta": conta.numero,
            "tipo": "Depósito",
            "valor": valor,
            "horario": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.salvar_dados()
        print("Depósito realizado com sucesso!")

    def sacar(self):
        numero = int(input("Número da conta: "))
        conta = self.encontrar_conta(numero)
        if not conta:
            print("Conta não encontrada!")
            return
        hoje = date.today().isoformat()
        if conta.ultimo_saque_data != hoje:
            conta.saques_hoje = 0
            conta.ultimo_saque_data = hoje
        if conta.saques_hoje >= 3:
            print("Limite diário de saques atingido!")
            return
        valor = float(input("Valor do saque: "))
        if valor <= 0 or valor > conta.saldo:
            print("Valor inválido ou saldo insuficiente!")
            return
        conta.saldo -= valor
        conta.saques_hoje += 1
        self.transacoes.append({
            "conta": conta.numero,
            "tipo": "Saque",
            "valor": valor,
            "horario": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.salvar_dados()
        print("Saque realizado com sucesso!")

    def extrato(self):
        numero = int(input("Número da conta: "))
        conta = self.encontrar_conta(numero)
        if not conta:
            print("Conta não encontrada!")
            return
        print(f"\nEXTRATO da conta {conta.numero}")
        transacoes = [t for t in self.transacoes if t["conta"] == numero]
        if not transacoes:
            print("Nenhuma movimentação.")
        else:
            for t in transacoes:
                tipo = t["tipo"]
                valor = t["valor"]
                horario = t["horario"]
                print(f"{horario} - {tipo}: {'+' if tipo == 'Depósito' else '-'}R$ {valor:.2f}")
        print(f"Saldo atual: R$ {conta.saldo:.2f}\n")

    def listar_usuarios(self):
        print("\nUsuários cadastrados:")
        for u in self.usuarios:
            print(f"{u.nome} - CPF: {u.cpf}")

    def listar_contas(self):
        print("\nContas cadastradas:")
        for c in self.contas:
            usuario = self.encontrar_usuario(c.usuario_cpf)
            print(f"Agência: {c.agencia}, Conta: {c.numero}, Titular: {usuario.nome if usuario else 'Desconhecido'}")

def menu():
    banco = Banco()
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
        if opcao == "1":
            banco.criar_usuario()
        elif opcao == "2":
            banco.criar_conta()
        elif opcao == "3":
            banco.depositar()
        elif opcao == "4":
            banco.sacar()
        elif opcao == "5":
            banco.extrato()
        elif opcao == "6":
            banco.listar_usuarios()
        elif opcao == "7":
            banco.listar_contas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
