# ============================================================================ #
# Objetivo Geral
# ============================================================================ #
 
# Iniciar a modelagem do sistema bancário em POO. Adicionar classes para cliente
# e as operações bancárias: depósito e saque.

from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

# ============================================================================ #
# Desafio

# Atualiza a implementação do sistema bancário, para armazenar os dados de clientes
# e contas bancárias em objetos ao invés de dicionários

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class PessoaJuridica(Cliente):
    def __init__(self, nome_fantasia, data_fundacao, cnpj, endereco):
        super().__init__(endereco)
        self.nome_fantasia = nome_fantasia
        self.data_fundacao = data_fundacao
        self.cnpj = cnpj

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0 # Atributos diretamente
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def data(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n❗❗❗ Saldo insuficiente para saque. ❗❗❗")

        elif valor > 0:
            self._saldo -= valor
            print("\n✔ Saque realizado com sucesso! ✔")
            return True

        else:
            print("\n⛔ Operação falhou! O valor informado é inválido. ⛔")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n✔ Depósito realizado com sucesso! ✔")
        else:
            print("\n⛔ Operação falhou! O valor informado é inválido. ⛔")
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n⛔ Operação falhou! O valor do saque excede o limite. ⛔")

        elif excedeu_saques:
            print("\n⛔ Operação falhou! Número máximo de saques excedido. ⛔")

        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        titular = self.cliente.nome if isinstance(self.cliente, PessoaFisica) else self.cliente.nome_fantasia
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero} 
            Titular:\t{titular} 
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    @property
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# ============================================================================ #
# Desafio Extra

# Atualiza os métodos e funções que tratam as opções do menu, para funcionarem
# com as classes modeladas.


def menu_banco():
    menu = """
    \n==================== MEU DO BANCO ====================\n
    1.\tSeja nosso cliente (Pessoa Física ou Jurídica)
    2.\tCriar conta
    3.\tRealizar depósito
    4.\tRealizar saque
    5.\tHistórico de Transações
    6.\tListar contas
    7.\tSair
    \n======================================================
    Digite uma opção: 
    """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf_cnpj, clientes):
        clientes_filtrados = [
            cliente for cliente in clientes
            if (isinstance(cliente, PessoaFisica) and cliente.cpf == cpf_cnpj) or
               (isinstance(cliente, PessoaJuridica) and cliente.cnpj == cpf_cnpj)
        ]
        return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n⛔ Cliente ainda não possui conta. Verifique o CPF ou CNPJ informado. ⛔")
        return None

    # Exibe as contas do cliente
    print("\nContas disponíveis:")
    for i, conta in enumerate(cliente.contas, start=1):
        print(f"{i} - Agência: {conta.agencia}, Conta: {conta.numero}")

    # Solicita ao usuário que escolha uma conta
    escolha = int(input("Selecione o número da conta: "))
    if 1 <= escolha <= len(cliente.contas):
        return cliente.contas[escolha - 1]
    else:
        print("\n⛔ Opção inválida. Tente novamente. ⛔")
        return None
    
def depositar(clientes):
    cpf_cnpj = input("Informe o CPF ou CNPJ do cliente: ")
    cliente = filtrar_cliente(cpf_cnpj, clientes)

    if not cliente:
        print("\n⛔ Cliente não encontrado. Verifique o CPF ou CNPJ informado. ⛔")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf_cnpj = input("Informe o CPF ou CNPJ do cliente: ")
    cliente = filtrar_cliente(cpf_cnpj, clientes)

    if not cliente:
        print("\n⛔ Cliente não encontrado. Verifique o CPF ou CNPJ informado. ⛔")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf_cnpj = input("Informe o CPF ou CNPJ do cliente: ")
    cliente = filtrar_cliente(cpf_cnpj, clientes)

    if not cliente:
        print("\n⛔ Cliente não encontrado. Verifique o CPF ou CNPJ informado. ⛔")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n======================= Extrato =====================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "\n⛔ Não foram realizadas movimentações. ⛔"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\t R${transacao['valor']:.2f}\t{transacao['data']}"
    
    print(extrato)
    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}\t{conta.data}")
    print("=" * 54)

def criar_cliente(clientes):
    tipo_cliente = input("O cliente é Pessoa Física (1) ou Pessoa Jurídica (2)? ")

    if tipo_cliente == "1":
        cpf = input("Informe o CPF (somente números): ")
        if any(cliente.cpf == cpf for cliente in clientes if isinstance(cliente, PessoaFisica)):
            print("Já existe um cliente com este CPF.")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

        cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
        clientes.append(cliente)
        print("Cliente Pessoa Física criado com sucesso!")

    elif tipo_cliente == "2":
        cnpj = input("Informe o CNPJ (somente números): ")
        if any(cliente.cnpj == cnpj for cliente in clientes if isinstance(cliente, PessoaJuridica)):
            print("Já existe um cliente com este CNPJ.")
            return

        nome_fantasia = input("Informe o nome fantasia: ")
        data_fundacao = input("Informe a data de fundação (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

        cliente = PessoaJuridica(nome_fantasia, data_fundacao, cnpj, endereco)
        clientes.append(cliente)
        print("Cliente Pessoa Jurídica criado com sucesso!")

    else:
        print("Opção inválida. Tente novamente.")

def criar_conta(numero_conta, clientes, contas):
    cpf_cnpj = input("Informe o CPF ou CNPJ do cliente: ")
    cliente = filtrar_cliente(cpf_cnpj, clientes)

    if not cliente:
        print("\n⛔ Cliente não encontrado. Verifique o CPF ou CNPJ informado. ⛔")
        return

    conta = ContaCorrente.nova_conta(
        cliente = cliente,
        numero = numero_conta
    )
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n✔ Conta criada com sucesso! ✔")

def listar_contas(clientes):
    if not clientes:
        print("\n⛔ Nenhum cliente cadastrado. ⛔")
        return
    
    cpf_cnpj = input("Informe o CPF ou CNPJ do cliente: ")
    cliente = filtrar_cliente(cpf_cnpj, clientes)

    if not cliente:
        print("\n⛔ Cliente não encontrado. Verifique o CPF ou CNPJ informado. ⛔")
        return

    if not cliente.contas:
        print("\n⛔ O cliente não possui contas cadastradas. ⛔")
        return
    
    print(f"\n=========== Contas de {cliente.nome if isinstance(cliente, PessoaFisica) else cliente.nome_fantasia} ===========")
    for conta in cliente.contas:
        print(textwrap.dedent(str(conta)))
    print("=" * 54)

def main_menu():
    clientes = []
    contas = []

    while True:
        escolha = menu_banco()

        if escolha == "1":
            criar_cliente(clientes)
            print("\nOpção selecionada: Seja nosso cliente")

        elif escolha == "2":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
            print("\nOpção selecionada: Criar Conta")

        elif escolha == "3":
            depositar(clientes)
            print("\nOpção selecionada: Realizar Depósito")

        elif escolha == "4":
            sacar(clientes)
            print("\nOpção selecionada: Realizar Saque")

        elif escolha == "5":
            exibir_extrato(clientes)
            print("\nOpção selecionada: Histórico de Transações")

        elif escolha == "6":
            listar_contas(clientes)
            print("\nOpção selecionada: Listar Contas")

        elif escolha == "7":
            print("\nSaindo do sistema. Até logo!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

main_menu()