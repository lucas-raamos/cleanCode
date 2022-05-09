
nomeProdutos = []
precoProdutos = []
qtdProdutos = []

def nomesProdutos():
    while True:
        nomeProduto = input("Digite o nome do produto: ")
        if nomeProduto not in nomeProdutos:
            nomeProdutos.append(nomeProduto)
        else:
            input("Produto ja cadastrado")
        precosProdutos()
        menu()


def precosProdutos():
    while True:
        precoProduto = input("Digite o preço do produto: ")
        if precoProduto not in precoProdutos:
            precoProdutos.append(precoProduto)
        qtdsProdutos()


def qtdsProdutos():
    while True:
        qtdProduto = input("Digite a quantidade: ")
        if qtdProduto not in precoProdutos:
            precoProdutos.append(qtdProduto)
        input("Produto cadastrado!!! [ENTER] ")
        menu()



def fimPrograma():
    while True:
        fimMenu = input("Deseja encerrar o programa? S/N?").lower()
        if fimMenu not in "sn" or fimMenu == "":
            input("Escolha apenas s ou n, por favor [ENTER]")
            continue
        if fimMenu == "s":
            print("Fim do programa!")
            exit()
        else: break

def imprimirProdutoEscolhido():
    print(nomeProdutos)
    produtoEscolhido = input("Digite um produto: ")
    for ind, produto in enumerate(nomeProdutos):
        if produto == produtoEscolhido:
            print("\t-", nomeProdutos[ind])
        input("[ENTER]")

def excluirPeloNome():
    print("Excluir produto")
    print(nomeProdutos)
    produtoExcluir = input("Digite o produto a ser excluído: ")
    for ind, produto in enumerate(nomeProdutos):
        if produto == produtoExcluir:
            nomeProdutos.pop(ind)
    input("Exclusão realizada. [ENTER]")

def menu():
    while True:
        escolha = input('''
        Menu
        0 - Finalizar o Programa
        1 - Cadastrar produtos
        2 - Imprimir um produto
        3 - Excluir um produto
        Escolha: ''')

        if escolha == "0": fimPrograma()
        elif escolha == "1": nomesProdutos()
        elif escolha == "2": imprimirProdutoEscolhido()
        elif escolha == "3": excluirPeloNome()
        else: input("Opção inválida [ENTER]")
menu()