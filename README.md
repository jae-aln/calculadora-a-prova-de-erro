# Calculadora segura no terminal

Projeto de terminal para praticar validacao de entradas e tratamento de excecoes
em Python. O programa solicita um dividendo e um divisor, repete a leitura
quando a entrada nao e numerica e mostra uma mensagem amigavel se o divisor for
zero.

## Requisitos

- Python 3.10 ou superior

## Executar

No terminal, dentro da pasta do projeto:

```powershell
python calculadora.py
```

Digite os valores solicitados. Por exemplo, `10` e `2` resultam em `5.0`.
Entradas como `dez` ou vazias sao solicitadas novamente.

## Testes

```powershell
python -m unittest -v
```

Os testes cobrem divisao normal, divisor zero, entrada nao numerica e campo
vazio.
