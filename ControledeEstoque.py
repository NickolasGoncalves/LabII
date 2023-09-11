
def menu():
    print("## MERCADINHO DO SEU ZÉ ##")
    print("1- Adicionar um produto: ")
    print("2- Buscar um produto: ")
    print("3- Vizualizar todos os produtos: ")
    print("4- Vender um produto: ")
    print("5- Relatório de vendas: ")
    opc = int(input("O que você deseja? "))
    return opc

def adicionar_produto(my_dict):
    product_name = input("Digite o nome do produto (ou deixe vazio para sair): ")
    
    if product_name == '':
        return
    
    product_amount = int(input("Digite a quantidade do produto: "))
    product_price = float(input("Digite o preço do produto: "))

    my_dict[product_name] = {
      "amount": product_amount,
      "price": product_price
    }
    for product_name, product_info in my_dict.items():
        amount = product_info["amount"]
        price = product_info["price"]
        print(f"Produto: {product_name}, Quantidade: {amount}, Preço: {price}")
        
def main():
    my_dict= {}
    
    while True:
        opc = menu()
        if opc == 1:
            while True:
                adicionar_produto(my_dict)
                if input("Deseja adicionar outro produto? (s/n): ").lower() != "s":
                    break
        
    
  



main()
