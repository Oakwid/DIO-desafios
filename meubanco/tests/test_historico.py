import pytest
from meubanco.historico import Historico
from meubanco.transacao import Deposito, Saque

def test_adicionar_transacao():
    historico = Historico()
    deposito = Deposito(100)
    saque = Saque(50)

    historico.adicionar_transacao(deposito)
    historico.adicionar_transacao(saque)

    assert len(historico.transacoes) == 2
    assert historico.transacoes[0]['tipo'] == 'Deposito'
    assert historico.transacoes[0]['valor'] == 100
    assert historico.transacoes[1]['tipo'] == 'Saque'
    assert historico.transacoes[1]['valor'] == 50

def test_transacoes_vazias():
    historico = Historico()
    assert len(historico.transacoes) == 0