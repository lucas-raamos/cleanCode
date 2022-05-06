

nome_produtos = []
preco_produtos = []
qtd_produtos = []


nome_produto = input("Digite o nome do produto: ")
if nome_produto not in nome_produtos:
    nome_produtos.append(nome_produto)
else:
    input("Produto ja cadastrado")

preco_produto = input("Digite o preço do produto: ")
if preco_produto not in preco_produtos:
    preco_produtos.append(preco_produto)

qtd_produto = input("Digite a quantidade: ")
if qtd_produto not in preco_produtos:
    preco_produtos.append(qtd_produto)

fim_menu = input("Deseja encerrar o programa? S/N?").lower()
if fim_menu == "s":
    print("Fim do programa!")

print(nome_produtos)
print(preco_produtos)
print(qtd_produtos)
