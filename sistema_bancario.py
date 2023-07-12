menu = """

  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor_depositado = int(input("Informe o valor para depositar : "))
        if valor_depositado < 1:
            print("operação inválida, apenas é aceitável valores positivos.")
        else:
            saldo += valor_depositado
            extrato += f"valor de {valor_depositado:.2f} foi depositado.\n"
            

    elif opcao == "s":    

        if numero_saques == LIMITE_SAQUES:
            print("Não é possivel mais sacar, o limite é 3 saques diários.")
            
        else:
            sacar_valor = int(input("Informe um valor para sacar : "))

            if sacar_valor < 1 :
                print("operação inválida, só é possivel sacar valores positivos")
            elif sacar_valor > saldo:
                print("Não é possivel sacar o dinheiro por falta de saldo na conta.")
            elif sacar_valor > limite:
                print("operação inválida, limite máximo de valor para sacar é R$ 500")
            else:
               saldo -= sacar_valor
               numero_saques += 1
               extrato += f"foi realizado um saque de {sacar_valor:.2f}.\n"
        
    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"Saldo atual : {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("operação inválida, por favor selecione novamente a operação desejada!")
