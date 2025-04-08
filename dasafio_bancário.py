menu = """

==================== Menu ====================
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Selecione uma opção: 

"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato, f"Depósito de R$ {valor:.2f} realizado com sucesso!\n"
    else:
        return saldo, extrato, "Valor inválido para depósito."
    

def sacar(saldo, valor, limite, numero_saques, extrato):
    if valor > saldo:
        return saldo, numero_saques, extrato, "Saldo insuficiente para saque."
    elif valor > limite:
        return saldo, numero_saques, extrato, "Valor acima do limite permitido para saque."
    elif numero_saques >= LIMITE_SAQUES:
        return saldo, numero_saques, extrato, "Número máximo de saques atingido."
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: R$ {valor:.2f}\n"
        return saldo, numero_saques, extrato, f"Saque de R$ {valor:.2f} realizado com sucesso!"
    

def exibir_extrato(saldo, extrato):
    print("==================== Extrato ====================")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"Saldo: R$ {saldo:.2f}")
    print("=================================================")
    
def main():
    global saldo, numero_saques, extrato
    while True:

        opcao = input(menu)
        
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato, mensagem = depositar(saldo, valor, extrato)
            print(mensagem)
            
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, numero_saques, extrato, mensagem = sacar(saldo, valor, limite, numero_saques, extrato)
            print(mensagem)
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
            
        elif opcao == "0":
            print("Obrigado por ser nosso cliente! Saindo...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")


main() 

