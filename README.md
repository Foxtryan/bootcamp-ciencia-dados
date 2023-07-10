# bootcamp-ciencia-dados
Bootcamp Ciência de Dados com Python - DIO &amp; iFood
Potência Tech powered by iFood | Ciências de Dados com Python

# Desafio de Projeto 1 -  Criar um sistema bancário simples com Python

  Deve ser possível realizar as operações de sacar, depositar e visualizar extrato.

  **Depósito**: Deve ser possível depositar valores positivos. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número de agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

  **Saque**: Deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

  **Extrato**: Deve listar todos os depósitos e saques na conta. No fim deve ser exibido o saldo atual da conta no formato R$ XXX.XX.
  
# Desafio de Projeto 2 - Aprimorar o sistema bancário com Python

  Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário e cadastrar conta bancária (vinculada com usuário).

  **Regras**:
  
  A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

  A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

  A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

  O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, número - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.
  
  O programa deve armazenar as contas em uma lista, uma conta é composta por agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário. Fique a vontade para adicionar novas funções, por exemplo: listar contas.
  
  
