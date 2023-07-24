# Desafio : Otimizando o Sistema Bancário

Desafio realizado para o Bootcamp Potência Tech powered by iFood | Ciência de Dados com Python.

## Objetivo Geral

Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções : cadastrar usuário (cliente) e cadastrar conta bancária.

## Desafio 

Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar extrato. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções : criar usuário (cliente do banco) e criar conta corrente (vincular com o usuário) 

#### Separação em funções

Deve-se criar funções para todas as operações do sistema. Para exercitar tudo o que foi aprendido, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.


#### Saque

A função saque deve receber os argumentos apenas por nome (***keyword only***)

#### Depósito 

A função depósito deve receber os argumentos apenas por posição (***positional only***)

#### Extrato 

a função extrato deve receber os argumentos por posição e nome (***positional only e keyword only***). argumentos posicionais : saldo, argumentos nomeados : extrato.

#### Criar Usuário (cliente) 

o programa deve armazenar os usuários em uma lista, um usuário é composto por : nome, data de nascimento, cpf e endereço. Não podemos cadastrar 2 usuários com o mesmo CPF.

#### Criar Conta Corrente 

o programa deve armazenar contas em uma lista, uma conta é composta por : agência, número da conta e usuário. O número da conta é sequencial, começando em 1, e o da agência é fixo : "0001". O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário.


## Links

[ Bootcamp Potência Tech powered by iFood | Ciência de Dados com Python](https://web.dio.me/track/potencia-tech-powered-ifood-ciencias-de-dados-com-python)

[Desafio Otimizando o Sistema Bancário](https://web.dio.me/lab/otimizando-o-sistema-bancario-com-funcoes-python/learning/82a55799-cfb8-479d-85a3-4982e29c90ba)


