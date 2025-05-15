# README para o pacote meubanco

## Descrição

O meubanco é um sistema de gerenciamento bancário desenvolvido em Python, utilizando Programação Orientada a Objetos (POO), para fins educacionais. O sistema permite a criação de clientes, contas bancárias e a realização de transações como depósitos e saques, além de manter um histórico dessas transações.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```text
meubanco/
├── meubanco/
│   ├── __init__.py
│   ├── cliente.py
│   ├── conta.py
│   ├── historico.py
│   ├── transacao.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_cliente.py
│   ├── test_conta.py
│   ├── test_historico.py
│   └── test_transacao.py
├── __init__.py
├── __main__.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## Instalação local

Para instalar o projeto, clone o repositório e instale as dependências necessárias:

```bash
git clone https://github.com/Oakwid/DIO-desafios/meubanco.git
cd meubanco
pip install .
```

### Instalando via PyPI

Instale o pacote diretamente do PyPI usando o `pip`:

```bash
pip install meubanco
```

## Uso

Para executar o sistema bancário, utilize o seguinte comando:

```bash
python -m meubanco
```

Siga as instruções no menu para interagir com o sistema.

## Testes

Para executar os testes, navegue até a raiz do projeto (onde está o setup.py) e rode:

```bash
pytest tests
```

ou simplesmente:

```bash
pytest
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
