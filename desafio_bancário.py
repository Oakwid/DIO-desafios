# importando datetime para manipulação de data e hora
from datetime import datetime

# Definindo visualização do menu

menu = """

==================== Menu ====================
[1]\tCriar Usuário
[2]\tCriar Conta Corrente
[3]\tDepositar
[4]\tSacar
[5]\tExtrato
[0]\tSair
===============================================

Selecione uma opção: 

"""

# Atribuindo variáveis principais

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
data = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# Definindo funções com comportamento de cada operação do manu
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios): # aqui encontrei uma solução diferente do professor.
        print("Já existe um usuário com este CPF.")
        return usuarios

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")
    return usuarios


def criar_conta_corrente(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if usuario:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        print(f"Conta corrente criada com sucesso! Agência: {agencia}, Número da Conta: {numero_conta}")
        return contas, numero_conta + 1
    else:
        print("Usuário não encontrado. Criação de conta corrente não realizada.")
        return contas, numero_conta

def depositar(saldo, valor, extrato, data, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\t{data}\n"
        return saldo, extrato, f"Depósito de R$ {valor:.2f} realizado com sucesso!\n"
    else:
        return saldo, extrato, "Valor inválido para depósito."
    

def sacar(*, saldo, valor, limite, numero_saques, extrato, data):
    if valor > saldo:
        return saldo, numero_saques, extrato, "Saldo insuficiente para saque."
    elif valor > limite:
        return saldo, numero_saques, extrato, "Valor acima do limite permitido para saque."
    elif numero_saques >= LIMITE_SAQUES:
        return saldo, numero_saques, extrato, "Número máximo de saques atingido."
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque:\t\t R$ {valor:.2f}\t{data}\n"
        return saldo, numero_saques, extrato, f"Saque de R$ {valor:.2f} realizado com sucesso!"
    
def exibir_extrato(saldo, data, /, *, extrato):
    print("======================= Extrato ====================")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"Saldo:\t\t R$ {saldo:.2f}\t{data}\n")
    print("====================================================")

# Definindo função para chamar o menu
    
def main_menu():
    global saldo, numero_saques, extrato

    usuarios = []
    contas = []
    agencia = "0001"
    numero_conta = 1

    while True:
        opcao = input(menu)
        
        if opcao == "1":
            usuarios = criar_usuario(usuarios)
            
        elif opcao == "2":
            contas, numero_conta = criar_conta_corrente(agencia, numero_conta, usuarios, contas)
      
        elif opcao == "3":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato, mensagem = depositar(saldo, valor, extrato, data)
            print(mensagem)
            
        elif opcao == "4":
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, numero_saques, extrato, mensagem = sacar(
                saldo=saldo,
                valor=valor,
                data=data,
                limite=limite, 
                numero_saques=numero_saques, 
                extrato=extrato)
            print(mensagem)
            
        elif opcao == "5":
            exibir_extrato(saldo, data, extrato=extrato)
            
        elif opcao == "0":
            print("Obrigado por ser nosso cliente! Saindo...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu

main_menu() 

