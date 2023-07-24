menu_criacao = """

  [u] Criar Usuário
  [c] Criar conta corrente
  [a] Acessar conta
  [l] Listar Contas
  [q] Sair

=> """


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
usuarios_cpf = []
usuarios_dados = {}
conta_corrente = {}
numero_conta = 0


def depositar(saldo,extrato,/):

    valor_depositado = int(input("Informe o valor para depositar : "))
    if valor_depositado < 1:
        return "operação inválida, apenas é aceitável valores positivos."
    else:
        saldo += valor_depositado
        extrato += f"valor de {valor_depositado:.2f} foi depositado.\n"

        return saldo, extrato


def sacar(*, numero_saques, limite_saques, saldo, extrato, limite):
    if numero_saques == limite_saques:
        return "Não é possivel mais sacar, o limite é 3 saques diários."
    else:
        sacar_valor = int(input("Informe um valor para sacar : "))

        if sacar_valor < 1 :
            return "operação inválida, só é possivel sacar valores positivos"
        elif sacar_valor > saldo:
            return "Não é possivel sacar o dinheiro por falta de saldo na conta."
        elif sacar_valor > limite:
            return "operação inválida, limite máximo de valor para sacar é R$ 500"
        else:
            saldo -= sacar_valor
            numero_saques += 1
            extrato += f"foi realizado um saque de {sacar_valor:.2f}.\n"

            return saldo, numero_saques, extrato



def visualizar_extrato(saldo, /, *, extrato):
    if extrato == "":
        return "Não foram realizadas movimentações."
    else:
        return extrato, f"Saldo atual : {saldo:.2f}"
        


def criar_usuário(nome, data_nascimento,cpf, endereco):
    usuarios_cpf.append(cpf)
    usuarios_dados[cpf] = {"data-nascimento" : data_nascimento, "nome" : nome, "endereço": endereco }
    print("usuário cadastrado com sucesso!")



def verificar_usuario(cpf):
    
    if usuarios_cpf.count(cpf) == 1:
        print("Erro, esse CPF já está cadastrado!")
    else:
        criar_usuário(nome,data_de_nascimento,cpf,endereco)


     

def criar_conta_corrente(cpf): 
    # verificar se o CPF está cadastrado
    if usuarios_cpf.count(cpf) == 1:
        agencia = "0001"
        global numero_conta
        numero_conta += 1
        conta_corrente[cpf] = {"agência" : agencia, "numero_conta": numero_conta, "usuario": usuarios_dados[cpf]["nome"] }
        print("Conta corrente criada com sucesso!")
    else:
        print("Esse CPF é inválido!")


def acessando_conta_corrente(agencia, conta, usuario):
    
    while True:
        print(f"Agência : {agencia} | Conta : {conta} | Usuário : {usuario} ")
        opcao = input(menu)

        if opcao == "d":
            retorno_depositar = depositar(saldo,extrato)

            if type(retorno_depositar) == type(str()):
                print(retorno_depositar)
            else:
                saldo = retorno_depositar[0]
                extrato = retorno_depositar[1]
            

        elif opcao == "s":    

            retorno_sacar = sacar(numero_saques=numero_saques,
                                     limite_saques=LIMITE_SAQUES,
                                     saldo=saldo,
                                     extrato=extrato,
                                     limite=limite)

            if type(retorno_sacar) == type(str()):
                print(retorno_sacar)
            else:
                saldo = retorno_sacar[0]
                numero_saques = retorno_sacar[1] 
                extrato = retorno_sacar[2]
        
        elif opcao == "e":

            retorno_extrato = visualizar_extrato(saldo, extrato= extrato)
            if retorno_extrato == "Não foram realizadas movimentações.":
                print(retorno_extrato)
            else:
                print(retorno_extrato[0] + "\n" + retorno_extrato[1])

        elif opcao == "q":
            break

        else:
            print("operação inválida, por favor selecione novamente a operação desejada!")


while True:

    opcao_menu = input(menu_criacao)

    if opcao_menu == "u":
        nome = input("Informe seu nome : ")
        data_de_nascimento = input("Informa a data de nascimento : ")
        cpf = int(input("Informe o CPF(somente números) : "))
        endereco = input("Informe o endereço (ex : rua - numero - bairro - cidade/sigla estado) : ")

        verificar_usuario(cpf)
                     
    elif opcao_menu == "c":
        cpf = int(input("Informe o CPF(somente números) : "))
        criar_conta_corrente(cpf)

    elif opcao_menu == "a":
        cpf = int(input("Informe o CPF(somente números) : "))
        conta_existe = conta_corrente.get(cpf, False)

        if conta_existe == False:
            print("Erro, essa conta não existe!")
        else:
            arg_1 = conta_corrente[cpf]["agência"]
            arg_2 = conta_corrente[cpf]["numero_conta"]
            arg_3 = conta_corrente[cpf]["usuario"]
            acessando_conta_corrente(arg_1, arg_2, arg_3)

    elif opcao_menu == "l":
        if conta_corrente == {}:
            print("Nenhuma conta foi cadastrada no momento!")
        else:
            for chave in conta_corrente:
                print(f""" 
                Agência : {conta_corrente[chave]["agência"]}
                Número da Conta : {conta_corrente[chave]["numero_conta"]}
                CPF : {chave}
                Usuário : {conta_corrente[chave]["usuario"]}
""")  
    
    elif opcao_menu == "q":
        break

    else:
        print("operação inválida, por favor selecione novamente a operação desejada!")






