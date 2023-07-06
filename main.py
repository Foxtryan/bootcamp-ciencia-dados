# Desafio DIO - Sistema bancário V2
from textwrap import dedent

def inicio():

    LIMITE_SAQUE = 3
    LIMITE_VALOR = 500.00
    numero_saques = 0
    saldo = 0
    movimentacoes = list()
    usuarios = list()
    contas = list()
    usuario_ativo = ""

    print("\n## Banco SeuDinheiroEhNosso ##")
    print("Seja Bem-vindo(a).".center(30, "#"))

    entrada = ""
    while entrada != "0":

        # Se não existe usuário ativo
        if usuario_ativo not in usuarios:

            entrada = menu_login()

            # Fazer Login
            if entrada == "1":
                 
            # Criar Usuário
            elif entrada == "2":
                
            # Criar Conta
            elif entrada =="3":

            # Outra entrada - sair
            else:
                print("Encerrando...")
                 
        else:

            # Depósito
            if entrada == "1":
        
            # Saque
            elif entrada == "2":
        
            # Extrato
            elif entrada == "3"
    
            # Nova Conta
            elif entrada == "4"
    
            # Trocar Usuário
            elif entrada == "5"
            entrada = menu()
        
            # Sair
            else:
                print("Encerrando...")
            

def menu_login():

    print(dedent("""
    [1] - Fazer Login
    [2] - Criar Usuário
    [3] - Criar Conta
    [0] - Sair
    """))
    entrada = input("\nEscolha uma opção: ")

    return entrada


def menu():

    print("[1] - Novo Usuário\n[2] - Nova Conta")
    print("[3] - Depósito\n[4] - Saque\n[5] - Extrato")
    print("[0] - Sair")

    print(dedent("""
    [1] - Depósito
    [2] - Saque
    [3] - Ver Extrato
    [4] - Nova Conta
    [5] - Trocar usuário
    """))

    entrada = input("\nEscolha uma opção: ")

    return entrada


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    return saldo, extrato

def extrato(saldo, /, *, extrato): pass

def criar_usuario(usuarios): 
     

    # [Nome, nascimento, cpf, endereço]
    # endereco = 'Rua Hortênsia, 11 - Jardim Alto - Lagoa Azul/MG'
def filtrar_usuarioas(cpf, usuarios): pass 


def criar_conta(usuario): pass
    # agencia, numero, usuario
    # uma conta pertence a somente um usuario


if __name__ == '__main__':
    inicio()