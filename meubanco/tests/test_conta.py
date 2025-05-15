import pytest
from meubanco.cliente import Cliente, PessoaFisica, PessoaJuridica
from meubanco.conta import ContaCorrente
from meubanco.transacao import Saque, Deposito

@pytest.fixture
def cliente_pf():
    return PessoaFisica("Fernando", "01-01-1990", "12345678909", "Rua A, 123 - Cidade/Estado")

@pytest.fixture
def cliente_pj():
    return PessoaJuridica("Empresa X", "01-01-2000", "12345678000195", "Rua B, 456 - Cidade/Estado")

@pytest.fixture
def conta_corrente(cliente_pf):
    return ContaCorrente.nova_conta(cliente_pf, "0001")

def test_deposito(conta_corrente):
    conta_corrente.depositar(100)
    assert conta_corrente.saldo == 100

def test_saque(conta_corrente):
    conta_corrente.depositar(200)
    sucesso = conta_corrente.sacar(150)
    assert sucesso is True
    assert conta_corrente.saldo == 50

def test_saque_insuficiente(conta_corrente):
    conta_corrente.depositar(100)
    sucesso = conta_corrente.sacar(150)
    assert sucesso is False
    assert conta_corrente.saldo == 100

def test_criacao_conta_corrente(cliente_pf):
    conta = ContaCorrente.nova_conta(cliente_pf, "0002")
    assert conta.numero == "0002"
    assert conta.cliente == cliente_pf
    assert conta.saldo == 0

def test_limite_valor_saque(conta_corrente):
    conta_corrente.depositar(1000)
    # Tenta sacar um valor acima do limite permitido por saque (500)
    assert conta_corrente.sacar(600) is False
    # O saldo deve permanecer inalterado
    assert conta_corrente.saldo == 1000

def test_deposito_valor_invalido(conta_corrente):
    # Tenta depositar um valor negativo
    assert conta_corrente.depositar(-50) is False
    # Tenta depositar zero
    assert conta_corrente.depositar(0) is False
    # O saldo deve permanecer zero
    assert conta_corrente.saldo == 0

def test_saque_valor_invalido(conta_corrente):
    conta_corrente.depositar(100)
    # Tenta sacar um valor negativo
    assert conta_corrente.sacar(-10) is False
    # Tenta sacar zero
    assert conta_corrente.sacar(0) is False
    # O saldo deve permanecer inalterado
    assert conta_corrente.saldo == 100

def test_str_conta_corrente(cliente_pf):
    conta = ContaCorrente.nova_conta(cliente_pf, "1234")
    output = str(conta)
    assert "Agência:" in output
    assert "C/C:" in output
    assert "Titular:" in output
    assert cliente_pf.nome in output
