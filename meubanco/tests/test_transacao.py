import pytest
from meubanco.transacao import Transacao, Saque, Deposito
from meubanco.conta import ContaCorrente
from meubanco.cliente import PessoaFisica
from meubanco.historico import Historico

@pytest.fixture
def cliente():
    return PessoaFisica("Fernando", "01-01-1990", "12345678901", "Rua Exemplo, 123")

@pytest.fixture
def conta(cliente):
    return ContaCorrente.nova_conta(cliente, "0001-1")

def test_saque_valido(conta):
    conta.depositar(100)
    saque = Saque(50)
    saque.registrar(conta)
    assert conta.saldo == 50
    assert len(conta.historico.transacoes) == 1

def test_saque_invalido(conta):
    saque = Saque(150)
    saque.registrar(conta)
    assert conta.saldo == 0
    assert len(conta.historico.transacoes) == 0

def test_deposito_valido(conta):
    deposito = Deposito(100)
    deposito.registrar(conta)
    assert conta.saldo == 100
    assert len(conta.historico.transacoes) == 1

def test_deposito_invalido(conta):
    deposito = Deposito(-50)
    deposito.registrar(conta)
    assert conta.saldo == 0
    assert len(conta.historico.transacoes) == 0

def test_limite_saques_por_conta(conta):
    conta.depositar(500)
    # Supondo que o limite de saques diários seja 3 (ajuste conforme a implementação)
    for _ in range(3):
        saque = Saque(50)
        saque.registrar(conta)
    # Tentar um quarto saque, que deve falhar
    saque_extra = Saque(50)
    saque_extra.registrar(conta)
    # O saldo deve ter sido debitado apenas 3 vezes
    assert conta.saldo == 350
    # Apenas 3 transações de saque devem estar no histórico
    assert len(conta.historico.transacoes) == 3
