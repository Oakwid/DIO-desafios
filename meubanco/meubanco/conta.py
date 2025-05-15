from meubanco.cliente import Cliente, PessoaFisica, PessoaJuridica
from meubanco.historico import Historico
from meubanco.transacao import Saque, Deposito
from datetime import datetime

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
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
            return False

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
            return True
        else:
            print("\n⛔ Operação falhou! O valor informado é inválido. ⛔")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n⛔ Operação falhou! O valor do saque excede o limite. ⛔")
            return False

        elif excedeu_saques:
            print("\n⛔ Operação falhou! Número máximo de saques excedido. ⛔")
            return False

        else:
            return super().sacar(valor)

    def __str__(self):
        titular = self.cliente.nome if isinstance(self.cliente, PessoaFisica) else self.cliente.nome_fantasia
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero} 
            Titular:\t{titular} 
        """