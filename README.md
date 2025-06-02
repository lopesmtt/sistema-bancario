# Sistema Bancário em Python

## Descrição

Este é um sistema bancário simples desenvolvido em Python que permite gerenciar usuários, contas, depósitos, saques e consultar extratos com histórico detalhado de transações incluindo data e hora.

Os dados são persistidos em arquivos JSON para que as informações sejam mantidas entre execuções.

---

## Funcionalidades

- **Cadastro de Usuários**: Permite cadastrar usuários informando CPF, nome completo, data de nascimento e endereço.
- **Criação de Contas Bancárias**: Cria contas vinculadas a usuários já cadastrados. Cada conta possui número, agência, saldo e histórico de movimentações.
- **Depósitos**: Permite realizar depósitos nas contas, registrando o valor e o timestamp (data e hora) da operação.
- **Saques**: Permite realizar saques com limite diário (configurado para 3 saques por dia), validando saldo disponível e registrando data e hora.
- **Extrato Bancário**: Exibe o extrato da conta com todas as transações (depósitos e saques), cada uma com data e hora detalhadas, além do saldo atual.
- **Listagem de Usuários e Contas**: Exibe usuários cadastrados e contas existentes para facilitar a consulta.

---

## Estrutura dos Dados

- `usuarios.json`: Armazena os dados dos usuários cadastrados.
- `contas.json`: Armazena os dados das contas, incluindo o saldo e o histórico de transações.

---

## Como Usar

1. Clone ou baixe este repositório.
2. Execute o script Python:

```bash
python banco-sistema.py
# Sistema Bancário


