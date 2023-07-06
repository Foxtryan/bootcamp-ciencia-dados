LIMITE_SAQUE = 3
LIMITE_VALOR = 500.00
OPCOES = {
    "1": lambda opc: deposito(),
    "2": lambda opc: saque(),
    "3": lambda opc: extrato(),
    "0": lambda opc: print("Encerrando..."),
}

saldo = 0
saques_diario = 0
movimentacoes = list()


def menu():
    
    entrada = ""
    while entrada != '0':
        
        print("\nEscolha uma opção:")
        print("[1] - Depósito")
        print("[2] - Saque")
        print("[3] - Consultar Extrato")
        print("[0] - Sair")

        entrada = input("Escolha: ")
        if entrada in OPCOES.keys():
            OPCOES[entrada]("opc")


def deposito():

    global saldo

    valor = input("Valor do depósito: ")
    valor = validar_valor(valor)

    if valor > 0:
        movimentacoes.append(valor)
        saldo += valor
        print(f"Depósito efetuado. Seu novo saldo é de {saldo}")

def saque():

    global saques_diario, saldo

    if saques_diario >= LIMITE_SAQUE:
        print("Limite de saques diário excedido.")
        return
    
    valor = input("Valor do saque: ")
    valor = validar_valor(valor)

    if valor > 500:
        print(f"Valor acima do limite permitido.\nSeu Limite é de {LIMITE_VALOR:.2f} por saque.")

    elif valor > saldo:
        print(f"Seu saldo é insuficiente. Seu saldo total é de {saldo:.2f}")

    elif valor > 0:
        saques_diario += 1
        movimentacoes.append(valor * -1)
        saldo -= valor
        print(f"Saque efetuado. Seu novo saldo é de {saldo}")

def extrato():

    print("\n###### Extrato ######\n")
    for movimento in movimentacoes:
        if movimento < 0:
            texto = "Saída  "
        else:
            texto = "Entrada"
        print(f"{texto} > R$ {movimento:.2f}")
    print(f"Saldo   = R$ {saldo:.2f}")
    print("\n"+"#"*25)


def validar_valor(valor):

    # Verifica se é um número.
    try:
        valor = float(valor)
    except ValueError:
        valor = 0
        print("É necessário um valor numérico positivo.")

    # Verificar se o número é positivo.
    if valor < 0:
        valor = 0
        print("É necessário um valor numérico positivo.")
    return valor


def inicio():

    print("\n## Banco SeuDinheiroEhNosso ##")
    print(" Seja Bem-vindo ".center(30, "#"))
    menu()


if __name__ == '__main__':
    inicio()