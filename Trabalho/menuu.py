def show_menu():
    """Menu de Opções"""
    print(30*'-_')
    print("##  MERCADINHO DO SEU ZÉ ##")
    print("1- Adicionar um produto: ")
    print("2- Buscar um produto: ")
    print("3- Vizualizar todos os produtos: ")
    print("4- Vender um produto: ")
    print("5- Relatório de vendas: ")
    print(30*'-_')
    opc = int(input("O que você deseja? "))
    return opc
