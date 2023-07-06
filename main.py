# Desafio DIO - Sistema bancário V1


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

### CODIGO ###
LIMITE_SAQUE = 3
LIMITE_VALOR = 500.00

saques_diario = 0
movimentacoes = list()
saldo = 0

print("\n## Banco SeuDinheiroEhNosso ##")
print("Seja Bem-vindo(a).".center(30, "#"))

entrada = ""
while entrada != "0":
        print("\nEscolha uma opção:")
        print("[1] - Depósito\n[2] - Saque\n[3] - Extrato")
        print("[0] - Sair")

        entrada = input("Escolha: ")


        # Depositando
        if entrada == "1":
             
            valor = input("Valor do depósito: ")
            valor = validar_valor(valor)

            if valor > 0:
                movimentacoes.append(valor)
                saldo += valor
                print(f"Depósito efetuado. Seu novo saldo é de {saldo:.2f}")
                

        # Sacando
        elif entrada == "2":

            if saques_diario >= LIMITE_SAQUE:
                valor = 0
                print("Limite de saques diário excedido.")
            else:
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
                print(f"Saque efetuado. Seu novo saldo é de {saldo:.2f}")

        # Extrato
        elif entrada == "3":

            print("\n###### Extrato ######\n")
            for movimento in movimentacoes:
                if movimento < 0:
                    texto = "Saída  "
                else:
                    texto = "Entrada"
                print(f"{texto} > R$ {movimento:.2f}")
            print(f"Saldo   = R$ {saldo:.2f}")
            print("\n"+"#"*25)


        else:
             print("Encerrando...")