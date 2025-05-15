from meubanco.cliente import Cliente,PessoaFisica, PessoaJuridica
from meubanco.transacao import Transacao, Saque, Deposito
from meubanco.conta import Conta, ContaCorrente

def test_cliente_inicializacao():
    cliente_pf = PessoaFisica("Fernando", "01-01-1990", "12345678909", "Rua A, 123 - Bairro - Cidade/Estado")
    assert cliente_pf.nome == "Fernando"
    assert cliente_pf.data_nascimento == "01-01-1990"
    assert cliente_pf.cpf == "12345678909"
    assert cliente_pf.endereco == "Rua A, 123 - Bairro - Cidade/Estado"
    assert cliente_pf.contas == []

    cliente_pj = PessoaJuridica("Empresa X", "01-01-2000", "12345678000195", "Avenida B, 456 - Bairro - Cidade/Estado")
    assert cliente_pj.nome_fantasia == "Empresa X"
    assert cliente_pj.data_fundacao == "01-01-2000"
    assert cliente_pj.cnpj == "12345678000195"
    assert cliente_pj.endereco == "Avenida B, 456 - Bairro - Cidade/Estado"
    assert cliente_pj.contas == []

def test_adicionar_conta():
    cliente = PessoaFisica("Fernando", "01-01-1990", "12345678909", "Rua A, 123 - Bairro - Cidade/Estado")
    conta = ContaCorrente("0001", cliente)
    cliente.adicionar_conta(conta)
    assert len(cliente.contas) == 1
    assert cliente.contas[0] == conta

def test_realizar_transacao():
    cliente = PessoaFisica("Fernando", "01-01-1990", "12345678909", "Rua A, 123 - Bairro - Cidade/Estado")
    conta = ContaCorrente("0001", cliente)
    cliente.adicionar_conta(conta)
    
    # Simula uma transação
    transacao = Deposito(100)
    cliente.realizar_transacao(conta, transacao)