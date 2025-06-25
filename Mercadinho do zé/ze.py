# Função para exibir o menu de opções
def menu():
    print("\nOpções:")
    print("1 - Cadastrar novo item")
    #print("2 - Buscar item")
    print("2 - Listar itens")
    print("X - Sair")
    
    return input("Escolha uma opção: ")

# Função para cadastrar um novo item no estoque
def cadastrar_item():
    print("===============================================")
    nome_prod = input("Insira o nome do produto: ")
    preco_prod = input("Insira o preço do produto: ")
    quantidade_prod = float(input("Insira a quantidade do produto: "))

    # Abre o arquivo em modo de adição e salva os dados do produto
    with open("estoque.txt", "a", encoding="utf-8") as arquivo: 
        arquivo.write(f"{nome_prod}, {preco_prod}, {quantidade_prod}\n")

    print("Item cadastrado com sucesso!")
    print("===============================================")

# Função para buscar um item 
#def buscar_item():
    #nome_do_item = input("Digite o nome do item que deseja buscar: ")
    #for item in itens:
        #print("===============================================")
        #if item["nome"] == nome_do_item:
            #print("Nome:", item["nome"])
            #print("Preço:", item["preço"])
            #print("Quantidade:", item["quantidade"])
        #print("===============================================")

# listar todos os itens do estoque
def listar_itens():
    with open("estoque.txt", "r", encoding="utf-8") as arquivo:
        print("===============================================")
        print("Estoque:\n")
        print(arquivo.read())
        print("===============================================")

# Operador do menu
def principal():
    while True:
        opcao = menu()
        
        if opcao == "1":
            cadastrar_item()
        
        #elif opcao == "2":
            #buscar_item()

        elif opcao == "2":
            listar_itens()

        elif opcao.upper() == "X":
            break

principal()